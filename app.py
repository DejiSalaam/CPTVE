from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(100), nullable=False)
    user_password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.user_email}'

# comment

@app.route('/home')
def landing():
    return render_template("index.html")

@app.route('/')
def home():
    return render_template("landing.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        email= request.form['email']
        password = request.form['password']
        new_user = User(user_email=email, user_password=password)
        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect("/users")
        except:
            return 'There was an issue signing up'
    else:
        return render_template('signup.html')


@app.route('/users')
def users():
    users = User.query.all()
    print(len(users))
    return render_template('users.html', users=users)

if __name__ == "__main__":
    app.run(debug=True)




