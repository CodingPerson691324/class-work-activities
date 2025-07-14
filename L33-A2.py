class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        return self.word+' ( '+self.meaning+' )'
    
flash = []
print('welcome to flaschard application')

while(True):
    word = input('enjter the name of the woreds u want to add to ur flashcard')
    meaning = input('enter the meaning of the word: ')
    obj = flashcard(word, meaning)
    flash.append(obj)
    option = int(input('enter 0 if you want to add another word to your flashcard and one if you want to view it'))

    if(option):
        break

print('\nYor flashcard')
for i in flash:
    print('>', i)