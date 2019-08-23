from flask import Flask, render_template, request
import json

app = Flask(__name__,static_url_path='', static_folder='static')

with open('data/resources.json', 'r') as resources:
    data = json.load(resources)
    #add json input

@app.route('/', methods=['POST'])
def my_form_post():
    output_text = request.form['output']
    input_text = request.form['input']
    if output_text == 'Adress':
        output_number=1
        print(1)
    elif output_text == 'Phone Number':
        output_number=2
        print(2)
    if input_text == 'Name':
        input_number=8
        print(8)
    elif input_text == 'Email':
        input_number = 1
        print(1)

    # idea; loop over all the resources and look for anything with matching input and output tag.
    server_output="{} -> {}".format(input_text,output_text) #use for debugging, remove later
    return render_template("index.html", output=server_output)

@app.route("/", methods=['GET'])
def root():
    output = request.args.get("input")
    return render_template("index.html", output=output)

app.run(debug=True)
