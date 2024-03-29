from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, RadioField, TextField, validators
import covidinfo

global state
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


class LoginForm(FlaskForm):
    age = StringField('age')
    state = StringField('state')


class testing(FlaskForm):
    q11 = TextField('Playing videogames/watching TV', validators=[validators.DataRequired()])
    q12 = TextField('Hiking/Biking', validators=[validators.DataRequired()])

    @app.route('/quiz', methods=['GET', 'POST'])
    def quiz():
        global state
        form = testing(request.form)

        print(form.errors)
        if request.method == 'POST':
            print(request.form)
            q11 = request.form['Playing videogames/watching TV']
            print("", q11)
        return render_template("quiz.html")





@app.route("/")
def home():
    return render_template("index.html")


@app.route("/openForm/", methods=['GET', 'POST'])
# that wont help
def openForm():
    print("opened form thing")
    return redirect(url_for('form'))

# @app.route("/quiz")
# def home():
#    return render_template("quiz.html")
#gimme a sec


@app.route('/form', methods=['GET', 'POST'])
def form():
    global state
    form = LoginForm()
    #if form.validate_on_submit():
    if True:
        try:
            age = form.age.data
            state = form.state.data
            print(age)
            print(state)
            return redirect(url_for('data'))
        except:
            pass
    print('sjafhjakfkj')
    return render_template('form.html', form=form)

@app.route('/data')
def data():
    print('bboosfjkfa')
    a = covidinfo.getStatePopulation(state)
    b = covidinfo.getCovid(state)
    c = b/a
    print(c * 100)
    return render_template('data.html')


if __name__ == '__main__':
    app.run(debug=True)