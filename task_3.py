import requests
import datetime
import json

city = str(input("Пожалуйста, введите город :"))
number_of_days = int(input("Введите количество дней :"))


def get_data():
    received_data = requests.get("https://api.openweathermap.org/data/2.5/forecast/daily?"
                                 f"q={city}&cnt={number_of_days}&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8")
    return received_data.json()

def getting_data() ->list:
    weather_data = get_data()
    result = []
    for day in weather_data["list"]:
        today = []
        if len(str(day["dt"])) > 9:
            full_date = datetime.datetime.fromtimestamp(day["dt"])
            date = full_date.strftime("%d-%m-%Y")
            today.append(date)
        today.append(str(day["temp"]["day"]))
        today.append(str(day["feels_like"]["day"]))
        today.append(str(day["temp"]["night"]))
        result.append(today)
    return result


def user_name(value):
    insert_for_name = get_data()
    transformation = datetime.datetime.fromtimestamp(insert_for_name['list'][0]["dt"])
    date = transformation.strftime("%d-%m-%Y")
    verified_name = "".join(str(date) + "-" + str(insert_for_name["city"]["name"]) + "-" + str(insert_for_name["cnt"]))
    return verified_name


def save_name(filename):
    with open(f"{filename}-days-weather-forecast.txt", "w") as file:
        new_data = getting_data()
        for day_data in new_data:
            for i, val in enumerate(day_data):
                day_data[i] = val.ljust(20)
            file.write("".join(day_data) + "\n")

def main():
    data = get_data()
    name = user_name(data)
    save_name(name)


main()