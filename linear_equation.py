y1 = None
y2 = None
x1 = None
x2 = None
k = None

#input
y1 = int(input("first y coordenate: "))
x1 = int(input("first x coordenate: "))
y2 = int(input("second y coordenate: "))
x2 = int(input("second x coordenate: "))

def calculate_k(y1, y2, x1, x2):
    global k
    k = (y2 - y1) / (x2 - x1)

calculate_k(y1, y2, x1, x2)
print("K is: "+ str(k))