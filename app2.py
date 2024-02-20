from flask import Flask

app = Flask(__name__)

@app.route('/profile/<username>')
def profile(username):
    return '<h1>This is a profile page for %s</h1>' % username

@app.route('/profileInt/<int:id>')
def profileInt(id):
    return '<h1>This is a profile page for %d</h1>' % id

if __name__ == '__main__':
    app.run(debug=True)