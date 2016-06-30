from flask import Flask, render_template, request
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from datetime import datetime

from wtforms import StringField, SubmitField
from wtforms.validators import Required

app = Flask(__name__)
app.config['SECRET_KEY']='s3cr3tk3y'
bootstrap = Bootstrap(app)
moment = Moment(app)

#Forms
class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    user_agent= request.headers.get('User-Agent')
    name=None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data;
        form.name.data = ''
    return render_template('index.html',
        ua=user_agent,
        current_time=datetime.utcnow(),
        name=name,
        form= form
    )
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

# error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
if __name__ == '__main__':
    app.run(debug=True)
