import requests

BASE_URL = "https://act-4-padilla.onrender.com"

# 1. HOME
print("\n===== HOME ENDPOINT =====")
response = requests.get(BASE_URL + "/")
print(response.text)

# 2. STUDENT
print("\n===== STUDENT ENDPOINT =====")
response = requests.get(BASE_URL + "/student")

if response.status_code == 200:
    data = response.json()
    print("Student ID:", data["student_id"])
    print("Name:", data["name"])
    print("Program:", data["program"])
    print("Year:", data["year"])
    print("Section:", data["section"])
else:
    print("Request failed:", response.status_code)

# 3. HELLO
print("\n===== HELLO ENDPOINT =====")
name = input("Enter your first name: ")

response = requests.get(
    BASE_URL + "/hello",
    params={"name": name}
)

if response.status_code == 200:
    print(response.json())

# 4. MY HOBBIES
print("\n===== MY HOBBIES =====")
response = requests.get(BASE_URL + "/my-hobbies")

if response.status_code == 200:
    data = response.json()
    print("Name:", data["name"])
    print("Hobbies:", data["hobbies"])
    print("Favorite Hobby:", data["favorite_hobby"])
else:
    print("Request failed:", response.status_code)

# 5. ADD NUMBERS
print("\n===== ADD NUMBERS =====")
response = requests.get(
    BASE_URL + "/add",
    params={"num1": 10, "num2": 20}
)

if response.status_code == 200:
    print(response.json())
else:
    print("Request failed:", response.status_code)