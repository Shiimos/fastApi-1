from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1:{
        "name": "Ismael",
        "age": 19,
        "classe": "Data structures"
    }
}

@app.get("/")
def index():
    return {"name": "first data"}

@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="Must input the idea of the student", gt = 0, lt = 3)):
    return students[student_id]