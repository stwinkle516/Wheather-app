import json,requests
def get_weather_data(city):
    url=f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a9fa45d619b60ef6244f6454d11d8988&units=metric'
    http_str=requests.get(url).text
    json_data=json.loads(http_str)
    final_data={}
    final_data["temp"]=json_data["main"]["temp"]
    final_data["pressure"]=json_data["main"]["pressure"]
    final_data["humidity"]=json_data["main"]["humidity"]
    final_data["wind"]=json_data["wind"]["speed"]
    final_data["Haze"]=json_data["weather"][0]["main"]
    final_data["city"]=json_data["name"]
    final_data["country"]=json_data["sys"]["country"]

    print("final_data---->",final_data)
    return final_data
