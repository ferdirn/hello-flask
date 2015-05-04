from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/')
@app.route('/user/<username>/')
def user(username=None):
    context = {'name': username, 'job': 'Hacker'}
    return render_template('hello.html', name=username, job='Programmer')

if __name__ == '__main__':
    app.run()
