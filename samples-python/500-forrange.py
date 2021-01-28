# for in range

# Print numbers 20XX where XX is 1..20

for i in range(1, 21):
    print("20", f"{i:02d}", sep="")
    #           ^ formatting
    #              ^ variable/value to format
    #                ^^ 2 digits, with leading zero
    #                  ^ integer


