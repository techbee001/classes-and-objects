class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float):
        self.name:str = name
        self.age:int = age
        self.tracks:list = tracks
        self.score:float = score

    def change_name(self, name):
         self.name = name
         # print('Name have been changed!!!')

    def change_age(self, age: int):
         if type(age) == int:
             self.age:int = age
             # print('Age have been changed!!!')
         else:
             print('Error!!! Age must be an Integer')
             return
    def add_track(self, track):
          self.tracks.append(track)
         # print('Track have be added!!!')
    def get_score(self):
         return self.score
         
Bob =Student (name="Bob", age=26, tracks=["FE","BE"], score=20.00)

print(Bob.name)
# Expected methods
Bob.change_name("peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()


print(Bob.name)














