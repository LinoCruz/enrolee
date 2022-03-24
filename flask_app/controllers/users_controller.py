from flask import jsonify, render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.users import User
# from flask_app.models.events import Event
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

#PRINCIPAL
@app.route("/")
def index():
    return render_template('index.html')

#SIGNUP AND LOGIN PAGE
@app.route("/signup")
def signup():
    return render_template('register.html')

#DASHBOARD
@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')

#FUNCTION TO REGISTER USERS
@app.route("/register", methods=["POST"])
def register():
    if not User.valida_usuario(request.form):
        return redirect("/signup")
    
    pwd = bcrypt.generate_password_hash(request.form['password'])
    
    data={
       "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pwd
    }
    #Get id with User.save
    id= User.save(data)
    #Put the user id's into session
    session['user_id'] = id
    
    return redirect("/dashboard")

#FUNCTION TO 
@app.route("/login", methods=["POST"])
def login():
    user = User.get_by_email(request.form)
        #user = User -> first_name, last_name, password, email ....

    if not user:
            # flash("Email not found", "login")
            # return redirect('/')
            return jsonify(message="Email not found")
        
    if not bcrypt.check_password_hash(user.password, request.form['password']):
            # flash("Wrong password", "login")
            # return redirect('/')
            return jsonify(message="Wrong password")
        
    session['user_id'] = user.id
    # return redirect('/dashboard')
    return jsonify(message="Welcome back")

