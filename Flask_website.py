from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello its my first website with Flask'

@app.route('/<name>/')
def user(name):
    return render_template('nature.html', your_name=name, list=['sea turtles', 'plankton', 'oarfish', 'jellyfish'])

@app.route('/admin/')
def admin():
    return redirect(url_for('user', name='Admin!'))

@app.route('/animals/')
def animals():
    return render_template('nature.html')

if __name__ == '__main__':
    app.run(debug=True)