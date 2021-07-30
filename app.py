from flask import Flask, render_template
import get
app = Flask(__name__)


@app.route('/')
def index():
    t = get.get_text()
    return render_template(
        'index.html',
        text=t,
        zhs=get.get_zh(t[0])
    )


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
