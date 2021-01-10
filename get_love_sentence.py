import requests
from lxml import etree
import re

def save_file(love_sentences):
    with open('love_yaya.csv', 'a', encoding='utf-8') as f:
        for context in love_sentences:
            f.write('{}\n'.format(context))

def read_url():
    base_url = 'https://m.kuaidu.com.cn/article/207521_{}.html'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    love_sentences = []
    for num in range(1, 11):
        url = base_url.format(num)
        resp = requests.get(url, headers=header)
        text = resp.content.decode('utf-8')
        html = etree.HTML(text)
        contexts = html.xpath('//div[@class="mycontext"]/p/text()')
        for ctx in contexts:
            ctx = re.sub(r'\n', '', str(ctx))
            ctx = re.sub(r' ', '', ctx)
            ctx = re.sub(r'[0-9]+?、', '', ctx)
            love_sentences.append(ctx)
    save_file(love_sentences)

if __name__ == '__main__':
    read_url()
