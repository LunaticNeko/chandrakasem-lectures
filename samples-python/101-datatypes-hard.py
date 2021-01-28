# Int and Float

x = 100
y = 22.4

xpx = x+x
xpy = x+y

# print(type(xpx), xpx)
# print(type(xpy), xpy)

very_large_number = 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890
very_large_float = float(very_large_number)
back_to_int = int(very_large_float)

# print(type(very_large_number), very_large_number)
# print(type(very_large_float), very_large_float)
# print(type(back_to_int), back_to_int)

# Addressing

S1 = "This is a sentence."
#     0123456789012345678

# print(S1[0])
# print(S1[9])
# print(S1[16])
# print(S1[0:5])
# print(S1[7:])
# print(S1[:12])

L = ['Dog', "Cat", 'Rabbit']
M = ['Horse', 'Deer']

# print(type(L))
# print(L[0])  # show value of item 0 in list L

L[0] = "Giraffe"

print(L + M)

# print(L)

T1 = (202, "Second Floor Office")
T2 = (201, "Technician Office")
T3 = (101, "Secretary Office")

# print(type(T1))

print(T1 + T2)

# T1[1] = "DANCE FLOOR"  # <== Will cause error
T1 = (202, "DANCE FLOOR")
print(T1)


Z = "LOD Monitor User Guide"

# Z[1] = 'C'  # <== Will cause error

Z = "LCD Monitor User Guide"

print(Z)
