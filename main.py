import requests
import json
from builtins import int

class Request1:
    def __init__(self, amount, category, difficulty, type):
        self.amount = amount
        self.category = category
        self.difficulty = difficulty
        self.type = type    
        
    def typeSelect(self):
        typeList = {1:'Any', 2:'Multiple Choice', 3:'True/False'}
        
        #multiple or boolean
        
        for key, value in typeList.items():
            print(key,":" , value)
                
        self.type = int(input('Input ONE index number corresponding to the difficulty above [1 to 3]: '))
        
        if type(self.type) != int:
            print('Only numbers are allowed!')
            self.typeSelect()
        elif self.type > 3:
            print('Number larger than 3 is not allowed!')
            self.typeSelect()
        elif self.type < 1:
            print('Number smaller than 1 is not allowed!')
            self.typeSelect()
        elif self.type >= 1 and self.type <= 3:
            if self.type == 2:
                self.type = 'multiple'
            elif self.type == 3:
                self.type = 'boolean'
            else:
                return True
        else:
            print('Invalid response. Only numbers are allowed!')
            self.typeSelect()  
    
    def difficultySelect(self):
        difficultyList = {1:'Any', 2:'easy', 3:'medium', 4:'hard'}
        
        for key, value in difficultyList.items():
            print(key,":" , value)
        
        self.difficulty = int(input('Input ONE index number corresponding to the difficulty above [1 to 4]: '))
        if type(self.difficulty) != int:
            print('Only numbers are allowed!')
            self.difficultySelect()
        elif self.difficulty > 4:
            print('Number larger than 4 is not allowed!')
            self.difficultySelect()
        elif self.difficulty < 1:
            print('Number smaller than 1 is not allowed!')
            self.difficultySelect()
        elif self.difficulty >= 1 and self.difficulty <= 4:
            self.difficulty = difficultyList[self.difficulty]
            self.typeSelect()
        else:
            print('Invalid response. Only numbers are allowed!')
            self.difficultySelect()    
    
    def categorySelect(self):
        categoryList = {8:"Any", 9:"General Knowledge",10:"Entertainment: Books",11:"Entertainment: Film",12:"Entertainment: Music",13:"Entertainment: Musicals & Theatres",14:"Entertainment: Television",15:"Entertainment: Video Games",16:"Entertainment: Board Games",17:"Science & Nature",18:"Science: Computers",19:"Science: Mathematics",20:"Mythology",21:"Sports",22:"Geography",23:"History",24:"Politics",25:"Art",26:"Celebrities",27:"Animals",28:"Vehicles",29:"Entertainment: Comics",30:"Science: Gadgets",31:"Entertainment: Japanese Anime & Manga",32:"Entertainment: Cartoon & Animations"}
        
        for key, value in categoryList.items():
            print(key,":" , value)
        
        self.category = int(input('Input ONE index number corresponding to the categories above [8 to 32]: '))
        
        if type(self.category) != int:
            print('Only numbers are allowed!')
            self.categorySelect()
        elif self.category > 32:
            print('Number larger than 32 is not allowed!')
            self.categorySelect()
        elif self.category < 9:
            print('Number smaller than 8 is not allowed!')
            self.categorySelect()
        elif self.category >= 8 and self.category <= 32:
            self.difficultySelect()
        else:
            print('Invalid response. Only numbers are allowed!')
            self.categorySelect()    
    
    def QuestionsCount(self):
        self.amount = int(input('Input the number of questions (max 10) that you want: '))
        if type(self.amount) != int:
            print('Only numbers are allowed!')
            self.QuestionsCount()
        elif self.amount > 10:
            print('Number larger than 10 is not allowed!')
            self.QuestionsCount()
        elif self.amount < 1:
            print('Number smaller than 1 is not allowed!')
            self.QuestionsCount()
        elif self.amount >= 1 and self.amount <= 10:
            self.categorySelect()
        else:
            print('Invalid response. Only numbers are allowed!')
            self.QuestionsCount()
               
    def MakeRequest(self):
        payload = {'amount': self.amount, 'category': self.category, 'difficulty': self.difficulty, 'type': self.type}
        
        if self.type == 1:
            del payload['type']

        if self.difficulty == 'Any':
            del payload['difficulty']

        url = 'https://opentdb.com/api.php'

        self.r = requests.get(url, params=payload)
     
        self.raw_results = self.r.json()
        
        self.response_code = self.raw_results['response_code']
        self.results = self.raw_results['results']
        
        print(self.response_code)
        
        if self.response_code == 1:
            print("No Results Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20)")
        
        for i in self.results:
            print()
            for k, v in i.items():
                print(k, ":", v)
        

x = Request1(0, 0, 0, 0)
x.QuestionsCount()
x.MakeRequest()

