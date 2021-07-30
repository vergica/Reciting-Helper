from flask import Flask, render_template
import random
import re
from lxml import etree
import urllib.urlopen
app = Flask(__name__)


def get_text():
    d = {}
    for i in open("word.txt", "r", encoding='utf-8').readlines():
        d[re.findall(r'\..*?<(.*?)\n', i)[0]] = re.findall(r'\.(.*?)<.*?\n', i)[0]
    m = random.sample(d.keys(), 4)
    m.insert(0, d[m[0]].strip(' '))
    return m


def get_zh(w):
    html = etree.parse("http://cn.bing.com/dict/search?q=" + w, etree.HTMLParser())
    print("http://cn.bing.com/dict/search?q=" + w)
    print(urlopen("http://cn.bing.com/dict/search?q=" + w).read())
    d = []
    en = html.xpath('//*[@id="sentenceSeg"]/div/div[2]/div[1]')
    zh = html.xpath('//*[@id="sentenceSeg"]/div/div[2]/div[2]')
    for i in range(len(en)):
        if re.match(r'.*?\. \. \.', en[i].xpath("string(.)")) is None:
            d.append([en[i].xpath("string(.)"), zh[i].xpath("string(.)").encode('ISO-8859-1').decode('utf-8')])
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
