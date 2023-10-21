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
print("Use the index for any value you've assigned,")
print("values containing a variable will be rejected")
print("Your values:")
print(myVar)
x1 = int(input("Point x1: "))
x2 = int(input("Point x2: "))
y1 = int(input("Point y1: "))
y2 = int(input("Point y2: "))
print('------')

def my_2p_equation(x1, x2, y1, y2):
    if all(var is not None for var in [x1, x2, y1, y2]):
        k = ( y2 - y1) / ( x2 - x1)
        print("k value for 2p equation is: "+ str(k))
    else:
        print("error: either of the point(s) are unassigned")

my_2p_equation(x1, x2, y1, y2)