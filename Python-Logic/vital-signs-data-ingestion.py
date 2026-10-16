#Program developed by Sam Espana
#Program enhanced by Blong Lor
#Date:

from datetime import date

today = date.today()
#string formatfor date showing month, day, and year
d2 = today.strftime("%B %d, %Y")
print("d2 = ", d2)
#INPUTS
print("\nVital Signs Program\n")
strFirst = input("Enter first name: ")
strLast = input("Enter last name: ")
fltFahrenheit = float(input("Enter temperature in Fahrenheit degrees: "))
intPulse = int(input("Enter pulse/minute: "))
intRespiration = int(input("Enter breaths/minute: "))
strBloodPressure = input("Enter blood pressure (Systolic/Diastolic): ")

#PROCESSING-CALCULATIONS
print("\nCalculating Celsius \n")
fltCelsius = (fltFahrenheit - 32)/1.8 #Converting Fahrenheit to Celcius

#OUTPUTS
print("Vital Signs Report\n")
print("Welcome "+strFirst+" "+strLast)
print("Temperature in Fahrenheit degrees =", fltFahrenheit)
print("Temperature in Celcius degrees = %.2f " %fltCelsius)
print("Pulse/minute =", intPulse)
print("Respiration/minute =", intRespiration)
print("Blood Pressure (Systolic/Diastolic) =", strBloodPressure)

print("\nBlong Lor")
