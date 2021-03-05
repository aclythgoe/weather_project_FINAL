#Import necessary tools 
import time
import requests


#Import Requests for weather API and JSON 
import requests
import json



#Make class named 'WeatherInformation'
class WeatherInformation:
    # Def __init__ and get inputs
    def __init__(self, zip_code, city_name, forecast):
        #Initialize Zip_code and give the inputs
        self.zip_code = zip_code
        self.city_name = city_name
        self.forecast = forecast
    
    #Get weather based on city name.
    def get_weather_cityname(self):
        self.city_name = input("\nPlease enter the name of your city: ")
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=8ba60d976d201bf3f8c60673f08ca278'.format(self.city_name)
        self.forecast = requests.get(url)

         #Connection Test
        if self.forecast.status_code == 200:
            print("\nConnection Succesful!")
        else: 
            print("!!! Error: Please check your spelling. !!!")
        

    # Get weather based on zip code.
    def get_weather_zip(self):
        self.zip_code = input("\nPlease enter your zip code: ")
        url = 'https://api.openweathermap.org/data/2.5/weather?zip={},us&units=imperial&APPID=8ba60d976d201bf3f8c60673f08ca278'.format(self.zip_code)
        self.forecast = requests.get(url)

         #Connection Test
        if self.forecast.status_code == 200:
            print("\nConnection Succesful!")
        else: 
            print("!!! Error: Please check your Zip Code. !!!")
        
    #Display the weather to the user.
    def display_weather(self):
        #Get JSON ready to grab specific key and value's from JSON data
        #If error arises, dismiss error messages, as error is addressed above in connection test.
        try:
            X = self.forecast.json()
            Y = X['main']
            wind = self.forecast.json()
            wind_data = wind['wind']


            #Define calls for each data set
            temp = Y['temp']
            feels = Y['feels_like']
            high = Y['temp_max']
            low = Y['temp_min']
            humidity = Y['humidity']
            wind = wind_data['speed']


            #Print output to user, displaying all information.
            print(f"\nThanks! Your forecast brought to you by Andrew:")
            print(f"\tTemperature: {temp}°F")
            print(f"\tFeels like: {feels}°F")
            print(f"\tToday's High: {high}°F")
            print(f"\tToday's low: {low}°F")
            print(f"\tWind: {wind} MPH")
            print(f"\tHumidity: {humidity}%")
        except:
            pass
        
#Starting the program.
print("\nPress 'q' at any time to quit")
start = input("\n\033[4mWelcome to the Daily Forecast! To start, please type 'start'\033[0m ")

while True:
    if start == 'start':
        active = True
        break
    elif start == 'q':
        active = False
        break
    else:
        print ("\nERROR: Try again, 'start' is case sensitive.")
        break

while active:
        #Instantiate class
        w = WeatherInformation('','','')
        
        #Ask the user if they want to search on city name or zip.
        print("Would you like to search by:")
        print("\t 1) Zip Code")
        print("\t 2) City Name")
        answer = input("\tType number here: ")

        if answer == '1':
            w.get_weather_zip()
            w.display_weather()
        elif answer == '2':
            w.get_weather_cityname()
            w.display_weather()
        elif answer == 'q':
            break
        else:
            print("!!! ERROR: Enter your choice in number format. (eg. 1 or 2) !!!")
        #Ask the user if they would like to try again. 
        again = input("\nWould you like to try again? (y/n) ".lower())
        if again == 'n' or again == 'no' or again == 'q':
            print("Thank you for using this tool!")
            print("Shutting down...")
            time.sleep(3)
            print("Shutdown succesful.")
            break  
