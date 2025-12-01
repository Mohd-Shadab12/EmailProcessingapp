from fastapi import FastAPI
from pydantic import BaseModel
from llm_model import process_given_email

app=FastAPI()

class Emailinput(BaseModel):
    email:str

@app.post("/generate")
def generate_output(data:Emailinput):
    try:
        output=process_given_email(data.email)
        return {"result":output}
    except Exception as e:
        return {"error": str(e)}