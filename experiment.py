from input_recognition import InputRecognition
input_recognition = InputRecognition()
input_recognition.run_input()

x1 = None
x2 = None
y1 = None
y2 = None
myVar = {

}

myVar = input_recognition.return_my_polymonial()

print("")
print("--- 2-point Equation ---")
print("Use the index for any monomonial you've assigned,")
print("monomonials containing a variable will be rejected")
print("Your polymonials:")
print(myVar)
indx_x1 = int(input("Point x1: "))
indx_x2 = int(input("Point x2: "))
indx_y1 = int(input("Point y1: "))
indx_y2 = int(input("Point y2: "))


def update_2p(indx_x1, indx_x2, indx_y1, indx_y2):
    global x1
    global x2
    global y1
    global y2
    x1 = myVar[indx_x1][0]
    x2 = myVar[indx_x2][0]
    y1 = myVar[indx_y1][0]
    y2 = myVar[indx_y2][0]

print(x1)
print(x2)
print(y1)
print(y2)
print("------")
update_2p(indx_x1, indx_x2, indx_y1, indx_y2)
print(x1)
print(x2)
print(y1)
print(y2)
print("------")

def my_2p_equation(x1, x2, y1, y2):

    if all(var is not None for var in [x1, x2, y1, y2]):
        try:
            k = ( int(y2) - int(y1)) / ( int(x2) - int(x1))
            print("k value for 2p equation is: "+ str(k))
        except ZeroDivisionError:
            print("k value for 2p equation is: 0")
    else:
        print("error: either of the point(s) are unassigned")

my_2p_equation(x1, x2, y1, y2)