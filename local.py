import sqlite3
import json
from flask import jsonify, session

LOCAL_DB = 'local.db'

class LocalStorage:
    def __init__(self):
        
        if not self.checkTableExist():
            self.initializeDatabase()
            
    def initializeDatabase(self):
       with sqlite3.connect(LOCAL_DB) as conn:
           cur = conn.cursor()
           cur.execute(
               '''
               CREATE TABLE Class
               (
                   id INTEGER PRIMARY KEY,
                   class_name TEXT,
                   room_id INTEGER,
                   picture_url TEXT,
                   people_number INTEGER,
                   class_date timestamp,
                   schedule_time_id, INTEGER,
                   trainer_id INTEGER,
                   FOREIGN KEY(room_id) REFERENCES Room(id),
                   FOREIGN KEY(schedule_time_id) REFERENCES ScheduleTime(id)
                   FOREIGN KEY(trainer_id) REFERENCES Trainer(id)
               )
               ''')
           cur.execute(
               '''
               CREATE TABLE Room
               (
                   id INTEGER PRIMARY KEY,
                   room_name TEXT,
                   is_active INTEGER
               )
               ''')
           cur.execute(
               '''
               CREATE TABLE ScheduleTime
               (
                  id INTEGER PRIMARY KEY,
                  start_time timestamp,
                  end_time timestamp
               )
               ''')
           cur.execute(
               '''
               CREATE TABLE Trainer
               (
                   id INTEGER PRIMARY KEY,
                   first_name TEXT,
                   last_name TEXT,
                   gender TEXT,
                   phone_number TEXT,
                   email TEXT
               )
               ''')
           cur.execute(
               '''
               CREATE TABLE UserClass
               (
                   id INTEGER PRIMARY KEY,
                   class_id INTEGER,
                   user_id INTEGER,
                   FOREIGN KEY(class_id) REFERENCES Class(id),
                   FOREIGN KEY(user_id) REFERENCES User(id)
               )
               ''')
           cur.execute(
               '''
               CREATE TABLE User
               (
                   id INTEGER PRIMARY KEY,
                   first_name TEXT,
                   last_name TEXT,
                   username TEXT,
                   password TEXT,
                   email TEXT
               )
               ''')
           conn.commit()

    def checkTableExist(self):
        with sqlite3.connect(LOCAL_DB) as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT count(name) 
                FROM sqlite_master 
                WHERE type='table' 
                    AND 
                    name='Class' 
                ''')  
            
            if cur.fetchone()[0] == 1:
                return True
            else:
                return False
            
    def get_connection(self):
        return sqlite3.connect(LOCAL_DB)        
            
    def get_class(self):
        with sqlite3.connect(LOCAL_DB) as conn:
            print('get_feature is here......')
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT *
                FROM Class
                ''')
        return cur.fetchall()
    
    def get_picture(self):
        with sqlite3.connect(LOCAL_DB) as conn:
            print('get_picture is here...')
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT *
                FROM Picture
                ''')
        
        return cur.fetchall()
            
    def get_room(self):
        with sqlite3.connect(LOCAL_DB) as conn:
            print('get_room is here....')
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT *
                FROM Room
                '''
            )
        return cur.fetchall()
    
    def add_class(self):
        with sqlite3.connect(LOCAL_DB) as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                insert into Class 
                (picture_url, class_name, room_id, class_date, people_number) 
                values 
                ('https://firebasestorage.googleapis.com/v0/b/gjservice-14737.appspot.com/o/BodyJam.jpg?alt=media&token=cc36589a-0450-4ade-ab3c-c53fbdb1ee71', 'Body Jam', 1, '08/06/2021', 30);
                ''')
            cur.execute(
                '''
                insert into Class 
                (picture_url, class_name, room_id, class_date, people_number) 
                values 
                ('https://firebasestorage.googleapis.com/v0/b/gjservice-14737.appspot.com/o/Boxing.jpg?alt=media&token=d856c6bb-34ff-41b9-b337-3c9e38d14670', 'Boxing', 1, '08/06/2021', 20);
                ''')
            cur.execute(
                '''
                insert into Class 
                (picture_url, class_name, room_id, class_date, people_number) 
                values 
                ('https://firebasestorage.googleapis.com/v0/b/gjservice-14737.appspot.com/o/BodyPump.jpg?alt=media&token=08dbf59c-76b3-4fb5-ac93-044689acab8a', 'Body Pump', 1, '08/06/2021', 20);
                ''')
            cur.execute(
                '''
                insert into Class 
                (picture_url, class_name, room_id, class_date, people_number) 
                values 
                ('https://firebasestorage.googleapis.com/v0/b/gjservice-14737.appspot.com/o/Cycling.jpg?alt=media&token=e4fec5c1-b466-49cf-9302-7e3b06e28180', 'Cycling', 1, '08/06/2021', 10);
                ''')
            cur.execute(
                '''
                insert into Class 
                (picture_url, class_name, room_id, class_date, people_number) 
                values 
                ('https://firebasestorage.googleapis.com/v0/b/gjservice-14737.appspot.com/o/Weight%20Training.jpg?alt=media&token=b7399c7e-c847-4dce-b538-d154f162ced1', 'Weight Training', 1, '08/06/2021', 20);
                ''')
            cur.execute(
                '''
                insert into Class 
                (picture_url, class_name, room_id, class_date, people_number) 
                values 
                ('https://firebasestorage.googleapis.com/v0/b/gjservice-14737.appspot.com/o/Yoga.jpg?alt=media&token=eb520a72-ce39-4ef2-b2dc-e9dae5c97071', 'Yoga', 1, '08/06/2021', 15);
                ''')
            cur.execute(
                '''
                insert into Class 
                (picture_url, class_name, room_id, class_date, people_number) 
                values 
                ('https://firebasestorage.googleapis.com/v0/b/gjservice-14737.appspot.com/o/Zumba.jpg?alt=media&token=b0bb7e32-2e4d-46d9-bdb9-6b116218372b', 'Zumba', 1, '08/06/2021', 30);
                ''')
            conn.commit()
            
    def add_user(self):
        with sqlite3.connect(LOCAL_DB) as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                insert into User 
                (first_name, last_name, username, password, email) 
                values 
                ('Kaila', 'Lyffe', 'klyffe0', 'R0SZs7', 'klyffe0@telegraph.co.uk');
                ''')
            conn.commit()
    
    def insert_user(self, first_name, last_name, username, password, email):
        with sqlite3.connect(LOCAL_DB) as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                insert into User 
                (first_name, last_name, username, password, email) 
                values 
                (?, ?, ?, ?, ?);
                ''', [first_name, last_name, username, password, email])
            
            conn.commit()
            
    def insert_trainer(self, first_name, last_name, phone_number):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                insert into Trainer
                (first_name, last_name, phone_number)
                values
                (?, ?, ?);
                ''', [first_name, last_name, phone_number])
            
            
            conn.commit()
           
    def insert_class(self, class_name, picture_url, trainer_id, people_number, class_date, room_id, schedule_time_id):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                insert into Class
                (class_name, picture_url, trainer_id, people_number, class_date, room_id, schedule_time_id)
                values
                (?, ?, ?, ?, ?, ?, ?);
                ''', [class_name, picture_url, trainer_id, people_number, class_date, room_id, schedule_time_id])
        
            conn.commit()    
                  
    def add_trainer(self):
        with sqlite3.connect(LOCAL_DB) as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                insert into Trainer 
                (first_name, last_name, gender, phone_number, email) 
                values 
                ('Krittamet', 'Chuwongworaphinit', 'Male', '092-315-2166', 'great@gmail.com');
                ''')
            cur.execute(
                '''
                insert into Trainer 
                (first_name, last_name, gender, phone_number, email) 
                values 
                ('Phanuwat', 'Sikharestrakul', 'Male', '095-778-2182', 'james@gmail.com');
                ''')
            cur.execute(
                '''
                insert into Trainer 
                (first_name, last_name, gender, phone_number, email) 
                values 
                ('Phanuwat', 'Sikharestrakul', 'Male', '095-778-2182', 'james@gmail.com');
                ''')
            cur.execute(
                '''
                insert into Trainer 
                (first_name, last_name, gender, phone_number, email) 
                values 
                ('Sanpawat', 'Sewsuwan', 'Male', '091-778-1332', 'yong@gmail.com');
                ''')
            cur.execute(
                '''
                insert into Trainer 
                (first_name, last_name, gender, phone_number, email) 
                values 
                ('Saharat', 'Tiewkunupakan', 'Male', '081-777-2222', 'tiew@gmail.com');
                ''')
            cur.execute(
                '''
                insert into Trainer 
                (first_name, last_name, gender, phone_number, email) 
                values 
                ('Kanyarat', 'Nalucupchanchai', 'Female', '085-718-5143', 'ping-ping@gmail.com');
                ''')
            
            conn.commit()
            
    def add_room(self):
        with sqlite3.connect(LOCAL_DB) as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                insert into Room 
                (room_name, is_active)
                values 
                ('Divavu', 1);
                ''')
            conn.commit()
            
    def add_timeslot(self):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                insert into ScheduleTime 
                (start_time, end_time) 
                values ('11:49', '10:40');
                '''
            )
    
    def query_get_classes(self):
        with sqlite3.connect(LOCAL_DB) as conn:
            print('get_feature is here......')
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT id, class_name, room_id, people_number
                FROM Class
                ''')
            
        data = cur.fetchall()
        result = []
        
        for i in range(len(data)):
            a = {'id': data[i][0],
                'class_name': data[i][1],
                'room_id': data[i][2],
                'people_number': data[i][3]}
            
            result.append(a)
        
        return jsonify(result) 
    
    def query_get_user(self):
        with self.get_connection() as conn:
            print('get_user is here....')
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT *
                FROM User
                ''')
            
        data = cur.fetchall()
        result = []
        
        for i in data:
            a = {'id': i[0],
                 'first_name': i[1], 
                 'last_name': i[2], 
                 'username': i[3], 
                 'password': i[4],
                 'email': i[5]}

            result.append(a)
        
        return jsonify(result)
    
    def query_get_trainer(self):
        with self.get_connection() as conn:
            print('get_trainer is here....')
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT id, first_name, last_name, phone_number
                FROM Trainer
                ''')
        data = cur.fetchall()
        result = []    
        
        for i in range(len(data)):
            a = {'id': data[i][0],
                 'first_name': data[i][1], 
                 'last_name': data[i][2], 
                 'phone_number': data[i][3]}
            
            result.append(a)
        
        b = {'trainers': result}
        return jsonify(b)
    
    def query_get_room(self):
        data = []
        dictionary = self.get_room()
        
        for i in range(len(dictionary)):
            a = {'id': dictionary[i][0],
                 'room_name': dictionary[i][1], 
                 'is_active': dictionary[i][2]}
            
            data.append(a)
        return jsonify(data)
    
    def query_get_timeslot(self):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT *
                FROM ScheduleTime
                ''')
            data = cur.fetchall()
            result = []    
        
        for i in range(len(data)):
            a = {'id': data[i][0],
                 'start_time': data[i][1],
                 'end_time': data[i][2]}
            
            result.append(a)
            
        return jsonify(result)
        
    def login(self, username, password):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT id, username, password
                FROM User
                WHERE username = ? AND password = ?
                '''
                , [username, password])
            
            data = cur.fetchone()
            json_login = {'id': data[0],
                          'username': data[1],
                          'password': data[2]}
            
            return jsonify(json_login)
        
    def get_user_by_username(self, username):
        with sqlite3.connect(LOCAL_DB) as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT *
                FROM User
                WHERE username = ?
                '''
            , [username])
            
            return cur.fetchone()
        
    def edit_user(self, user):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                UPDATE User
                SET first_name = ?, 
                last_name = ?, 
                username = ?, 
                password = ?, 
                email = ?
                WHERE id = ?
                '''
            , [user['first_name'], user['last_name'], user['username'], user['password'], user['email'], user['id']])
            
            conn.commit()
            
    def edit_class_user(self, room):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                UPDATE Room
                SET room_id = ?
                room_name = ?
                '''
                ,[room['room_id'],room['room_name']])
            
            conn.commit()
                
    def delete_trainer(self, trainer):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                DELETE 
                FROM Trainer
                WHERE id = ?
                '''
            , [trainer['id']])
            conn.commit
            
    def delete_all_class(self):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                DELETE
                FROM Class
                ''')
            conn.commit()              
            
    def get_class_detail_by_class_id(self, class_id):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT Class.people_number, Room.id, Room.room_name
                FROM Class
                JOIN Room ON Class.room_id = Room.id
                ''')

            data = cur.fetchall()
            result = []
          
            for i in range(len(data)):
                a = {'people_number': data[i][0],
                     'room_id': data[i][1],
                     'room_name': data[i][2]}
            
            result.append(a)
        
        return jsonify(result) 
        
    def query_get_class_detail(self):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT id, picture_url, class_name, class_date, people_number
                FROM Class
                ''')
            
            data = cur.fetchall()
            result = []    
        
        for i in range(len(data)):
            a = {'id': data[i][0],
                 'picture_url': data[i][1],
                 'class_name': data[i][2], 
                 'class_date': data[i][3], 
                 'people_number': data[i][4]}
            
            result.append(a)
            
        b = {'class_ex': result}
        return jsonify(b)
        
    def query_room_name(self):
        with self.get_connection() as conn:
            cur = conn.cursor()
            cur.execute(
                '''
                SELECT id, room_name
                FROM Room
                ''')
            data = cur.fetchall()
            result = []    
        
        for i in range(len(data)):
            a = {'id': data[i][0],
                 'room_name': data[i][1]}
            
            result.append(a)
            
        return jsonify(result)
        
storage = LocalStorage()

