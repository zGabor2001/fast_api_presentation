## Repo for FastAPI sample presentation for Lumos Student Data Consulting

Recommended to use Postman for request sending.

1. Install Python 3.12, if you dont have it
2. Open your IDE
3. Go to the terminal and run these commands:
   - On Windows:
      - python -m venv venv
      - venv/scripts/activate
      - pip install -r requirements.txt
   - On Mac:
      - python -m venv venv
      - source venv/bin/activate
      - pip install -r requirements.txt
4. Start your server in terminal with running:
   - uvicorn main:app --reload
5. Your API is available at: http://127.0.0.1:8000/ (localhost)

If using curl to send requests:
- curl "http://127.0.0.1:8000/calculator/add?a=10&b=5"
