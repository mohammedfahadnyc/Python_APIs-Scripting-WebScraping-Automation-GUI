from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,FloatField, SubmitField
from wtforms.validators import DataRequired
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)
Bootstrap(app)


class Movie(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String)
    year = db.Column(db.String)
    description = db.Column(db.String)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


class MyForm(FlaskForm):
    rating = FloatField(label='Your Rating  out of 10 : ', validators=[DataRequired(message="Need A Rating")])
    review = StringField(label='Write Your Review Here', validators=[DataRequired(message="Need a rating")])
    submit = SubmitField(label="Update")

class AddForm(FlaskForm):
    title = StringField(label='Enter The Movie Name ', validators=[DataRequired(message="Need A Rating")])
    submit = SubmitField(label="Add The Movie")

# db.create_all()

@app.route("/")
def home():
    # movie_list = db.session.query(Movie).all()
    movie_list = Movie.query.order_by(Movie.rating).all()
    for i in range(len(movie_list)) :
        movie_list[i].ranking = len(movie_list)-i
    db.session.commit()
    return render_template("index.html",list=movie_list)


@app.route("/edit",methods=["GET","POST"])
def edit():
    form = MyForm()
    id = request.args.get('movie_id')
    movie = Movie.query.get(id)
    if form.validate_on_submit() :
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return home()
    return render_template("edit.html",form=form,movie=movie)

@app.route("/delete")
def delete():
    id = request.args.get('movie_id')
    movie = Movie.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return home()

@app.route("/add",methods=["GET","POST"])
def add():
    form = AddForm()
    if request.method == "POST" :
        movie_name = form.title.data
        print(movie_name)
        api_endpoint = "https://api.themoviedb.org/3/search/movie"
        parameters = {
            'api_key' : "146894407afc7a1954e4b28ec42ad4be",
            'query' : f"{movie_name}"
        }
        data = requests.get(url=api_endpoint,params=parameters).json()
        movies = data['results']
        return render_template("select.html",movies=movies)

    return render_template("add.html", form=form)


@app.route("/add_to_db")
def add_to_db():
    movie_api_id = request.args.get('movie_id')
    url = f"https://api.themoviedb.org/3/movie/{movie_api_id}?api_key=146894407afc7a1954e4b28ec42ad4be&language=en-US"
    data = requests.get(url=url).json()
    image_path = data['poster_path']
    movie = Movie()
    movie.title = data['original_title']
    movie.year = data["release_date"]
    movie.description = data["overview"]
    # rating = db.Column(db.Float)
    # review = db.Column(db.String)
    movie.img_url = f"https://image.tmdb.org/t/p/w500/{image_path}"
    db.session.add(movie)
    db.session.commit()
    movie_id = Movie.query.filter_by(title=f"{data['original_title']}").first().id
    return redirect(url_for('edit',movie_id=movie_id))



if __name__ == '__main__':
    app.run(debug=True,port=8081)








# API Call References
# import requests
# api_endpoint = "https://api.themoviedb.org/3/search/movie"
# parameters = {
#     'api_key' : "146894407afc7a1954e4b28ec42ad4be",
#     'query' : "matrix"
# }
#
# data = requests.get(url=api_endpoint,params=parameters).json()
# movies = data['results']
# for movie in movies :
#     print(movie['id'])
#     print(movie['title'])
#     print(movie['release_date'])
#
#
# movie_id = int(movies[0]['id'])
# url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=146894407afc7a1954e4b28ec42ad4be&language=en-US"
# data = requests.get(url=url).json()
# print(data)
# image_path = data['poster_path']
# image_url = f"https://image.tmdb.org/t/p/w500/{image_path}"
# title = data['original_title']
# description = data["overview"]
# year = data["release_date"]
#
# print(image_url,title,description,year)