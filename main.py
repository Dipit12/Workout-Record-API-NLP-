import requests
from _datetime import datetime
#nutritionix part
api_key = "873affeb619174e70089116f87fa074e"
app_id = "b29823a9"

nutrionix_endpoint  = "https://trackapi.nutritionix.com//v2/natural/exercise"
parameters ={
    "query":input("Tell me which exercise you did today")
}
headers = {
    "x-app-id":app_id,
    "x-app-key": api_key
}
response = requests.post(url=nutrionix_endpoint,json=parameters,headers = headers)
data = response.text
print(data)

# sheety api
sheety_url = "https://api.sheety.co/5c397b0ad6da439c9c10e6368640f877/myWorkout/sheet1"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_input = {
        "workout":{
            "date":today_date,
            "time": now_time,
            "exercise":exercise["name"].title(),
            "duration":exercise["duration"],
            "calories":exercise["nf_calories"]
        }
    }
sheet_response = requests.post(url = sheety_url,json = sheet_input)
print(sheet_response.text)
