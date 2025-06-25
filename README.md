# AI-Based Personal Finance Assistant

<img align="centre" alt="Coding" width="400" src="https://github.com/rishi-2399/ai-finance-assistant/blob/92471f49f3ec082e2cafe0e7ebaf16e52b496ab3/images/front_interface_FA.png">


<img align="centre" alt="Coding" width="400" src="https://github.com/rishi-2399/ai-finance-assistant/blob/37d089ed73e28e77f59e15aed2bbb0c42108ede9/images/sample_FA.png">


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
