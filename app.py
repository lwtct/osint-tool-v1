from flask import Flask, render_template, request

app = Flask(__name__,static_url_path='', static_folder='static')

file = open('data/resources.json', 'r')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['output']
    return render_template("index.html", output=text)

@app.route("/")
def root():
    output = request.args.get("input")
    return render_template("index.html", output=output)

app.run(debug=True)
