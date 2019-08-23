from flask import Flask, render_template, request
import json

app = Flask(__name__,static_url_path='', static_folder='static')

querry_type = {
    'Address' : 1,
    'Phone Number' : 2,
    'Name' : 8
}

with open('data/resources.json', 'r') as resources:
    data = json.load(resources)
    #add json input


querry_type = {
    'Address' : 1,
    'Phone Number' : 2,
    'Name' : 8
}

@app.route('/', methods=['POST'])
def my_form_post():
    output_text = request.form['output']
    input_text = request.form['input']
    if output_text not in querry_type.keys() or input_text not in querry_type.keys():
        output = "Invalid Arguments"
        return render_template("index.html", types=querry_type.keys(), output=output)

    ab115c34017f5fd862bb144cd6b36fd7f830bd29

    output_number = querry_type[output_text]
    input_number = querry_type[input_text]

    print(input_number, output_number)

    # idea; loop over all the resources and look for anything with matching input and output tag.
    server_output="{} -> {}".format(input_text,output_text) #use for debugging, remove later
    return render_template("index.html", types=querry_type.keys(), output=server_output)

@app.route("/", methods=['GET'])
def root():
    output = request.args.get("input")
    return render_template("index.html", types=querry_type.keys(), output=output)

app.run(debug=True)
