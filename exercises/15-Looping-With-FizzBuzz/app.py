def fizz_buzz():
    # ✅↓ Write your code here ↓✅
    j = 0 
    for i in range(100):
        j += 1
        if (j % 3 == 0) and (j % 5 == 0):
             print("FizzBuzz")
        elif j % 3 == 0:
            print("Fizz")
        elif j % 5 == 0:
            print("Buzz")
        else :
            print(j)
        


# ❌↓ DON'T CHANGE THE CODE BELOW ↓❌
fizz_buzz()
