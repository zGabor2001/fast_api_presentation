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


# Implement the /divide endpoint here based on the above functions
# Remember, no division by zero.
# Tip: add an if that returns an HTTPException with the
# correct status code when the number you divide with is zero

@router.get("/divide")
def divide(a: float, b: float) -> dict:
    """Divide two numbers."""
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {"result": a / b}
