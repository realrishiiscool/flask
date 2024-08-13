from flask import Flask,url_for,redirect,render_template

app = Flask(__name__)
#this  is one lie edioted
@app.route('/')
def index():
	return render_template('index.html')


if __name__ == "__main__":
	app.run()
