import requests

database = {
    "1" : "Anusha", 
    "2" : "Abheek",
    "3" : "Hemlata",
    "4" : "Mukesh",
 }

def get_user_by_id(user_id):
    return database.get(user_id, "User not found")

def get_user():
    response = requests.get(f"https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    else:
        return "User not found"