# Project: Temperature and Windspeed
# Created by: Umair
# Created on: Oct 21, 2021
# This program will ask the user to input temperature and windspeed and it will output wether its hot or cold and wether its windy or not windy

# Asks the user to input the temperature
temperature = (input("Enter the temperature in celcius: "))
# Asks the user to input the wind speed
wind_speed = (input("\nEnter the wind speed in km: "))

# Runs the .isdecimal() function on temperature and wind_speed to check if its a whole integer
if (temperature.isdecimal() and wind_speed.isdecimal()):

# Checks to see if temperature is greater than 25 and wind_speed is greater than 19
# if it returns True, "The day is hot and windy" will be printed
    if (int(temperature) >= 25 and int(wind_speed) >= 19):
        print("\nThe day is hot and windy")

# Checks to see if temperature is greater than 25 and wind_speed is not greater than 19
# if it returns True, "The day is hot and not windy" will be printed
    elif (int(temperature) >= 25 and int(wind_speed) < 19):
        print("\nThe day is hot and not windy")

# Checks to see if temperature is not greater than 25 and wind_speed is greater than 19
# if it returns True, "The day is not hot and windy" will be printed
    elif (int(temperature) < 25 and int(wind_speed) >= 19):
        print("\nThe day is cold and windy")

# Checks to see if temperature is not greater than 25 and wind_speed is greater than 19
# if it returns True, "The day is not hot and windy" will be printed
    elif (int(temperature) < 25 and int(wind_speed) < 19):
        print("\nThe day is cold and not windy")

else: 
    print("\nInvalid Entry")

