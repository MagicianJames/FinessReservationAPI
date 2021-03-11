from flask import Flask, request, session
from local import storage
import sqlite3
# from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask("Flask test")
# json = FlaskJSON(app)
LOCAL_DB = 'local.db'

@app.route('/')
def index(): 
    return 'James is here'

@app.route('/test')
def test():
    return storage.query_get_classes()

@app.route('/user')
def user():
    return storage.query_get_user()

@app.route('/trainer')
def trainer():
    return storage.query_get_trainer()

@app.route('/room')
def room():
    return storage.query_get_room()

@app.route('/class')
def get_class_info():
    return storage.query_get_class_detail()

@app.route('/timeslot')
def get_timeslot():
    return storage.query_get_timeslot()

@app.route('/add-timeslot')
def addTimeslot():
    storage.add_timeslot()
    return 'Add class successfully'

@app.route('/add-class')
def addClass():
    storage.add_class()
    return 'Add class successfully'

@app.route('/add-user')
def addUser():
    storage.add_user()
    return 'Add user successfully'
    
@app.route('/add-trainer')
def addTrainer():
    storage.add_trainer()
    return 'Add trainer successfully'

@app.route('/add-room')
def addRoom():
    storage.add_room()
    return 'Add room successfully'    

@app.route('/insert-user', methods=['POST'])
def insertUser():
    data = request.get_json()
    try:
        storage.insert_user(data['first_name'], data['last_name'], data['username'], data['password'], data['email'])
        return storage.query_get_user()
    except:
        return 'Fail'
    
@app.route('/insert-trainer', methods=['POST'])
def insertTrainer():
    data = request.get_json()
    try:
        storage.insert_trainer(data['first_name'], data['last_name'], data['phone_number'])
        return storage.query_get_trainer()
    except:
        return 'Fail'
            
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result = storage.login(data['username'], data['password'])
    
    if (result is not None):
        return result
    else:
        return 'Failed'
    
@app.route('/insert-class', methods=['POST'])
def insert_class():
    data = request.get_json()
    try:
        storage.insert_class(data['class_name'], data['picture_url'], data['trainer_id'], data['people_number'], data['class_date'], data['room_id'], data['schedule_time_id'])
        return storage.query_get_class_detail()
    except:
        return 'Fail'
    
@app.route('/edit-user', methods=['POST'])
def edit_user():
    data = request.get_json()
    storage.edit_user(data)
    return storage.query_get_user()

@app.route('/delete-trainer', methods=['POST'])
def delete_trainer():
    data = request.get_json()
    storage.delete_trainer(data)
    return storage.query_get_trainer()

@app.route('/delete-all-class')
def delete_all_classes():
    storage.delete_all_class()
    return storage.query_get_class_detail()
        
@app.route('/get-class-detail')
def get_class_detail():
    data = request.args.get('class-id')
    print('James: ', data)
    return storage.get_class_detail_by_class_id(data)

@app.route('/get-room-name')
def get_room_name():
    return storage.query_room_name()
    


app.run(debug = True)

