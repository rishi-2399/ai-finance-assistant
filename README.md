# AI-Based Personal Finance Assistant

### Setup Instructions
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Initialize database:
   ```
   python app/database.py
   ```
3. Run the backend:
   ```
   uvicorn app.main:app --reload
   ```
4. Open `frontend/index.html` in a browser.
