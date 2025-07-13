class India():
    def capital(self):
        print('new delhi is the capital of india')
    def language(self):
        print('hindi is the most spoken language in india')
    def type(self):
        print('insdia is a developing country')

class USA():
    def capital(self):
        print('washington.d.c is the capital of USA')
    def language(self):
        print('english is the most spoken language in USA')
    def type(self):
        print('USA is a developed country')

obj_ind = India()
obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()