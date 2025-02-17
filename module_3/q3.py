"""Calculate the area and circumference of a circle given its radius."""

from math import pi, pow

PI = pi

radius = float(input("Enter the circle's radius: "))
area = PI * pow(radius, 2)
circumference = 2 * PI * radius

print(f"The area is {area}, and the circumeference is {circumference}")
