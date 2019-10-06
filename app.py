from flask import Flask, render_template, request
from urllib.parse import urlparse
import json
import automation
import threading

automate = automation.Automate()
app = Flask(__name__, static_url_path = '', static_folder = 'static')
def search_database(input_number, output_number):
    check = 0
    pav_list = []# defines the URL output list
    des_list = []# defines the discription output list
    dom_list = []# defines the domains of URL list# opens the json file under working name 'resources'
    with open('data/resources.json', 'r') as resources:
        data = json.loads(resources.read())# dumps the JSON data into a list
        for item in data: #iterates over each entry of list 'data'
            try:
                if "url" in item.keys(): # check if there is a url key in the json object
                        if input_number in item.get("input") and output_number in item.get("output"): # check if the input and the output is handled by the website
                            pav = item.get("url") # get the url url of the website 
                            pav_list.append(pav)# adds the URL to the output list
                            dom = urlparse(pav).netloc.replace("www.", "").split(".")[0].capitalize() # format the domain name
                            dom_list.append(dom) # adds formatted domain to the domain list
                            des = item.get("purpose") # get purpose of the website
                            des_list.append(des)  # adds purpose to the description list
            except:
                None
    out_list = automate.execute(dom_list) # List of Automation Results
    if not pav_list:
        check = 1
    return pav_list, des_list, dom_list, out_list #return every lists that will be displayed on the website

querry_type = {
  'Email': 1,
  'Home address': 2,
  'Online alias': 3,
  'general information': 4,
  'verification': 5,
  'IP adress': 6,
  'domain name': 7,
  'Name': 8,
  'Phone number': 9,
  'Classification': 10,
  'Malware check': 11,
  'Threat detection': 12,
  'Redirection': 13,
  'History': 14,
  'Trend': 15,
  'Term': 16,
  'Dark web': 17,
  'Black list': 18,
  'Web crawling': 19,
  'Image': 20,
  'Location': 21,
  'Video': 22
}

# print(automate.execute(["hello"]))

@app.route('/', methods = ['POST'])
def my_form_post():
    output_text = request.form['output'] # get the output type
    input_text = request.form['input'] # get the input type
    if output_text not in querry_type.keys() or input_text not in querry_type.keys(): # check if both input and output are valid
        output = "Invalid Arguments"
        return render_template("index.jinja", types = querry_type.keys(), output = output, search_output = '')
    output_list = []
    output_number = querry_type[output_text] # get the ID of the output
    input_number = querry_type[input_text] # get the ID of the input
    link_list, desc_list, domain_list, out_list = search_database(input_number, output_number) # idea; loop over all the resources and look for anything with matching input and output tag.#use for debugging, remove later
    if not out_list:
        output_empty_check = "No links found."
    else:
        output_empty_check = ""
    return render_template("index.jinja", types = querry_type.keys(), domain_list = domain_list, link_list = link_list, desc_list = desc_list, out_list = out_list, output_empty_check=output_empty_check)

@app.route("/", methods = ['GET'])
def root():
    output = request.args.get("input")
    return render_template("index.jinja", types = querry_type.keys(), output = output)

app.run(debug = True)