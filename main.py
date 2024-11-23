from fastapi import FastAPI
from routers import calculator, converter

app = FastAPI(title="FastAPI Project with Two Routers")

app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])
# Add router here
app.include_router(converter.router, prefix="/metric-converter", tags=["Metric Converter"])

@app.get("/")
def read_root() -> dict:
    return {"message": "Welcome to the FastAPI project with Calculator and Metric Converter"}