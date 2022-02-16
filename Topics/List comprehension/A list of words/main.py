# work with the preset variable `words`
new_list = [word for word in words if str(word).startswith('a') or str(word).startswith('A')]
print(new_list)
