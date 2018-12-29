################################
#
#  Simple Python Bowling Game
#
################################

class bowlingGame():

    def __init__(self):
        self.start()
        
    def roll(self, *args):
        if args:
            for pinDown in args: 
                if type(pinDown) == int and pinDown >= 0 and pinDown <= 10:
                    self.makeOneRoll(pinDown)
                else:
                    print("You can't possibly knock '"+str(pinDown)+"' pin(s) down. Try again!")
        else:
            print("You forgot to make a roll. Please try again and knock some pins down!")
        
    def makeOneRoll(self,pinDown):
        frameIndex = self.frame-1
        self.everyRollScoreList.append(pinDown)
        self.addScoreToPreviousFrames(pinDown)
            
        if self.rollNum == 1:
            self.frameScore = pinDown
            self.recordScore(frameIndex)
            self.rollNum +=1
            if self.allPinsDown():
                print("STRIKE! on frame %i" % self.frame)
                self.framesToAddScoreTo += [frameIndex,frameIndex]
                if self.notLastFrame(): self.startNewFrame()
                
        else: # 2nd roll in frame
            self.frameScore += pinDown
            self.recordScore(frameIndex)
            if self.allPinsDown():
                print("SPARE! on frame %i" % self.frame)
                self.framesToAddScoreTo.append(frameIndex)
            if self.notLastFrame(): self.startNewFrame()
            else:
                # continue to increment rollNum only for 10th Frame
                if self.rollNum < 3: self.rollNum += 1
        #self.printCurrentState()
    
    def start(self):
        self.frameScoreList= [0 for i in range(10)]
        self.everyRollScoreList=[]
        self.framesToAddScoreTo = []
        self.frame = 1
        self.rollNum = 1
        print ("Started a New Bowling Game!! ")
        # self.printCurrentState()
    
    def startNewFrame(self):
        self.frame += 1
        self.rollNum = 1
    
    def recordScore(self, frame):
        self.frameScoreList[frame] = self.frameScore
        
    def allPinsDown(self):
        return self.frameScore == 10
        
    def notLastFrame(self): 
        return (self.frame < 10)
                    
    def addScoreToPreviousFrames(self, pinDown):
        if len(self.framesToAddScoreTo) == 1:
            self.addExtraScore(pinDown)
        elif len(self.framesToAddScoreTo) >= 2:
            scoreAddedFrame = self.addExtraScore(pinDown)
            if self.framesToAddScoreTo[0] != scoreAddedFrame:
                self.addExtraScore(pinDown)
            
    def addExtraScore(self,pinDown):
        frameIndexToAddScore = self.framesToAddScoreTo.pop(0)
        self.frameScoreList[frameIndexToAddScore] += pinDown
        return frameIndexToAddScore
    
    def getTotalScore(self):
        totalScore = 0
        for frameScore in self.frameScoreList:
            totalScore += frameScore
        return totalScore
        
    def printRolls(self):
        print("All rolls: " + str(self.everyRollScoreList))
        
    def printScores(self):
        print("Scores per Frame: " + str(self.frameScoreList))
        
    def printTotalScore(self):
        print("Total Score: " + str(self.getTotalScore()))
        
    def printCurrentState(self):
        print("----------------------")
        print("Frame Number %i" % self.frame)
        print("Roll Number %i" % self.rollNum)
        self.printScores()
        self.printTotalScore()
        print("----------------------")

def printTestTitle(title):
    print()
    print("=============================================================================")
    print(title)
    print("=============================================================================")

def test_firstRollInGame():
    printTestTitle("Tests all possible first roll of game (knock down 0-10 pins)")
    game = bowlingGame()
    for pinDown in range(11): #0-10
        game.start()
        game.roll(pinDown)
        assert (game.frameScoreList[0] == pinDown), "Score in first roll is not correct"
        if (pinDown != 10):
            assert (game.frame == 1), "Should still be in frame 1"
            assert (game.rollNum == 2), "Second Roll should be available for frame"
        else:
            assert (game.frame == 2), "Should be in frame 2"
            assert (game.rollNum == 1), "Should be first roll in frame 2"
    
def test_strikeFrame():
    printTestTitle("Tests strike frame (frame 1) will add the next two scores")
    game = bowlingGame()
    for pinDown in [10,5,5,3]:
        game.roll(pinDown)
    game.printRolls()
    game.printCurrentState()
    assert (game.frameScoreList[0] == 20), "Frame 1 Score is not correct"
    printTestTitle("Tests strike frame (frame 2) will add the next two scores")
    game = bowlingGame()
    for pinDown in [10,10,5,3,8]:
        game.roll(pinDown)
    game.printRolls()
    game.printCurrentState()
    assert (game.frameScoreList[1] == 18), "Frame 2 Score is not correct"
    
def test_spareFrame():
    printTestTitle("Tests spare frame (frame 1) will add the next two scores")
    game = bowlingGame()
    game.roll(8,2,5,4)
    game.printRolls()
    game.printCurrentState()
    assert (game.frameScoreList[0] == 15), "Frame 1 Score is not correct"
    
    printTestTitle("Tests spare frame (frame 2) will add the next two scores")
    game = bowlingGame()
    game.roll(10,5,5,7,3)
    game.printRolls()
    game.printCurrentState()
    assert (game.frameScoreList[1] == 17), "Frame 2 Score is not correct"
    
def test_perfectGame():
    printTestTitle("Tests getting a perfect game with perfect score")
    game = bowlingGame()
    for i in range(12):
        game.roll(10)
    game.printCurrentState()
    assert (game.getTotalScore() == 300), "Total Score for game is not correct"

def test_spareInTenth():
    printTestTitle("Tests getting a spare in tenth frame with extra roll")
    game = bowlingGame()
    for i in range(9):
        game.roll(10)
    game.roll(7,3,5)
    game.printRolls()
    game.printCurrentState()
    assert (game.getTotalScore() == 272), "Total Score for game is not correct"
    
def test_mixOfEverything():
    printTestTitle("Tests getting a mix of spares, strikes, and normal rolls with no extra roll in tenth frame")
    game = bowlingGame()
    for pinDown in [10,5,3,7,3,4,5,8,2,9,0,7,3,10,6,2,8,0]:
        game.roll(pinDown)
    game.printRolls()
    game.printCurrentState()
    assert (game.getTotalScore() == 131), "Total Score for game is not correct"

def test_invalidRolls():
    printTestTitle("Tests some invalid rolls: 11, -1, 'abc', or empty roll")
    game = bowlingGame()
    for pinDown in [11,-1,'abc']:
        game.roll(pinDown)
        # roll should not have counted
        assert (game.frame == 1), "Should still be in frame 1"
        assert (game.rollNum == 1), "Should be first roll in frame 2"
        assert (game.getTotalScore() == 0), "Total Score should remain at 0"
    game.roll()
    assert (game.frame == 1), "Should still be in frame 1"
    assert (game.rollNum == 1), "Should be first roll in frame 2"
    assert (game.getTotalScore() == 0), "Total Score should remain at 0"
    game.printRolls()
    game.printCurrentState()