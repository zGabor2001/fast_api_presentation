from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/add")
def add(a: float, b: float) -> dict:
    """Add two numbers."""
    return {"result": a + b}


@router.get("/subtract")
def subtract(a: float, b: float) -> dict:
    """Subtract two numbers."""
    return {"result": a - b}


@router.get("/multiply")
def multiply(a: float, b: float) -> dict:
    """Multiply two numbers."""
    return {"result": a * b}


# Exercise 1 ###

# Implement the /divide endpoint here based on the above functions
# Remember, no division by zero. What should be the condition?
# Tip: add an exception handling condition: an 'if' that returns an HTTPException with the
# correct status code when the number you divide with is zero.

