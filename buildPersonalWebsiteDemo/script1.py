from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # a '/' means home page
def home():
    return render_template("home.html")

@app.route('/test/')
def test():
    return 'different page!'

if __name__ == "__main__":
    app.run(debug=True)