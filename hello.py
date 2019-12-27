from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello heroku for the first test!"

if __name__ == "__main__":
	app.run()

