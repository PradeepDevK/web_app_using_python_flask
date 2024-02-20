from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(
    os.path.join(project_dir, "mydatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

class Book(db.Model):
    name = db.Column(db.String(100),unique=True,nullable=False,primary_key=True)
    author = db.Column(db.String(100),nullable=False)

# # Ensure to create database tables within the application context
# with app.app_context():
#     # Create all database tables
#     db.create_all()
    
@app.route('/updatebooks')
def updatebooks():
    books = Book.query.all()
    return render_template('updatebooks.html', books=books)

@app.route('/addbook')
def addBook():
    return render_template('addbook.html')

@app.route('/')
def index():
    # return 'This is the request made by the client %s ' % request.headers
    return render_template('index.html')

@app.route('/profile/<username>')
def profile(username):
    isActive = True
    return render_template('profile.html', username=username, isActive=isActive)

@app.route('/books')
def books():
    # books = ['Book1', 'Book2', 'Book3']
    # books = [{'name':'Book1','author':'Author 1','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'},
    #          {'name':'Book2','author':'Author 2','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'},
    #          {'name':'Book3','author':'Author 3','cover':'https://www.mswordcoverpages.com/wp-content/uploads/2018/10/Book-cover-page-3-CRC.png'}]
    # return render_template('books.html',books=books)
    books = Book.query.all()
    return render_template('books.html',books=books)

@app.route('/submitbook',methods=['POST'])
def submitbook():
    name = request.form['name']
    author = request.form['author']
    book = Book(name=name,author=author)
    db.session.add(book)
    db.session.commit()
    # return "Data submitted successfully! Book name is %s and author is %s" % (name,author)
    return redirect('/books')

@app.route('/update',methods=['POST'])
def update():
    oldname = request.form['oldname']
    newname = request.form['name']
    author = request.form['author']
    
    book = Book.query.filter_by(name=oldname).first()
    book.name = newname
    book.author = author
    db.session.commit()
    return redirect("/books")

@app.route('/delete',methods=['POST'])
def delete():
    name = request.form['name']
    book = Book.query.filter_by(name=name).first()

    db.session.delete(book)
    db.session.commit()
    return redirect("/books")


if __name__ == '__main__':
    app.run(debug=True)