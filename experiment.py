from input_recognition import InputRecognition
input_recognition = InputRecognition()
input_recognition.run_input()

myVar = {

}

myVar = input_recognition.return_my_polymonial()

if len(myVar) == 0:
    print("no numbers given, please try again")
else:
    for i in range(len(myVar)):
        print('option '+ str(i)+': '+ str(myVar[i][0]))

x1 = int(input("x1: "))
x2 = int(input("x2: "))
y1 = int(input("y1: "))
y2 = int(input("y2: "))