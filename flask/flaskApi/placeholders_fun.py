import json
from operator import sub
from flask import Flask, json,jsonify,request
from flask_restful import Api

app = Flask(__name__)

@app.route("/api/", methods = ['GET','POST','DELETE','PUT'])
def function_json():
    try:
        if(request.method == 'GET'):    
            with open('jsonfiles.json', 'r') as json_file:
                print(json_file)
                json_objects = json.load(json_file)
                json_file.close()
                return jsonify({'data': json_objects})

    except FileNotFoundError:
        return({
            'status': 404,
            'error':'File Not Found'
        })


# QN1 Create an API to display title in reversed order for the given user id.
# ( If record is not available then display appropriate response( Exception Handling) )
@app.route("/api/reversed/<int:userId>", methods = ['GET','POST'])
def function_reversed(userId):
    try:
        with open('jsonfiles.json') as json_file:
            users = json.load(json_file)
            json_file.close()
            for user in users:
                if user['userId'] == userId:
                    return jsonify({
                        'userId': user['userId'],
                        'id': user['id'],
                        'title': user['title'],
                        'revered_title': user['title'][::-1],
                        'completed': user['completed']
                        })
            else:
                return jsonify({
                    'status': 404,
                    'id': userId,
                    'message': 'No record found',
                    })
    except FileNotFoundError:
        return({
            'status': 404,
            'error':'File Not Found'
            })

# QN2 Create an api where the field ”title” with field “completed= false”  is converted to camelcase 
# and returns the response with converted title and status in json format.
@app.route("/api/camelcase/", methods = ['GET','POST','DELETE'])
def function_camelcase():
    try:
        with open('jsonfiles.json') as json_file:
            users = json.load(json_file)
            json_file.close()
        camelcase=[]
        for user in users:
            if str(user['completed']) == 'false':
                camelcase.append({
                    'userId': user['userId'],
                    'id': user['id'],
                    'title':user['title'].title(),
                    'completed': user['completed']
                })
        return jsonify({'data':camelcase})

    except FileNotFoundError:
        return({
            'status': 404,
            'error':'File Not Found'
            })

# QN3 Create an API to update completed status to false for given userid.
@app.route("/api/update/<int:userId>", methods = ['GET','POST','PUT'])
def function_update(userId):
    if request.method=='PUT':
        try:
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
                'error':'File Not Found'
                })
    else:
        return({
                'status': 404,
                'error':'Wrong Found'
                })

# QN4 Create an api to delete all todos which have been completed for userid=3
@app.route("/api/delete/<int:userId>", methods = ['DELETE'])
def function_delete(userId):
    try:
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
    except FileNotFoundError:
        return({
                'status': 404,
                'error':'File not Found'
                })

# QN5 Create an API to insert a new record and display Success message along with 
# record that has been inserted for provided userid.
@app.route("/api/insert/<int:userId>", methods = ['POST'])
def function_insert(userId):
    try:
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
                'error':'Successful'
                })
        else:
            return({
            'status': 404,
            'error':'Wrong Found'
            })
            
    except FileNotFoundError:
        return({
            'status': 404,
            'error':'File not Found'
            })


# QN6  in file named as placeholdersQ6.py              

if __name__ == "__main__":
    app.run(debug=True)
