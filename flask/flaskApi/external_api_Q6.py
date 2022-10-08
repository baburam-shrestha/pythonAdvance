import json
from flask import Flask, jsonify, request

app = Flask(__name__)
# QN6 Find any external API besides that given in the assignment.
# Retrieve the data from that api with the GET operation, 
# clean the data and load it in your local as "example.json" file. 
# Finally, perform all crud operations on that data.


#Read JSON data
@app.route('/api/', methods = ['GET','POST','DELETE','PUT'])
def read():
    try:
        with open('examples.json', 'r') as json_file:
            json_objects = json.load(json_file)
            json_file.close()

        if request.method == 'GET':
            return jsonify({
                'Data':json_objects,
                })
        else:
            return jsonify({
                'status':404,
                'message':'Wrong Method',
                })
    except FileNotFoundError:
        return({
            'Status': 404,
            'message':'File Not  Found',
        })


#Get data passing name parameter
@app.route('/api/name/<string:name>',methods = ['GET','POST','DELETE','PUT'])
def get_by_name(name):
    try:
        with open('examples.json', 'r') as json_file:
            json_objects = json.load(json_file)
            json_file.close()

        if request.method == 'GET':   
            for json_object in json_objects:
                if json_object['name'] == name:
                    result = jsonify({'status':"Success",
                    "name":json_object['name'],
                    "country_code":json_object['alpha_two_code'],
                    "website":json_object['web_pages'],
                    'country':json_object['country']
                    })
                    break

            return jsonify({
                'data':result
                })
        else:
            return jsonify({
                'status':404,
                'message':'Wrong Method',
                })

    except FileNotFoundError:
        return({
            'Status': 404,
            'message':'File Not  Found',
        })

#insert
@app.route('/api/insert',methods = ['GET','POST','DELETE','PUT'])
def insert():
    try:
        with open('examples.json', 'r') as json_file:
            json_objects = json.load(json_file)
            json_file.close()
        new_data={
            "domains": ["afu.edu.np"],
            "alpha_two_code": "NP",
            "country": "Nepal",
            "web_pages": [
            "http://www.afu.edu.np/"],
            "name": "Agriculture and Forestry University",
            "state-province": 'null',
            }

        if request.method == 'POST':
            json_objects.append(new_data)
            with open('example.json','w') as file:
                json.dump(json_objects,file)
            return jsonify({
                'status':200,
                'amessage': 'Successfull',
                'Data':new_data,
            })   

    except FileNotFoundError:
        return({
            'Status': 404,
            'message':'File Not  Found',
        })

@app.route('/api/update/<string:name>',methods = ['GET','POST','DELETE','PUT'])
def update(name):
    try:
        with open('exmaples.json', 'r') as json_file:
            json_objects = json.load(json_file)
            json_file.close()

        if request.method == 'PUT':
            for json_object in json_objects:
                if json_object['name'] == name:
                    json_object['name']="Updated"    

            with open ('jsonfiles.json','w') as file:
                file.write(json.dumps(json_objects))
                file.close()
            return jsonify({
                'status':200,
                'message':'Successfull',
                'name':name,
                })
        else:
            return jsonify({
                'status':404,
                'message':'Wrong Method',
                })

    except FileNotFoundError:
        return({
            'Status': 404,
            'message':'File Not  Found',
        })


if __name__ == "__main__":
    app.run(debug=True)
