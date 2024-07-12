# app.py
from flask import Flask, render_template, redirect, url_for, flash
from forms import LoginForm, SignupForm
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash('Signup successful!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)

@app.route("/")
@app.route('/dashboard')
def dashboard():
    return "<h2>Welcome to the dashboard!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
