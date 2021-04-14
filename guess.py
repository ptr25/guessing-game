number = 25
inputNo = int(input("Guess the number"))
if(inputNo<number):
    print("Guess a number higher than ")
elif(inputNo>number):
    print("Guess a number lower than " + inputNo)
else:
    print("You got it right")
