from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
db = SQLAlchemy(app)

# DB Model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    department = db.Column(db.String(50))

# Dummy Admin Credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

# Routes
@app.route('/')
def home():
    if 'user' in session:
        students = Student.query.all()
        return render_template('dashboard.html', students=students)
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == ADMIN_USERNAME and request.form['password'] == ADMIN_PASSWORD:
            session['user'] = ADMIN_USERNAME
            return redirect('/')
        else:
            return render_template('login.html', error="Invalid credentials.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if 'user' not in session:
        return redirect('/login')

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        dept = request.form['department']
        student = Student(name=name, age=age, department=dept)
        db.session.add(student)
        db.session.commit()
        return redirect('/')
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    if 'user' not in session:
        return redirect('/login')

    student = Student.query.get_or_404(id)

    if request.method == 'POST':
        student.name = request.form['name']
        student.age = request.form['age']
        student.department = request.form['department']
        db.session.commit()
        return redirect('/')
    return render_template('edit.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    if 'user' not in session:
        return redirect('/login')

    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
