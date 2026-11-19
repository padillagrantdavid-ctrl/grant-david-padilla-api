import requests

url = "https://prince-act5-1.onrender.com/ENDPOINT"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("\n===== CLASSMATE API RESULT =====")

    for key, value in data.items():
        print(key, ":", value)

else:
    print("Request failed.")