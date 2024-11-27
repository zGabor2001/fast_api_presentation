from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/km-to-mi")
def km_to_miles(km: float) -> dict:
    """Convert kilometers to miles."""
    if km < 0:
        raise HTTPException(status_code=400, detail="Distance cannot be negative")
    miles = km * 0.621371
    return {"kilometers": km, "miles": round(miles, 2)}

# Exercise 3 (Bonus) ###

# What is missing? Implement the opposite function - convert miles to kilometers.
# Remember, distances cannot be negative.
# Tip: add an 'if' that returns an HTTPException with the
# correct status code when the miles number entered is negative.


@router.get("/c-to-f")
def celsius_to_fahrenheit(c: float) -> dict:
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (c * 9/5) + 32
    return {"celsius": c, "fahrenheit": round(fahrenheit, 2)}


@router.get("/f-to-c")
def fahrenheit_to_celsius(f: float) -> dict:
    """Convert Fahrenheit to Celsius."""
    celsius = (f - 32) * 5/9
    return {"fahrenheit": f, "celsius": round(celsius, 2)}
