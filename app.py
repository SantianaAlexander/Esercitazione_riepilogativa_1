from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from models import Utenti

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///utenti.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app) 
login_manager.login_view = 'login'

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request-methhod == 'POST':
        username = request.form['username']
        hashed_password = request.form['password']
        pw_hash = bcrypt.generate_password_hash(hashed_password, 10)
        if Utenti.query.filter_by(username = username).fisrt():
            return render_template('register.html', error="Questo username è già in uso. Ritenta!")
        new_user = User(username=username, hashed_password=pw_hash)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', error=None)
if __name__ == '__main__':
    app.run(debug=True)