try:
    numerator = 10
    denominator = 1
    dividedAnswer = numerator / denominator
    print(dividedAnswer)
    newnum = int(input("Enter a new number"))
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except:
    print("The entered number is invalid")
else:
    print("Everything went good.")
finally:
    print("The code reaches its end.")