from flask import Flask, render_template, request
import json

app = Flask(__name__,static_url_path='', static_folder='static')


def search_database(input_number, output_number):
    pav_list = [] #defines the output list
    with open('data/resources.json', 'r') as resources: #opens resources.json file under working name 'resources'
        data = json.loads(resources.read()) #dumps the JSON data into a list
        data_counter = 0 #resets the variable
        for line in data: #iterates over each entry of list 'data'
            try:
                if 'url' in str(data[data_counter]): #checks if the entry is a valid resource entry
                    input_confirm = 0 #reset variables
                    output_confirm = 0
                    work = str(data[data_counter])  #creating a string of the active list entry
                    work = work.split("', ")  #creating a list of the string 'work'
                    work_counter = 0 #reset variables
                    list_item_check_input = 0
                    list_item_check_output = 0
                    for list_item in work:  #iterate over each entry of the list 'work'
                        if 'input' in str(work[work_counter]):  #check if the current entry in list 'work' contains the input classification
                            work_input = str(work[work_counter]) #save the location of the input classification for later use
                            list_item_check_input = 1
                        if 'output' in str(work[work_counter]): #does what was done for input previously for output
                            work_output = str(work[work_counter])
                            list_item_check_output = 1
                        if list_item_check_output == 1 & list_item_check_input == 1: #if both the input and output location are found there is no reason to continue checking
                            pass
                        work_counter += 1 #updates the current entry of list work
                    if str(input_number) in work_input and str(output_number) in work_output: #check if the active entry has the necessary input and output classification
                        pav = str(work[0])  #variable name from Pyro57#6998. Feel free to annoy him on discord even though he did next to nothing with the development of this application.
                        pav = pav.replace("{'url': '", "") #removes the unnecessary part and just leaves the URL
                        pav_list.append(pav) #adds the URL to the string
                    else:
                        pass
                else:
                    pass
            except Exception:     #deals with the errors
                pass
            data_counter += 1 #moves on to next entry in list 'data'
    return pav_list #when completed this returns a list of all URLs with the correct classification

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
        return render_template("index.jinja", types=querry_type.keys(), output=output, search_output='')


    output_number = querry_type[output_text]
    input_number = querry_type[input_text]
    print(input_number, output_number)
    search_output = search_database(input_number, output_number)
    print(search_output)
    # idea; loop over all the resources and look for anything with matching input and output tag.
    server_output="{} -> {}".format(input_text,output_text) #use for debugging, remove later
    return render_template("index.jinja", types=querry_type.keys(), output=server_output, search_output=search_output)

@app.route("/", methods=['GET'])
def root():
    output = request.args.get("input")
    return render_template("index.jinja", types=querry_type.keys(), output=output)

app.run(debug=True)
