from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello There!</h1>'

@app.route('/home/<place>')
def home(place):
    return '<h1>You are on the ' + place + 'page!</h1>'

if __name__ == "__main__" :
    app.run(debug=True)