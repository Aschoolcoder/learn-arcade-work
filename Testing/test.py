temperature = input("What is the temperature in Fahrenheit? ")
# Convert the input to an integer
temperature = int(temperature)
x = 0

# Do our comparison
if temperature == 44:
    print("correct!!!")
    x += 1
else:
    print("imagine not knowing the temperature on the 2nd of november at 8:24 in the morning.")

rich = input("who is the richest person in the world? ")

if rich == "Jeff Bezos":
    print("correct!")
    x += 1
else:
    print("you are wrong :(")
quadratic_answer = input("what is the answer for the quadratic equation 0 = 8x^2 + 6x + 1? ")

if quadratic_answer == "- 1/2 and -1/4":
    print("Correct!!!!!!!")
    x += 1
else:
    print("Incorrect :(")
trick_question = input("is the answer to this question a, b, or c? ")

if trick_question == "d":
    print("Correct, how did you know????")
    x += 1
else:
    print("the answer was d :')")
quiz = input("Did you enjoy this quiz? ")

if quiz == "yes":
    print("correct >:)")
    x += 1
else:
    print("false, this quiz was the best >:)")

print("your score is", x, "out of 5")
