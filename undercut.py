import random
class Person:
    def __init__(self,name) -> None:
        self.name = name
        self.score = 0 

    def incr_score(self):
        self.score += 1
    def get_zero(self):
        self.score = 0

    def get_score(self):
        return int(self.score)

    def __str__(self):
        return "%d: %s"%(self.score,self.name)

    def __repr__(self):
        return "{}"%(str(self)) 


class Computer(Person):
    def get_move(self):
        return int(random.randint(1,10))


class Humman(Person):
    def get_move(self):
        answer = input("say number:")
        return int(answer)
 


crash = Computer("crash")
print(crash)

sinan = Humman("sinan")
print(sinan)

def game_play():
    a = sinan.get_score()
    b = crash.get_score()
    while  a < 5 and b < 5 :
        score1 = sinan.get_move()
        score2 = crash.get_move()

        if score1 == score2 - 1:
            crash.incr_score()
            print("crash won")
            b += 1
            print("sinan:%d crash:%d"%(a,b))
            
        elif score2 == (score1 - 1):
            sinan.incr_score()
            print("sinan won")
            a += 1
            print("sinan:%d crash:%d"%(a,b))
             
        else:
            print("it is draw")
            print("sinan:%d crash:%d"%(a,b))
    
    if sinan.get_score() == 5:
        print ("result sinan won")
    else:
        print("result crash won")
    return sinan.get_zero(), crash.get_zero()

game_play()





