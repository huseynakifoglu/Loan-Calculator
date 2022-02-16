vowels = 'aeiou'
# create your list here
inp = str(input())
vowels2 = []
for letters in inp:
    if letters in vowels:
        vowels2.append(letters)
print(vowels2)
