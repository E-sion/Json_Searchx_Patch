import os
from bs4 import BeautifulSoup
import csv

# 修改file名称为导出的html文件，有多个文件则运行一次改一次~
# 例如：file = r"messages2.html"

file = r""


def Name_ID_csv(file):
    # 读取HTML文件
    with open(file, 'r',encoding='utf-8') as f:
        html_content = f.read()

    # 创建BeautifulSoup对象解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 提取每个id和对应的标题内容
    data = []
    messages = soup.find_all('div', class_='message')
    for message in messages:
        message_id = message['id'].replace('message', '')
        title_element = message.find('div', class_='title bold')
        if title_element:
            title = title_element.text.strip()
            data.append([message_id, title])

    # 写入CSV文件
    csv_file = '文件名称和id.csv'
    write_header = not os.path.exists(csv_file)  # 判断文件是否存在来确定是否写入标题行
    with open(csv_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(['ID', 'Title'])
        writer.writerows(data)



Name_ID_csv(file)
