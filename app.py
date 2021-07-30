from flask import Flask, render_template
import random
import re
from lxml import etree
app = Flask(__name__)


def get_text():
    d = {}
    for i in open("word.txt", "r", encoding='utf-8').readlines():
        d[re.findall(r'\..*?<(.*?)\n', i)[0]] = re.findall(r'\.(.*?)<.*?\n', i)[0]
    m = random.sample(d.keys(), 4)
    m.insert(0, d[m[0]].strip(' '))
    return m


def get_zh(w):
    html = etree.parse("http://m.youdao.com/singledict?dict=blng_sents&more=true&q=" + w, etree.HTMLParser())
    d = []
    en = html.xpath('//*[@id="bd"]/div/ul/li/div[2]/p[1]')
    zh = html.xpath('//*[@id="bd"]/div/ul/li/div[2]/p[2]')
    for i in range(len(en)):
        d.append([en[i].xpath("string(.)"), zh[i].xpath("string(.)")])
    return random.sample(d, 3)


@app.route('/')
def index():
    t = get_text()
    return render_template(
        'index.html',
        text=t,
        zhs=get_zh(t[0])
    )


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
