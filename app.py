from flask import Flask, render_template, request

app = Flask(__name__,static_url_path='', static_folder='static')

#HI THERE THIS IS A MERGE TEST

@app.route("/")
def root():
    output = request.args.get("input")
    return render_template("index.html", output=output)


app.run(debug=True)
