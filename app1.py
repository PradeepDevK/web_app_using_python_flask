from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>This is an index page.</h1>'

@app.route('/new')
def new():
    return '<h1>This is a new page</h1>'

@app.route('/demo')
def demo():
    return '<h1>This is a demo page</h1>'

if __name__ == '__main__':
    app.run()