import requests
import  datetime
nutritionix_app_id = "65bb434c"

nutritionix_api_key = "4b623d2fcee2782b320e6e3fd3fd47a0"

endpoint = " https://trackapi.nutritionix.com/v2/natural/exercise"

nlp_exercise_end_point = f"{endpoint}"

GENDER = "Female"
WEIGHT_KG = 80
HEIGHT_CM = 165
AGE = 19
headers = {
    "x-app-id" : nutritionix_app_id,
    "x-app-key" : nutritionix_api_key,
    "x-remote-user-id" : "0"
}
#
params = {
    "query" : input("What exercises you've completed Today?\n"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
#
response = requests.post(url=nlp_exercise_end_point,headers=headers,json=params)
response = response.json()


date = datetime.datetime.now().strftime("%x")
time = datetime.datetime.now().strftime("%X")

header = {
    "Authorization" : "Bearer nkbdjwqhiue1u23h4jkdasbnkfjqf"
}

for exercise in response["exercises"] :
    sheety_api_endpoint = "https://api.sheety.co/6d265cf17d9cad6aa4d01c8acd566dc2/workOutLogger/workouts"
    params = {
        "workout" :
            {
        "date" : date,
        "time" : time,
        "exercise" : exercise["name"],
        "duration" : exercise["duration_min"],
        "calories" : exercise["nf_calories"]
            }
    }
    response = requests.post(url=sheety_api_endpoint,json=params,headers=header)
    print(response.text)

