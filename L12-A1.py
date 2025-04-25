#take input as a word
string = input('please enter a word: ')
#take input of a character
char = input('please enter a character: ')
i = 0
count = 0
#loop to find the occurence of a character
while i < len(string):
    if string[i] == char:
        count = count + 1
    i = i + 1
#display the result
print('the total number of times this',char,'has occured is:',count)