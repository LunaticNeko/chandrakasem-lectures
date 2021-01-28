# For-Each

# animals = ['Dog', 'Cat', 'Rabbit', 'Giraffe', 'Fish']

with open('animals.txt', 'r') as f:
    for animal in f:
        print(animal.strip())
