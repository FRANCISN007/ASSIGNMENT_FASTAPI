from fastapi import FastAPI

app=FastAPI()

Student = {}

@app.get('/')
def home():
    return {"Message": "at home"}

@app.post('/Students')
def create_student(id: str, name: str, age: int, sex: str, height:float ):
    new_student = {
        'id': id,
        'name': name,
        'age': age,
        'sex' : sex,
        'height' : height,
    }
@app.update('/Students')
def update_student(id: str, name: str, age: int, sex: str, height:float ):

 @app.delete('/Students')   
 def delete_student(id: str, name: str, age: int, sex: str, height:float ):

 
    


