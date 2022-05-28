class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = list(tracks)
        self.score = float(score)
       
    def change_age(self, change_age):
	    self.change_age = change_age
	    print("Age was changed from",self.age," to ", self.change_age)

    def change_name(self, change_name):
	    self.change_name = change_name
	    print("The Name was changed from ",self.name," to ", change_name)

    def add_track(self,add_track):
	    self.add_track = add_track
	    print("Track was changed from ", self.tracks, " to ", add_track)

    def get_score(self,get_score):
        self.get_score = get_score
        print ("This is your Score ", get_score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score(Bob.score)
