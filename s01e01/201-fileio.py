# File Operations

with open("animals.txt", 'r') as f:
    # text = f.read() # read whole file
    text = f.readlines()  # text becomes a list of lines

    print(type(text))
    print(text)

print("The End")
