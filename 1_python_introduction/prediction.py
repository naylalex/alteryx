import random
lower_threshold = 1 
upper_threshold = 100
device_reading = random.randint(lower_threshold, upper_threshold)
prediction = 0
while prediction != device_reading:
    prediction = int(input("What is your prediction? [{},{}]? ".format(lower_threshold, upper_threshold)))
    if prediction > 0:
        #Hint the user
        if prediction > device_reading:
            print("Prediction larger than device reading. Try again.")
        else:
            print("Predition lower than device reading. Try again.")

    else:
        print("Ciao!")
        break
else:
    print("Your prediction was correct!")