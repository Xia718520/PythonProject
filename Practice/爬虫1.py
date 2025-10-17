import requests
from bs4 import BeautifulSoup
import csv

# 1. 目标URL
url = 'https://movie.douban.com/top250'

# 2. 设置请求头，模拟浏览器访问，避免被反爬
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# 3. 发送HTTP GET请求
response = requests.get(url, headers=headers)

# 4. 检查请求是否成功
if response.status_code == 200:
    # 5. 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 6. 查找所有包含电影信息的div
    movie_list = soup.find_all('div', class_='info')

    # 7. 准备一个列表来存储数据
    movies = []

    # 8. 遍历每个电影区块，提取具体信息
    for movie in movie_list:
        # 提取电影标题（在<span class="title">里）
        title = movie.find('span', class_='title').get_text()
        # 提取评分（在<span class="rating_num">里）
        rating = movie.find('span', class_='rating_num').get_text()

        # 将数据存入列表
        movies.append([title, rating])
        # 打印到控制台
        print(f"电影：{title}， 评分：{rating}")

    # 9. （可选）保存到CSV文件
    with open('douban_top250.csv', 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        writer.writerow(['电影标题', '评分']) # 写入表头
        writer.writerows(movies) # 写入数据

    print("数据已保存到 douban_top250.csv")

else:
    print(f"请求失败，状态码：{response.status_code}")