from flask import Flask, render_template

app = Flask(__name__)

@app.route('/welcome/<username>')
def hello(username):
    return render_template('hello.html', name=username)

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name
    

if __name__ == '__main__':
    app.run()