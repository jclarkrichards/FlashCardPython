"""
Has raw format polish::english::#right::#wrong::lastval::streak::#decks-added::
'lastval' is 1 if got correct when seen last time.  -1 if got wrong when seen last time.
streak is how many times you got this word right or wrong in a row.
#decks-added is just how many times this word has been added to a deck.

"""

class Card(object):
    def __init__(self, rawgroup):
        self.raw = rawgroup
        self.parsegroup()

    def parsegroup(self):
        self.english = self.raw.split("::")[0]
        self.polish = self.raw.split("::")[1]
        self.right = int(self.raw.split("::")[2])
        self.wrong = int(self.raw.split("::")[3])
        self.lastval = int(self.raw.split("::")[4])
        self.streak = int(self.raw.split("::")[5])
        self.decks_added = int(self.raw.split("::")[6])
        self.lastdict = {1: 0.15, -1: -0.05}
        self.easing = 0.1
        

    def incrementRight(self):
        '''If getting a word right'''
        self.right += 1
        #if self.lastval == 1:#got it right last time
        self.streak += 1
        self.streak = min(self.streak, 10)#clamp to 10
        if self.lastval == 1:#Got it right last time as well
            self.easing += .1
            
        else:#Got it wrong last time
            self.easing += 0.05
        self.easing = min(self.easing, .5)
        self.lastval = 1
        self.regroup()

    def incrementWrong(self):
        '''if getting a word wrong'''
        self.wrong += 1
        #if self.lastval == -1:#got it wrong last time
        self.streak -= 2
        self.streak = max(self.streak, 0)#Clamp it
        if self.lastval == 1:#Got it right last time as well
            self.easing -= .1
            
        else:#Got it right last time
            self.easing -= 0.05
        self.easing = max(self.easing, .1)
        #else:
        #    self.streak = 1
        self.lastval = -1
        self.regroup()

    #def group(self, english, polish):
    #    return english+"::"+polish+"::0::0::0::0::0::\n"
        
    def regroup(self):
        self.raw = self.english+"::"+self.polish+"::"+str(self.right)+"::"+str(self.wrong)+"::"+str(self.lastval)+"::"+str(self.streak)+"::"+str(self.decks_added)+"::\n"

    def getLearnValue(self):
        '''learn value determines how well you know the word. Returns value between 0 and 1'''
        #val = (self.right / (self.right + self.wrong)) + 0.5 * (self.lastval) * self.streak
        #val = 0.05 + self.lastdict[self.lastval] * self.streak
        val = 0.05 + self.easing * self.streak
        val = min(val, 1)
        val = max(val, 0)
        return val
