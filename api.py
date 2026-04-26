#Import library to send requests to API
import requests
#Step 1:Store API key
API_KEY="976ef3362386e35e5cca0e92a7aceb83"
#Step 2:Ask user to enter city name
city=input("Enter city name: ")
#Step 3:Create API url
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
#step 4: Send request to API
response=requests.get(url)
#step 5:covert response into json
data=response.json()
print(data)
#step 6: Check if city exists
if data["cod"]!=404:

    #Extract main weather data
    main=data["main"]

    #Extract weather description
    weather_data=data["weather"][0]

    #get individual values
    temperature=main["temp"]
    humidity=main["humidity"]
    pressure=main["pressure"]
    description=weather_data["description"]

    #step 7: Print weather details
    print("Weather Details:")
    print("City:", city)
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Description: {description}")
else:
    print("City not found")