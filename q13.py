"""Reads a temperature and outputs the probable season."""

temp = int(input("Enter a temperature: "))
probable_weather = ""

if temp > 110 or temp < -5:
    print("The temperature entered is outside the valid range.")
    quit()

if temp >= 90:
    probable_weather = "summer"
elif temp >= 70:
    probable_weather = "spring"
elif temp >= 50:
    probable_weather = "fall"
else:
    probable_weather = "winter"

print(f"The probable weather is {probable_weather}.")
