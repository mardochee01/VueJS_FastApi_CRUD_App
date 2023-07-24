from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from database import student_collection
from models import Student

router = APIRouter()

@router.post("/students/", response_model=Student)
async def create_student(student: Student):
    inserted_student = student_collection.insert_one(student.dict())
    student.id = str(inserted_student.inserted_id)
    return student

@router.get("/students/{student_id}", response_model=Student)
async def read_student(student_id: str):
    student = student_collection.find_one({"_id": ObjectId(student_id)})
    if student is None:
        raise HTTPException(status_code=404, detail="Student Not found")
    return student

@router.put("/students/{student_id}", response_model=Student)
async def update_student(student_id: str, student: Student):
    update_student = student_collection.find_one_and_update(
        {"_id": ObjectId(student_id)}, {"$set": student.dict()}, return_document=True)
    if update_student is None:
        raise HTTPException(status_code=404, detail="Student Not found")
    return update_student

@router.delete("/students/{student_id}", response_model=Student)
async def delete_student(student_id: str):
    delete_student = student_collection.find_one_and_delete({"_id": ObjectId(student_id)})
    if delete_student is None:
         raise HTTPException(status_code=404, detail="Student Not found")
    return delete_student

@router.get("/students/", response_model=list[Student])
async def read_all_student():
    students = list(student_collection.find())
    return students