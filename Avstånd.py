import math as m

x1 = float(input("x1: "))
y1 = float(input("y1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))

def avstånd(x1, y1, x2, y2):
    distance = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"avståndet mellan punkterna ({x1}, {y1}) och ({x2}, {y2}) är {distance}")
 
avstånd(x1, y1, x2, y2)