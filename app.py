from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    name = 'Rosalia'
    return render_template('/index.html', title='Welcome', username=name)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
