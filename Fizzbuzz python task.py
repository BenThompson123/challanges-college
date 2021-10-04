


def chat():
    engine = pyttsx3.init()
    engine.say("your text here")
    engine.runAndWait()

def fizzBuzz():
    for i in range(1,50):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzBuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
fizzBuzz()
