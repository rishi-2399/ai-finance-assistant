import requests

# Test adding expense
data = {"user_id": 2, "category": "Food", "amount": 20.5}
response = requests.post("http://127.0.0.1:8000/add_expense/", json=data)
print(response.json())

# Test getting expenses
response = requests.get("http://127.0.0.1:8000/get_expenses/", params={"user_id": 2})
print(response.json())
