from datetime import date
from utils import add, subtract, multiply, divide

print("Name: Md. Abrar Nawar")
print("Today's date:", date.today())

print("5 + 3 =", add(5, 3))
print("5 - 3 =", subtract(5, 3))
print("5 * 3 =", multiply(5, 3))
try:
    print("6 / 0 =", divide(6, 0))
except ValueError as error:
    print("Error:", error)