def capitalizeWords(words, func):
    for word in words:
        print(func(word))

words = ['ffgfdg','wef4g','f3rfas', 'gwersaa']

# The second parameter is the lambda expression
capitalizeWords(words, lambda word: word.upper())