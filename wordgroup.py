"""
Has format polish::english::right::wrong::

"""

class WordGroup(object):
    def __init__(self, rawgroup):
        self.raw = rawgroup
        self.parsegroup()

    def parsegroup(self):
        self.polish = self.raw.split("::")[0]
        self.english = self.raw.split("::")[1]
        self.right = int(self.raw.split("::")[2])
        self.wrong = int(self.raw.split("::")[3])

    def incrementRight(self):
        self.right += 1
        self.regroup()

    def incrementWrong(self):
        self.wrong += 1
        self.regroup()

    def regroup(self):
        self.raw = self.polish+"::"+self.english+"::"+str(self.right)+"::"+str(self.wrong)+"::\n"
