from flask import Flask, render_template,request,redirect
from pymongo import MongoClient




# app.config['MONGO_URI']="mongodb://localhost:27017/intern23"
# mongo=PyMongo(app)
app = Flask(__name__)
URI="mongodb://localhost:27017"
client=MongoClient(URI)
print(":)")
db=client["intern"]
collection=db["user"]

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/signup',methods=['GET','POST'])

def signup():
    if(request.method=='POST'):
        email=request.form.get('email')
        name=request.form.get('name')
        contact=request.form.get('phone')
        password=request.form.get('password')
        profile=request.form.get('currprofile')
        
        
        if collection.find_one({'email':email}):
            return render_template('login.html',content="User Already Exist! Login here")
        
        user_data={
            'name':name,
            'email':email,
            'password':password,
            'contact':contact,
            'profile':profile
        }
        collection.insert_one(user_data)
        print(user_data)
        print("User added successfully :) ")
        return redirect('/login')
    else:
        print("not working")
        return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login_user():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password') 
        print(email)
        print(password)
        user=collection.find_one({'email': email, 'password': password})
        if user:
            print("Login Successfullyyy")
            return redirect('/')
        else:
            print("wrong credential")
            return render_template('login.html',content="Wrong Credential")
    else:
        return render_template('login.html',content="Login here")





if __name__=='__main__':
    app.run(debug="True")
