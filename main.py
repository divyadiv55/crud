from flask import Flask,render_template,redirect,request
from app import *
app=Flask(__name__)


def register_student(name,age,course,courseduration):
    data=read_json()
    id=len(data["students"])+1
    stud_data={
        "id":id,
         "name":name,
         "age":age,
         "course":course,
         "courseduration":courseduration
          
     }
    data["students"].append(stud_data)
    write_json(data)
    print("Student registered successfully!")

@app.route("/")
def homepage():
    data=read_json()
    return render_template("app.html",data_html=data["students"])

@app.route("/delete/<id>")
def delete(id):
    data=read_json()
    for stud in data["students"]:
        if int(id)==stud["id"]:
            data["students"].remove(stud)
            
    num=1
    for stud in data["students"]:
        stud["id"]=num
        num+=1
    write_json(data)
    return redirect("/")



@app.route("/update/<id>",methods=["GET","POST"])
def update(id):
    data=read_json()
    for stud in data["students"]:
        if int(id)==stud["id"]:
            stud["name"]=request.form["name"]
            stud["age"]=request.form["age"]
            stud["course"]=request.form["course"]
            stud["courseduration"]=request.form["courseduration"]
            
    
            
    write_json(data)
    return redirect("/")
    



@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="POST":
        # print(request.form["name"])
        # print(request.form["age"])
        # print(request.form["course"])
        # print(request.form["courseduration"])
       register_student(request.form["name"],request.form["age"],request.form["course"],request.form["courseduration"])
       
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)
    
    