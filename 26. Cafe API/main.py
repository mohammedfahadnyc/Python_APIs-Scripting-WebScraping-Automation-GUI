import random
import jsons
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=True)
    img_url = db.Column(db.String(500), nullable=True)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=True)
    has_toilet = db.Column(db.Boolean, nullable=True)
    has_wifi = db.Column(db.Boolean, nullable=True)
    has_sockets = db.Column(db.Boolean, nullable=True)
    can_take_calls = db.Column(db.Boolean, nullable=True)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


    

## HTTP GET - Read Record

# Get - A random Cafe
@app.route("/random")
def get_random_cafe():
    table= db.session.query(Cafe).all()
    cafe = random.choice(table)
    cafe = vars(cafe)               #turning object into a dictionary
    del cafe['_sa_instance_state']  #removing this from the dictionary
    # return   jsonify(id = cafe.id,
    #                name=cafe.name,
    #                map = cafe.map_url,
    #                image = cafe.img_url,
    #                location=cafe.location,
    #                has_seats = cafe.seats,
    #                has_toilet = cafe.has_toilet,
    #                has_wifi = cafe.has_wifi,
    #                has_sockets = cafe.has_sockets,
    #                can_take_calls = cafe.can_take_calls,
    #                coffe_price = cafe.coffee_price)
    return   jsonify(cafe = cafe)

#Get - All Cafe in the Database

@app.route("/all")
def get_all_cafes():
    table_list = db.session.query(Cafe).all()            #list of all table objects
    cafe_list = [vars(table) for table in table_list]        #converting each object in to dictionary and putting in a list
    for cafe in cafe_list :
        del cafe['_sa_instance_state']      #removing this key from each dict in the list

    return jsonify(cafe=cafe_list)


#Get - Find A Cafe :  use https://...../search?loc=<value> to pass *args parameter
@app.route("/search")
def search():
    location = request.args.get("loc")
    cafe = Cafe.query.filter_by(location=location).all()
    if len(cafe) > 0 :
        cafe_list = [vars(table) for table in cafe]  # converting each object in to dictionary and putting in a list
        for cafe in cafe_list:
            del cafe['_sa_instance_state']  # removing this key from each dict in the list

        return jsonify(cafe=cafe_list)
    else :
        return jsonify (cafe = "Cafe Doesnt Exist ")

## HTTP POST - Create Record
@app.route("/add",methods=["GET","POST"])   #using the postman,we are sending parameters in the url
def add():
    if request.method == "POST" :
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("loc"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify (response="Successfully Added")

## HTTP PUT/PATCH - Update Record

# update Price
@app.route("/update-price/<int:cafe_id>",methods=["PATCH"])   #using the postman,we are sending parameters in the url
def update(cafe_id):
    if request.method == "PATCH":
        cafe = Cafe.query.filter_by(id=cafe_id).first()
        if cafe :
            new_price = request.args.get('new_price')
            cafe.coffee_price = new_price
            db.session.commit()
            return jsonify(message="Suucessfully Updated"),202
        else :
            return jsonify(message="No Cafe found with this id"),404

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>",methods=["DELETE"])   #using the postman,we are sending parameters in the url
def delete(cafe_id):
    if request.method == "DELETE":
        cafe = Cafe.query.filter_by(id=cafe_id).first()
        our_secret_key = "jhksfkj2saf@fd"
        secret_key = request.args.get("API_KEY")
        if cafe and our_secret_key==secret_key :
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(message="Successfully Deleted")
        elif not cafe :
            return jsonify(message="Cafe Not Found")
        elif our_secret_key != secret_key :
            return jsonify(message="Not Authenticated")




if __name__ == '__main__':
    app.run(debug=True,port=8081)

