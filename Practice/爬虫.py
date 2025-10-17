import requests

def get_web_info(url):
    """
    获取在线网页信息的通用函数
    """
    try:
        # 向目标网页发出请求
        response = requests.get(url)

        # 检查请求状态
        print(f"状态码: {response.status_code}")

        # 自动检测并设置编码
        response.encoding = response.apparent_encoding

        # 返回网页内容
        return response.text

    except Exception as e:
        print(f"请求失败: {e}")
        return None

# 使用示例
url = 'http://www.weather.com.cn/'
html_text = get_web_info(url)

if html_text:
    print("网页获取成功！")
    print(f"网页内容长度: {len(html_text)} 字符")
    # 打印前500个字符预览
    print(html_text[:500])
else:
    print("网页获取失败！")