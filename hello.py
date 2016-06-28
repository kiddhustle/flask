from flask import Flask, render_template, request
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route('/')
def index():
    user_agent= request.headers.get('User-Agent')
    return render_template('index.html',ua=user_agent)
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
if __name__ == '__main__':
    app.run(debug=True)
