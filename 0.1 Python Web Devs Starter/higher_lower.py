from flask import Flask
app = Flask(__name__)
import random
@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Guess a number between 0 and 9 </h1>' \
           '<img src="https://media2.giphy.com/media/xUn3CftPBajoflzROU/200w.webp?cid=ecf05e4700pybb9f28km56lsd0783nef0edqjdexfskz9qnq&rid=200w.webp&ct=g">'

random_number = random.randint(0,9)
@app.route('/<int:number>')
def display(number):
    if number == random_number :
        return '<h1 style="text-align:center">You got me! </h1>' \
               '<img src="https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp">'

    if number > random_number:
        return '<h1 style="text-align:center">Too High! </h1>' \
               '<img src="https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp">'

    if number< random_number:
        return '<h1 style="text-align:center">Too low! </h1>' \
               '<img src="https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp">'


if __name__ == '__main__':
    app.run(debug=True,port=8081)