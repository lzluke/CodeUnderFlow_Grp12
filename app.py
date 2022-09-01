from flask import Flask, render_template, url_for, redirect, session
from forms import LoginForm
import methods

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'


def sessionCheck():
    if 'user' in session:
        return True
    return False


@app.route('/login', methods=['GET', 'POST'])
def login():
    loggedin = sessionCheck()
    form = LoginForm()
    if form.validate_on_submit():
        db = methods.getShelve()
        user = False
        for obj in db.values():
            # print(obj)
            if obj.getUsername() == form.username.data:
                user = obj.getId()
        if user:
            if db[user].getPw() == form.password.data:
                session['user'] = user
                return redirect(url_for('home'))
    return render_template('login.html', form=form, loggedin=loggedin)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/')
def home():
    if not sessionCheck():
        return redirect(url_for('login'))
    return render_template('Insights.html')


@app.route('/expenses', methods=['GET', 'POST'])
def expenses():
    if not sessionCheck():
        return redirect(url_for('login'))
    return render_template('Expenses.html')


@app.route('/floorPlan', methods=['GET', 'POST'])
def floorPlan():
    if not sessionCheck():
        return redirect(url_for('login'))
    return render_template('FloorPlan.html')


@app.route('/targets', methods=['GET', 'POST'])
def targets():
    if not sessionCheck():
        return redirect(url_for('login'))
    return render_template('Targets.html')


@app.route('/about', methods=['GET', 'POST'])
def about():
    loggedin = sessionCheck()
    return render_template('About.html', loggedin=loggedin)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    loggedin = sessionCheck()
    return render_template('Contact.html', loggedin=loggedin)


if __name__ == "__main__":
    app.run(debug=True)
