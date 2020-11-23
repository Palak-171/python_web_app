from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy 
import os

app = Flask(__name__)
app.secret_key = "Secret Key"

path = os.path.abspath( os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(path , 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Crud(db.Model):
    sno = db.Column(db.Integer, primary_key = True)
    book_id = db.Column(db.String(100))
    book_name = db.Column(db.String(100))
    book_author = db.Column(db.String(100))
    student_id = db.Column(db.String(100))
    student_name = db.Column(db.String(100))
    issue_date = db.Column(db.String(100))
    return_date = db.Column(db.String(100))
    issuer_name = db.Column(db.String(100))

    def __init__(self, book_id, book_name, book_author, student_id, student_name, issue_date, return_date, issuer_name):
        self.book_id = book_id
        self.book_name = book_name
        self.book_author = book_author
        self.student_id = student_id 
        self.student_name = student_name
        self.issue_date = issue_date
        self.return_date = return_date
        self.issuer_name = issuer_name


@app.route('/')
def index():
    all_data = Crud.query.all()
    return render_template("index.html", all_data = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        book_id = request.form['book_id']
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        student_id = request.form['student_id']
        student_name = request.form['student_name']
        issue_date = request.form['issue_date']
        return_date = request.form['return_date']
        issuer_name = request.form['issuer_name']
       
        my_data = Crud(book_id, book_name, book_author, student_id, student_name, issue_date, return_date, issuer_name)
        db.session.add(my_data)
        db.session.commit()

        flash("Book Issue Data Inserted Successfully")
        return redirect(url_for('index'))

@app.route('/update', methods = ['POST'])
def update():
    if request.method == "POST":
        my_date = Crud.query.get(request.form.get('sno'))
        my_date.book_id = request.form['book_id']
        my_date.book_name = request.form['book_name']
        my_date.book_author = request.form['book_author']
        my_date.student_id = request.form['student_id']
        my_date.student_name = request.form['student_name']
        my_date.issue_date = request.form['issue_date']
        my_date.return_date = request.form['return_date']
        my_date.issuer_name = request.form['issuer_name']
        
        db.session.commit()
        flash("Books Data Updated Successfully")
        return redirect(url_for('index'))

@app.route('/delete/<sno>/')
def delete(sno):
    my_data = Crud.query.get(sno)
    db.session.delete(my_data)
    db.session.commit()

    flash("Books Data Deleted Successfully")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug = True)

