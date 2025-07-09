from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI() # fastapi instance

students={} # empty dictionary

class Student(BaseModel):
    name:str
    gender:str
    age:int

#creating a new student record
@app.post("/students/{student_id}") #this is the post endpoint visible on swagger UI.
def create_student(student_id:int, student:Student): #while trying out, we need to enter student id and Student details
                                                     #(name, gender, age) as input
    if student_id in students:
        raise HTTPException(status_code=404,detail="Student already exists")
    students[student_id]=student
    return {"message":"Student added successfully","student":student}

#reading a student record
@app.get("/students/{student_id}")#this is the get endpoint visible on swagger UI.
def read_student(student_id:int):#before getting any student record, we need to input the student_id
    if student_id not in students:
        raise HTTPException(status_code=404,detail="student detail not found")
    return students[student_id]

#updating a student record
@app.put("/students/{student_id}")# this is the put endpoint on swagger UI.
def update_student(student_id:int,student:Student):#in order to update the student record, we need to 
                                                    #input the id and the updated student details.
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    students[student_id]=student
    return {
        "message":"Student detail updated successfully",
        "student":student
    }

@app.delete("/students/{student_id}")# this is the delete endpoint on swagger UI.
def delete_student(student_id:int):# in order to delete a student record, we need to input the student_id
    if student_id not in students:
        raise HTTPException(status_code=404,detail="Student does not exist")
    del students[student_id]

