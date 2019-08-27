from flask import Flask, render_template, request
import json

app = Flask(__name__,static_url_path='', static_folder='static')

def search_database(input_number, output_number):
    with open('resources.json', 'r') as resources:
        data = json.loads(resources.read())
        data_counter = 0
        for line in data:
            try:
                if 'url' in str(data[data_counter]):
                    work = str(data[data_counter])
                    work = work.split("', ")
                    print(work[4],"|", work[5])
                    if str(input_number) in str(work[4]):
                        input_confirm = 1
                    if str(output_number) in str(work[5]):
                        output_confirm = 1
                    if input_confirm == 1 & output_confirm == 1:
                        return work[0]
                    else:
                        return 'null'
                else:
                    pass
            except Exception:
                pass
            data_counter += 1

querry_type = {
    'Address' : 1,
    'Phone Number' : 2,
    'online alias' : 3,
    'general information' : 4,
    'verification' : 5,
    'IP adress' : 6,
    'Name' : 8
}

@app.route('/', methods=['POST'])
def my_form_post():
    output_text = request.form['output']
    input_text = request.form['input']
    if output_text not in querry_type.keys() or input_text not in querry_type.keys():
        output = "Invalid Arguments"
        return render_template("index.jinja", types=querry_type.keys(), output=output)


    output_number = querry_type[output_text]
    input_number = querry_type[input_text]
    print(input_number, output_number)

    # idea; loop over all the resources and look for anything with matching input and output tag.
    server_output="{} -> {}".format(input_text,output_text) #use for debugging, remove later
    return render_template("index.jinja", types=querry_type.keys(), output=server_output)

@app.route("/", methods=['GET'])
def root():
    output = request.args.get("input")
    return render_template("index.jinja", types=querry_type.keys(), output=output)

app.run(debug=True)
