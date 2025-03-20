#input a word
text = str(input('enter a string: '))
#reverse a string
revText = text[::-1]
print(f'the reverse of {text} is {revText}')
#lower text
lowerText = text.lower()
print(f'the lowercase of {text} is {lowerText}')
#uppercase text
upperText = text.upper()
print(f'the uppercase of {text} is {upperText}')
#findtext
findText = text.find('Jay')
print(findText)


