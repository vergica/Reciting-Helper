from flask import Flask, render_template
import pck.getinfo
app = Flask(__name__)


@app.route('/')
def index():
    t = get.get_text()
    return render_template(
        'index.html',
        text=t,
        zhs=getinfo.get_zh(t[0])
    )


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
