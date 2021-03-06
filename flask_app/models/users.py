from flask_app.config.mysqlconnection import connectToMySQL
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class User:

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls, data):
        #data = {
        #     "first_name": "Elena",
        #     "last_name": "De Troya",
        #     "email": "elena@cd.com",
        #     "password": "91289128snkndsaajdyasdl"
        # }
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        nuevoId = connectToMySQL('enrolee').query_db(query, data)
        return nuevoId
    
    @staticmethod
    def valida_usuario(formulario):
        # formulario = {
        #     "first_name": "Emilio",
        #     "last_name": "Navejas",
        #     "email": "emilio@codingdojo.com",
        #     "password": "12345"
        # }

        es_valido = True

        #Validar que mi nombre sea mayor a 2 caracteres
        if len(formulario['first_name']) < 2:
            flash('Name must have at least 2 characters', 'registro')
            es_valido = False
        #Validar que mi apellido sea mayor a 2 caracteres
        if len(formulario['last_name']) < 2:
            flash('Last name must have at least 2 characters', 'registro')
            es_valido = False
        #Valido email con expresiones regulares #abc123@21msn.com ->NO te aceptaría a.com
        if not EMAIL_REGEX.match(formulario['email']):
            flash('Wrong email', 'registro')
            es_valido = False
        if len(formulario['password']) < 8:
            flash('Password must have at least 8 characters', 'registro')
            es_valido = False
        if formulario['password'] != formulario['confirm']:
            flash('Passwords do not match', 'registro')
            es_valido = False
        
        #Consulta si ya existe ese correo
        query = "SELECT id FROM users WHERE email = %(email)s"
        results = connectToMySQL('enrolee').query_db(query, formulario)
        #results = [
        #     {"first_name": "Cynthia", "last_name":"Castillo"}
        # ]
        if len(results) >= 1:
            flash('E-mail registrado previamente', 'registro')
            es_valido = False

        return es_valido

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('enrolee').query_db(query, data)
        usr = result[0]
        user = cls(usr)
        return user
    
    @classmethod
    def get_by_email(cls, data):
        # data = {
        #     "email": "lino@codingdojo.com",
        #     "password": "1234"
        # }
        query = "SELECT * FROM users WHERE email = %(email)s"
        result = connectToMySQL('enrolee').query_db(query, data)
        if len(result) < 1:
            return False
        else :
            usr = result[0]
            #usr = {"id": "1", "first_name": "Elena", "last_name": "De Troya", "email": "elena@cd".......}
            user = cls(usr)
            return user