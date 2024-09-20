#How to raise an exception
def height_discrimination(gender, height):
    if height < 0:
        raise ValueError("height must be greater than zero")
        
    if gender == "male" and height >= 180:
        print("OK")
    elif gender == "male" and height < 180:
        print("Short Man")
    elif gender == "female":
        print("No Problem")

#How to handle an exception
def safe_division(a, d):
    try:
        return a / d
    except ZeroDivisionError:
        return a / 1
    except TypeError:
        print("Cannot divide a non-number!")
        return

#height_discrimination("male", -9)
        
print(safe_division(9,9))
print(safe_division(9,3))
print(safe_division(9,0))
print(safe_division("5",2))
