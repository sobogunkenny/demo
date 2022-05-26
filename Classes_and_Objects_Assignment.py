class Student:
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score
        
    def change_name(self, n):
        self.name = n
        return self.name
    
    def change_age(self, a):
        self.age = a
        return self.age
    
    def add_track(self, t):
        self.tracks = t
        return self.tracks
    
    def get_score(self):
        return self.score
        
        
"""
Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)
#Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
"""
        
  
        



