# -*- coding: utf-8 -*-
# 贝叶斯判别 + 可视化 + 对话框输入（支持两种判别规则：MAP 与 最小风险）
# 该文件包含详细中文注释，支持在对话框里输入先验、类条件概率，并可选择判别方法

import tkinter as tk                 # 用于创建 GUI 界面
from tkinter import messagebox       # 用于弹出消息对话框
import random                         # 用于生成演示用的随机样本
import matplotlib.pyplot as plt      # 用于绘图

# ===========================
# 统计判别相关函数
# ===========================

def bayes_classifier(priors, likelihoods):
    """
    计算后验概率 P(类别|特征)
    priors: dict {类别: P(类别)}
    likelihoods: dict {类别: P(特征|类别)}
    返回: posteriors dict {类别: P(类别|特征)}
    """
    # 计算边缘概率 P(特征)
    evidence = sum(priors[c] * likelihoods[c] for c in priors)
    if evidence == 0:
        # 避免除零
        raise ZeroDivisionError("证据（边缘概率）为 0，无法计算后验概率")
    posteriors = {c: (priors[c] * likelihoods[c]) / evidence for c in priors}
    return posteriors


def classify_map(posteriors):
    """
    MAP 判别：选择后验概率最大的类别
    """
    return max(posteriors, key=posteriors.get)


def min_risk_decision(posteriors, cost_true):
    """
    最小风险判别（给定 "错法代价" 与后验概率，选择期望风险最小的预测类别）

    这里我们使用的损失矩阵 L(i,j) 定义为：
      L(i, j) = 0               if i == j (正确分类)
      L(i, j) = cost_true[i]    if i != j (把真实为 i 的样本判为 j 的代价为 cost_true[i])

    这样，预测为 j 时的期望风险为：
      R(j) = sum_{i != j} cost_true[i] * P(i|x)

    posteriors: dict {类别: P(类别|特征)}
    cost_true: dict {真实类别: 代价权重（正数）}
    返回: (best_class, risks_dict)
    """
    classes = list(posteriors.keys())
    risks = {}
    # 总风险计算：对每个可能的预测 j，累加真实为 i 且 i!=j 时的代价*后验概率
    for j in classes:
        r = 0.0
        for i in classes:
            if i == j:
                continue
            # cost_true[i] 表示真实类别为 i 时被错判的损失权重
            r += cost_true.get(i, 1.0) * posteriors[i]
        risks[j] = r
    # 选择期望风险最小的预测类
    best = min(risks, key=risks.get)
    return best, risks


# ===========================
# GUI：对话框输入 + 判别方法选择 + 可视化
# ===========================

def run_dialog():
    """
    创建 Tkinter 对话框，让用户输入先验、条件概率，并选择判别方法
    支持：
      - MAP（最大后验）
      - 最小风险（可设置真实类别的错判代价：城市>森林>农田）
    """
    def calculate():
        """按钮回调：读取输入、计算后验、根据选择的规则判别并绘图"""
        try:
            # 读取先验概率并检查数值
            priors = {
                "农田": float(prior_farmland.get()),
                "森林": float(prior_forest.get()),
                "城市": float(prior_city.get())
            }
            # 检查先验是否在 [0,1]
            for k, v in priors.items():
                if v < 0 or v > 1:
                    messagebox.showerror("输入错误", f"先验概率 {k} 必须在 [0,1] 之间")
                    return
            # 可选：检查先验和是否约等于 1（给予提示，不强制）
            s = sum(priors.values())
            if abs(s - 1.0) > 1e-6:
                # 给出提醒，但允许继续（某些练习题可能不要求严格归一化）
                if not messagebox.askyesno("先验和不为1", f"先验概率之和为 {s:.4f}，是否继续？"):
                    return

            # 读取类条件概率
            likelihoods = {
                "农田": float(like_farmland.get()),
                "森林": float(like_forest.get()),
                "城市": float(like_city.get())
            }
            for k, v in likelihoods.items():
                if v < 0 or v > 1:
                    messagebox.showerror("输入错误", f"条件概率 P(特征|{k}) 必须在 [0,1] 之间")
                    return

            # 读取代价权重（最小风险规则使用），若用户未改动使用默认值
            cost_true = {
                "农田": float(cost_farmland.get()),
                "森林": float(cost_forest.get()),
                "城市": float(cost_city.get())
            }
            for k, v in cost_true.items():
                if v < 0:
                    messagebox.showerror("输入错误", f"代价 {k} 必须为非负数")
                    return

            # 计算后验概率
            try:
                posteriors = bayes_classifier(priors, likelihoods)
            except ZeroDivisionError as e:
                messagebox.showerror("计算错误", str(e))
                return

            # 判断使用哪种判别规则
            method = method_var.get()
            if method == "MAP（最大后验）":
                decision = classify_map(posteriors)
                info_lines = [f"P({c}|特征) = {posteriors[c]:.4f}" for c in posteriors]
                info = "\n".join(info_lines) + f"\n\n判别方法：{method}\n判别结果：{decision}"

                # 可视化：仅显示后验概率
                plt.figure(figsize=(6, 4))
                plt.bar(list(posteriors.keys()), list(posteriors.values()), color=["green", "blue", "red"])
                plt.title(f"后验概率分布（{method}）")
                plt.ylim(0, 1)
                for i, v in enumerate(posteriors.values()):
                    plt.text(i, v + 0.02, f"{v:.2f}", ha='center')
                plt.show()

            else:  # 最小风险判别
                decision, risks = min_risk_decision(posteriors, cost_true)
                info_lines = [f"P({c}|特征) = {posteriors[c]:.4f}" for c in posteriors]
                risk_lines = [f"R(判为{c}) = {risks[c]:.4f}" for c in risks]
                info = "\n".join(info_lines) + "\n\n" + "\n".join(risk_lines) + f"\n\n判别方法：{method}\n判别结果：{decision}"

                # 可视化：左图为后验概率，右图为各预测类的期望风险
                fig, axs = plt.subplots(1, 2, figsize=(12, 4))
                axs[0].bar(list(posteriors.keys()), list(posteriors.values()), color=["green","blue","red"])
                axs[0].set_title("后验概率分布")
                axs[0].set_ylim(0, 1)
                for i, v in enumerate(posteriors.values()):
                    axs[0].text(i, v + 0.02, f"{v:.2f}", ha='center')

                axs[1].bar(list(risks.keys()), list(risks.values()), color=["green","blue","red"])
                axs[1].set_title("预测为某类别时的期望风险")
                # 在风险图上显示数值
                for i, v in enumerate(risks.values()):
                    axs[1].text(i, v + max(risks.values())*0.02, f"{v:.2f}", ha='center')

                plt.suptitle(f"最小风险判别（代价：城市>{cost_true['城市']}, 森林>{cost_true['森林']}, 农田>{cost_true['农田']}）")
                plt.show()

            # 最后弹窗显示文本信息（后验与判别或风险）
            messagebox.showinfo("计算结果", info)

        except ValueError:
            # 捕获 float 转换异常
            messagebox.showerror("输入错误", "请输入有效的数值（例如 0.5）")

    # ---------------- GUI 元素创建 ----------------
    dialog = tk.Tk()
    dialog.title("贝叶斯判别输入（支持 MAP 与 最小风险）")

    # 先验输入区域
    tk.Label(dialog, text="请输入先验概率（P(类别)）：").grid(row=0, column=0, columnspan=4)

    tk.Label(dialog, text="农田").grid(row=1, column=0)
    prior_farmland = tk.Entry(dialog, width=8)
    prior_farmland.grid(row=1, column=1)
    prior_farmland.insert(0, "0.5")  # 默认值

    tk.Label(dialog, text="森林").grid(row=1, column=2)
    prior_forest = tk.Entry(dialog, width=8)
    prior_forest.grid(row=1, column=3)
    prior_forest.insert(0, "0.3")

    tk.Label(dialog, text="城市").grid(row=1, column=4)
    prior_city = tk.Entry(dialog, width=8)
    prior_city.grid(row=1, column=5)
    prior_city.insert(0, "0.2")

    # 条件概率输入区域
    tk.Label(dialog, text="请输入条件概率 P(特征|类别)：").grid(row=2, column=0, columnspan=6, pady=(10,0))

    tk.Label(dialog, text="农田").grid(row=3, column=0)
    like_farmland = tk.Entry(dialog, width=8)
    like_farmland.grid(row=3, column=1)
    like_farmland.insert(0, "0.7")

    tk.Label(dialog, text="森林").grid(row=3, column=2)
    like_forest = tk.Entry(dialog, width=8)
    like_forest.grid(row=3, column=3)
    like_forest.insert(0, "0.5")

    tk.Label(dialog, text="城市").grid(row=3, column=4)
    like_city = tk.Entry(dialog, width=8)
    like_city.grid(row=3, column=5)
    like_city.insert(0, "0.3")

    # 判别方法选择（下拉菜单）
    tk.Label(dialog, text="选择判别方法：").grid(row=4, column=0, pady=(10,0))
    method_var = tk.StringVar(dialog)
    method_var.set("MAP（最大后验）")
    method_menu = tk.OptionMenu(dialog, method_var, "MAP（最大后验）", "最小风险（有代价）")
    method_menu.grid(row=4, column=1, columnspan=2, pady=(10,0))

    # 若选择最小风险，可设置真实类别的代价权重（城市>森林>农田）
    tk.Label(dialog, text="（仅当选择最小风险时生效）错判代价（真实类别的权重）：").grid(row=5, column=0, columnspan=6)

    tk.Label(dialog, text="农田").grid(row=6, column=0)
    cost_farmland = tk.Entry(dialog, width=8)
    cost_farmland.grid(row=6, column=1)
    cost_farmland.insert(0, "1")   # 默认最小代价

    tk.Label(dialog, text="森林").grid(row=6, column=2)
    cost_forest = tk.Entry(dialog, width=8)
    cost_forest.grid(row=6, column=3)
    cost_forest.insert(0, "2")

    tk.Label(dialog, text="城市").grid(row=6, column=4)
    cost_city = tk.Entry(dialog, width=8)
    cost_city.grid(row=6, column=5)
    cost_city.insert(0, "3")   # 默认最大代价（城市>森林>农田）

    # 计算按钮
    tk.Button(dialog, text="计算", command=calculate, bg="#4CAF50", fg="white", padx=10).grid(row=7, column=0, columnspan=6, pady=12)

    # 启动窗口主循环
    dialog.mainloop()


# ===========================
# 可视化演示（保留）
# ===========================

def visualize_demo():
    """随机生成样本并用 MAP 判别做一个示意图（保留用于演示）"""
    classes = ["农田", "森林", "城市"]
    priors = {"农田": 0.5, "森林": 0.3, "城市": 0.2}

    samples = []
    for _ in range(50):
        true_class = random.choice(classes)
        if true_class == "农田":
            feature = random.gauss(0.7, 0.1)
        elif true_class == "森林":
            feature = random.gauss(0.5, 0.1)
        else:
            feature = random.gauss(0.3, 0.1)
        feature = min(max(feature, 0.0), 1.0)
        likelihoods = {c: 1 - abs(feature - (0.7 if c == '农田' else 0.5 if c == '森林' else 0.3)) for c in classes}
        posteriors = bayes_classifier(priors, likelihoods)
        pred_class = classify_map(posteriors)
        samples.append((true_class, pred_class, feature))

    colors = {"农田": "green", "森林": "blue", "城市": "red"}
    markers = {"农田": "o", "森林": "s", "城市": "D"}

    plt.figure(figsize=(8, 4))
    for true_cls, pred_cls, feature in samples:
        edgecolor = "black" if true_cls == pred_cls else "yellow"
        plt.scatter(feature, 0, c=colors[true_cls], marker=markers[pred_cls], edgecolors=edgecolor, s=100)

    plt.axvline(0.4, color="gray", linestyle="--")
    plt.axvline(0.6, color="gray", linestyle="--")
    plt.title("贝叶斯分类结果示意")
    plt.xlabel("特征值")
    plt.ylim(-0.5, 0.5)
    plt.show()


# ===========================
# 程序入口
# ===========================
if __name__ == "__main__":
    # 先运行对话框交互
    run_dialog()
    # 对话框关闭后做一个演示（可注释）
    visualize_demo()
