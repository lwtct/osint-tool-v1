from flask import Flask, render_template, request

app = Flask(__name__,static_url_path='', static_folder='static')


@app.route("/")
def root():
    return render_template("index.html")


app.run(debug=True)