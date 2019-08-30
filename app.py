from flask import Flask, render_template, request
from urllib.parse import urlparse
import json

app = Flask(__name__,static_url_path='', static_folder='static')


def search_database(input_number, output_number):
    pav_list = []  # defines the URL output list
    des_list = []  # defines the discription output list
    dom_list = []  # defines the domains of URL list
    with open('data/resources.json', 'r') as resources:  # opens the json file under working name 'resources'
        data = json.loads(resources.read())  # dumps the JSON data into a list
        data_counter = 0  # resets the variable
        for line in data:  # iterates over each entry of list 'data'
            try:
                if 'url' in str(data[data_counter]):  # checks if the entry is a valid resource entry
                    work = str(data[data_counter])  # creating a string of the active list entry
                    work = work.split("', ")  # creating a list of the string 'work'
                    work_counter = 0  # reset variables
                    list_item_check_input = 0
                    list_item_check_output = 0
                    list_item_check_purpose = 0
                    list_item_check_url = 0
                    for list_item in work:  # iterate over each entry of the list 'work'
                        if 'input' in str(work[work_counter]):   # check if the current entry in list 'work' contains the input classification
                            work_input = str(work[work_counter])  # save the location of the input classification for later use
                            list_item_check_input = 1
                        if 'output' in str(work[work_counter]):  # does what was done for input previously for output
                            work_output = str(work[work_counter])
                            list_item_check_output = 1
                        if 'purpose' in str(work[work_counter]):
                            purpose = str(work[work_counter])
                            list_item_check_purpose = 1
                        if 'url' in str(work[work_counter]):
                            url = str(work[work_counter])
                            list_item_check_url = 1
                        if list_item_check_output == 1 & list_item_check_input == 1 & list_item_check_purpose == 1 & list_item_check_url == 1:  # if all the location are found there is no reason to continue checking
                            pass
                        work_counter += 1  # updates the current entry of list work
                    if str(input_number) in work_input and str(output_number) in work_output:  # check if the active entry has the necessary input and output classification
                        pav = url  # variable name from Pyro57#6998. Feel free to annoy him on discord even though he did next to nothing with the development of this application.
                        pav = pav.replace("{'url': '", "")  # removes the unnecessary part and just leaves the URL
                        pav_list.append(pav)  # adds the URL to the output list
                        dom_list.append(urlparse(pav).netloc.replace("www.","").split(".")[0].capitalize())
                        des = purpose
                        des = des.replace("'purpose': '", "").capitalize()  # removes unnecessary part and just leaves the description
                        des_list.append(des)  # adds the description to the output list
                    else:
                        pass
                else:
                    pass
            except Exception:  # deals with the errors
                pass
            data_counter += 1  # moves on to next entry in list 'data'
    return pav_list, des_list, dom_list # when completed this returns a list of all URLs and description with the correct classification

querry_type = {
    'Email' : 1,
    'Home address' : 2,
    'Online alias' : 3,
    'general information' : 4,
    'verification' : 5,
    'IP adress' : 6,
    'domain name' : 7,
    'Name' : 8,
    'Phone number' : 9
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
    link_list, desc_list, domain_list = search_database(input_number, output_number)
    # idea; loop over all the resources and look for anything with matching input and output tag.
    server_output="{} -> {}".format(input_text,output_text) #use for debugging, remove later
    return render_template("index.jinja", types=querry_type.keys(), output=server_output, domain_list=domain_list, link_list=link_list, desc_list=desc_list)

@app.route("/", methods=['GET'])
def root():
    output = request.args.get("input")
    return render_template("index.jinja", types=querry_type.keys(), output=output)

app.run(debug=True)