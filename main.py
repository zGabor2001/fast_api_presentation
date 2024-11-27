from fastapi import FastAPI
from routers import calculator, converter


app = FastAPI()

app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])

# Exercise 2 #
# Add converter router here based on the calculator router above
# Remember to define prefix param!


@app.get("/")
def read_root() -> dict:
    return {"message": "Your server is running!"}
