# helloTest.py
# at the end point / call method hello which returns "hello world"

from flask import Flask, render_template
from flask import request
import pyrebase
app = Flask(__name__)

config = {
  "apiKey": "AIzaSyAULHAeNQR_uxYqfa-tgSGQp0Re3dg6YmE",
  "authDomain": "shlok-s-project.firebaseapp.com",
  "databaseURL": "https://shlok-s-project-default-rtdb.firebaseio.com/",
  "storageBucket": "shlok-s-project.appspot.com"
}

firebase = pyrebase.initialize_app(config)

@app.route("/")
def hello():
  return render_template("hello.html")

@app.route("/upload_file")
def upload_file():
    return render_template("upload_file.html")
    '''storage = firebase.storage()
    storage.child("photos/myPictureName.jpg").download("D:\project","ABCD.jpg")'''
    

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        return render_template("success.html", name = f.filename)  


if __name__ == '__main__':
  app.run(debug=True)









'''import pyrebase



def main():
    
    
    db= firebase.database()
    data = {"name": "vivek"}
    db.child("users").child("Morty").set(data)   
    
if __name__ == "__main__":
    main()'''