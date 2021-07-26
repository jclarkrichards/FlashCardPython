"""
Has format polish::english::last::#right::#wrong::
'last' is 1 if got correct when seen last time.  0 if got wrong when seen last time.
 

"""

class WordGroup(object):
    def __init__(self, rawgroup):
        self.raw = rawgroup
        self.parsegroup()

    def parsegroup(self):
        self.polish = self.raw.split("::")[0]
        self.english = self.raw.split("::")[1]
        self.last = int(self.raw.split("::")[2])
        self.right = int(self.raw.split("::")[3])
        self.wrong = int(self.raw.split("::")[4])

    def incrementRight(self):
        self.right += 1
        self.regroup()

    def incrementWrong(self):
        self.wrong += 1
        self.regroup()

    def regroup(self):
        self.raw = self.polish+"::"+self.english+"::"+str(self.last)+"::"+str(self.right)+"::"+str(self.wrong)+"::\n"

    def getLearnValue(self):
        '''learn value determines how well you know the word. Simply the difference between right and wrong.'''
        return self.right - self.wrong
