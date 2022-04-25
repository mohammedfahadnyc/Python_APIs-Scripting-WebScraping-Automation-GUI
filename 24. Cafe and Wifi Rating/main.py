from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,SelectField,URLField
from wtforms.validators import DataRequired,URL
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = URLField('Cafe Location On Google Map', validators=[URL(require_tld=True, message="Not A Valid URL")])
    opening = StringField('Opening Time', validators=[DataRequired()])
    closing = StringField('Closing Time', validators=[DataRequired()])
    coffe_rating = SelectField('Coffee Rating', choices=['☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕'],validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength', choices=['💪', '💪💪', '💪💪💪', '💪💪💪💪', '💪💪💪💪💪'], validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'],validators=[DataRequired()])
    submit = SubmitField('Submit')




# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv',mode='a') as file:
            file.write('\n')
            for key in form.data :
                if key=='csrf_token' or key=="submit":
                    continue
                file.write(f"{form.data[key]},")
        return cafes()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True,port=8081)
