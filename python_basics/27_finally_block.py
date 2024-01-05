try:
    a = 20
    b = 10
    print(a/b)
except ZeroDivisionError:
    print("There is a divide by zero error")
finally:
    print("This will be execute no matter what")