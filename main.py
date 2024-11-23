from fastapi import FastAPI
from routers import calculator, converter


app = FastAPI()

app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])

# Add router here based on the calculator router above
# Remember to define prefix param!
app.include_router(converter.router, prefix="/converter", tags=["Metric Converter"])


@app.get("/")
def read_root() -> dict:
    return {"message": "Your server is running!"}
