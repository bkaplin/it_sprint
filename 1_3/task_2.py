def check_word(word):
    letters = [elem for elem in word if elem != ' ']
    return letters == letters[::-1]


print(check_word(input('text to check: ')))
