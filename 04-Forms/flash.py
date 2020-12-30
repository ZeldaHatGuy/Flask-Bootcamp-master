from flask import Flask, render_template, flash, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)


app.config['SECRET_KEY'] = 'mykey'



class SimpleForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    submit = SubmitField('Click Me.')

@app.route('/', methods = ['GET', 'POST'])
def index3():
    form = SimpleForm()
    session['breed'] = form.breed.data


    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash('You just have selected {}.'.format(session['breed']))

        return redirect(url_for('index3'))

    return render_template('index3.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

