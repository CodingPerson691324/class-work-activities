import random

class FruitQuiz:

    def __init__(self):

        self.fruits={'apple':'red','orange':'orange','watermelon':'green', 'banana':'yellow'}
    
    def quiz(self):
        while (True):

            fruit, color = random.choice(list(self.fruits.items()))

            print(f'what is the color of {fruit}')
            user_answer = input()

            if(user_answer.lower() == color):
                print('correct answer')
            else:
                print('wrong answer')

            option = int(input('wnter 0 if you want to play again other wise enter 1 : '))
            if(option):
                break

print('welcome to the fruit quiz')
fq = FruitQuiz()
fq.quiz()