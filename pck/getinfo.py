import random
import re
from lxml import etree


def get_text():
    d = {}
    for i in open("word.txt", "r", encoding='utf-8').readlines():
        d[re.findall(r'\..*?<(.*?)\n', i)[0]] = re.findall(r'\.(.*?)<.*?\n', i)[0]
    m = random.sample(d.keys(), 4)
    m.insert(0, d[m[0]].strip(' '))
    return m


def get_zh(w):
    html = etree.parse("http://cn.bing.com/dict/search?q=" + w, etree.HTMLParser())
    d = []
    en = html.xpath('//*[@id="sentenceSeg"]/div/div[2]/div[1]')
    zh = html.xpath('//*[@id="sentenceSeg"]/div/div[2]/div[2]')
    for i in range(len(en)):
        if re.match(r'.*?\. \. \.', en[i].xpath("string(.)")) is None:
            try:
                d.append([en[i].xpath("string(.)"), zh[i].xpath("string(.)").encode('ISO-8859-1').decode('utf-8')])
            except Exception:
                pass
    return random.sample(d, 3)
