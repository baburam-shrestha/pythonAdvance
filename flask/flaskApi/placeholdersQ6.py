import json
from operator import sub
from flask import Flask, json,jsonify,request
from flask_restful import Api

app = Flask(__name__)
# QN6 Find any external API besides that given in the assignment.
# Retrieve the data from that api with the GET operation, 
# clean the data and load it in your local as "example.json" file. 
# Finally, perform all crud operations on that data.
@app.route("/api/insert/<int:userId>", methods = ['GET','POST','DELETE','PUT'])
def function_crud(userId):
    try:
        #reading
        if(request.method == 'GET'):    
            with open('jsonfiles.json', 'r') as json_file:
                print(json_file)
                json_objects = json.load(json_file)
                json_file.close()
                return jsonify({'data': json_objects})
        #inserting
        if request.method == 'POST':  
            new = request.get_json()  
            with open('jsonfiles.json', 'r') as openfile:
                json_files = json.load(openfile)
                json_files.close()
        
            json_files.append(new)
            with open('jsonfiles.json','w') as file:
                json.dump(json_files,file)
                file.close()

            return({
                'status': 200,
                'message':'Successful'
                })
        
        #deleting
        if request.method=='DELETE':
            with open('jsonfiles.json') as json_files:
                files = json.load(json_files)
                json_files.close()
            for file in files:
                if file['userId']==userId:
                    del files[file]

            with open ('jsonfiles.json','w') as file:
                file.write(json.dumps(files))
                file.close()
            return({
                'status': 200,
                'error':'Successful'
                })
        if request.method=='PUT':
            with open('jsonfiles.json') as json_file:
                files = json.load(json_file)
                json_file.close()
            for file in files:
                if file['userId'] == userId and str(file['completed'])=='true':
                    file['completed'] = 'false'
                    break
            with open ('jsonfiles.json','w') as file:
                file.write(json.dumps(files))
                file.close()

            return jsonify({
                    'status': 200,
                    'message':'Successful'
                    })
                    
    except FileNotFoundError:
        return({
            'status': 404,
            'error':'File not Found'
            })

if __name__ == "__main__":
    app.run(debug=True)