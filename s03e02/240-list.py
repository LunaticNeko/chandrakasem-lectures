scores = [10, 4, 2, 8, 7, 8, 9, 5]
'''
print("Printing")
print(scores)

print("Indexing")
print(scores[0])
print(scores[1])
try:
    print(scores[999])
except IndexError:
    pass
print(scores[-1])
print(scores[-2])
print(scores[-3])

print("Slicing")
print(scores[4:6])
print(scores[:6])
print(scores[6:])
'''

print(f"list length = {len(scores)}")
print(sum(scores)/len(scores))
