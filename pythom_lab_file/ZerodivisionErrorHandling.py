try:
    a = int(input("enter number:"))
    b = int(input("enter divisional number:"))
    result = a/b
    print(result)
except ZeroDivisionError:
    print("Cannot divide by Zero")    
