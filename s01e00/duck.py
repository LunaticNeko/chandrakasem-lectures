class Duck:
    color = ""
    weight = 0
    def quack(self):
        print("QUACK!")

D = Duck()

D.color = "white"
D.weight = 20

print(D.color, D.weight)
D.quack()

