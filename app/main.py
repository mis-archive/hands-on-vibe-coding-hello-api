from fastapi import FastAPI


app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hey there! 👋"}


@app.get("/goodbye")
def goodbye():
    return {"message": "Catch you later! ✌️"}


