text = str(input())
digits = [int(x) for x in text]
odds = []

for digit in digits:
    if digit % 2 != 0:
        odds.append(digit)

print(odds)
