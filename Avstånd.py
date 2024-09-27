import math as m

cords=[]
cordsString= input("Ange i formatet: x,x y,y x,x y,y : ")
cords = cordsString.split()

x1 = float(cords[0])
y1 = float(cords[1])
x2 = float(cords[2])
y2 = float(cords[3])

def avstånd(x1, y1, x2, y2):
    distance = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"avståndet mellan punkterna ({x1}, {y1}) och ({x2}, {y2}) är {distance}")


if len(cords) == 4:
    avstånd(x1, y1, x2, y2)
else:
    print("try again!")


