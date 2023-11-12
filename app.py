from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import csv
from io import StringIO

app = Flask(__name__)
app.secret_key = 'babamoni'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    referral_code = db.Column(db.String(10), nullable=False, unique=True)

admin_username = 'admin'
admin_password = 'admin@123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone_number = request.form.get('phone_number')

    referral_code = name[:3].upper() + phone_number[-3:]

    new_user = User(name=name, phone_number=phone_number, referral_code=referral_code)
    db.session.add(new_user)
    db.session.commit()

    return render_template('success.html', referral_code=referral_code)

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == admin_username and password == admin_password:
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            return render_template('admin_login.html', error='Invalid credentials')
    return render_template('admin_login.html', error=None)

@app.route('/admin_home')
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    with app.app_context():
        users = User.query.all()

    return render_template('admin.html', users=users)

@app.route('/download_csv')
def download_csv():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    with app.app_context():
        users = User.query.all()

        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)
        csv_writer.writerow(['Name', 'Phone Number', 'Referral Code'])

        for user in users:
            csv_writer.writerow([user.name, user.phone_number, user.referral_code])

        csv_data.seek(0)
        return csv_data.getvalue(), 200, {'Content-Type': 'text/csv', 'Content-Disposition': 'attachment; filename=users.csv'}

@app.route('/search', methods=['POST'])
def search():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    referral_code = request.form.get('referral_code')

    with app.app_context():
        result = User.query.filter_by(referral_code=referral_code).all()

    return render_template('search.html', result=result)
@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
	with app.app_context():
		db.create_all()
		app.run(debug=True)

