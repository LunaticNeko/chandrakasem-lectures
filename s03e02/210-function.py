def oddeven(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"
    
def squaresize(w):
    return w**2

def twotimes(s):
    return 2*s

def result(home_score, away_score):
    if home_score > away_score:
        return f"Home Team Win {home_score} - {away_score}"
    elif home_score < away_score:
        return f"Away Team Win {home_score} - {away_score}"
    else:
        return f"Tie {home_score} - {away_score}"
    
def hello(name):
    print("hello", name)

print(oddeven(10))
print(squaresize(19))
print(result(0, 3))
print(result(7, 0))
print(result(2, 2))
hello("a")