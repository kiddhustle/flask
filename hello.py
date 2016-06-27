from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent= request.headers.get('User-Agent')
    output = '''<h1>Hello!</h1>
    <p>USer agent is: {ua}</p>
    '''.format(ua=user_agent)
    return output
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
if __name__ == '__main__':
    app.run(debug=True)
