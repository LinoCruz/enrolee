from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Event: 
    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.description = data["description"]
        self.host = data["host"]
        self.location = data["location"]
        self.cost = data["cost"]
        self.date = data["date"]
        self.time = data["time"]
        self.registration = data["registration"]
        self.image = data["image"]
        self.user_id = data["user_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    #VALIDATE EVENT
    @staticmethod
    def validate_event(formulario):
        es_valido = True

        if len(formulario['title']) < 3:
            flash("The event title must have at least 3 characters", "event")
            es_valido = False
        
        if len(formulario['description']) < 3:
            flash("The description must have at least 3 characters", "event")
            es_valido = False
                
        if formulario['date'] == "":
            flash("Insert a Date", "event")
            es_valido = False
        
        if formulario['time'] == "":
            flash("Insert a time", "event")
            es_valido = False
        
        return es_valido
    
    
    #SAVE  NEW EVENT
    @classmethod
    def save(cls, data):
        query = "INSERT INTO events (title, description,host, location,cost,date,time,registration,image, user_id) VALUES (%(title)s, %(description)s, %(host)s, %(location)s, %(cost)s, %(date)s,%(time)s, %(registration)s,%(image)s,%(user_id)s);"
        newId = connectToMySQL('enrolee').query_db(query, data)
        
        list_tags =data["tags"].split(",")
        for tag in list_tags:
            query="INSERT INTO tags (name, event_id) VALUES (%(name)s, %(event_id)s)"
            data={"name" : tag, "event_id": newId}
            nuevox = connectToMySQL('enrolee').query_db(query, data)
        return newId
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM events"
        results = connectToMySQL('enrolee').query_db(query)
        events = []
        for event in results:
            events.append(cls(event))
        return events
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM events WHERE id = %(id)s"
        result = connectToMySQL('enrolee').query_db(query, data)
        event = cls(result[0])
        return event
    
    @classmethod
    def get_user_created_event(cls, data):
        query = "SELECT * FROM events INNER JOIN users ON events.user_id = users.id WHERE  users.id = %(id)s ORDER BY date DESC LIMIT 1;"
        result = connectToMySQL('enrolee').query_db(query, data)
        event = cls(result[0])
        print(result)
        return event
    
    @classmethod
    def users_events(cls, data):
        query = "SELECT * FROM events INNER JOIN users ON events.user_id = users.id WHERE  users.id = %(id)s ORDER BY date DESC;"
        result = connectToMySQL('enrolee').query_db(query, data)
        events = []
        for event in result:
            events.append(cls(event))
        return events
    
    
    @classmethod
    def update(cls, data):
        query = "UPDATE events SET name = %(name)s, under30 = %(under30)s, description = %(description)s, instructions = %(instructions)s, date_made = %(date_made)s WHERE (id = %(id)s);"
        result = connectToMySQL('enrolee').query_db(query, data)
        return result
    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM events WHERE id = %(id)s"
        return connectToMySQL('enrolee').query_db(query, data)