#define the base class Player
class Player:
  def play(self):
    print("The player is playing cricket.")
#define the derived class Batsman
class Batsman(Player):
  def play(self):
    print("The batsman is batting.")
#define the derived class Bowler
class Bowler(Player):
  def play(self):
    print("The bowler is bowling")
#create object of batsman and bowler class
batsman=Batsman()
bowler=Bowler()
#call the play() method for each object
batsman.play()
bowler.play()