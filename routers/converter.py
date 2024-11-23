from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/km-to-m")
def km_to_miles(km: float) -> dict:
    """Convert kilometers to miles."""
    if km < 0:
        raise HTTPException(status_code=400, detail="Distance cannot be negative")
    miles = km * 0.621371
    return {"kilometers": km, "miles": round(miles, 2)}

@router.get("/m-to-km")
def miles_to_km(miles: float) -> dict:
    """Convert miles to kilometers."""
    if miles < 0:
        raise HTTPException(status_code=400, detail="Distance cannot be negative")
    km = miles / 0.621371
    return {"miles": miles, "kilometers": round(km, 2)}

@router.get("/c-to-f")
def celsius_to_fahrenheit(celsius: float) -> dict:
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9/5) + 32
    return {"celsius": celsius, "fahrenheit": round(fahrenheit, 2)}

@router.get("/f-to-c")
def fahrenheit_to_celsius(fahrenheit: float) -> dict:
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return {"fahrenheit": fahrenheit, "celsius": round(celsius, 2)}