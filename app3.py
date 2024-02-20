from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/admin')
def welcome_admin():
    return 'Welcome admin'

@app.route('/guest/<guest>')
def welcome_guest(guest):
    return 'Welcome guest %s' % guest

@app.route('/user/<name>')
def welcome_user(name): 
    if name == 'admin':
        return redirect(url_for('welcome_admin'))
    else:
        return redirect(url_for('welcome_guest', guest=name))

if __name__ == '__main__':
    app.run(debug=True)