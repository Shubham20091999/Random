# * len can be zero or more
# _ len can be one only
# ? len can be one or zero
# eg
# atleast 3 charcters ___*
# atmost 3 characters ???
# exactly 3 characters ___
# atleast 2 and atmost 4 ??__

class CheckString:
    def __init__(self, dummy, test):
        self.memo = [[None for _ in range(len(test)+1)]
                for _ in range(len(dummy)+1)]
        self.dummy = dummy
        self.test = test

    def check(self, i=0, j=0):
        if(self.memo[i][j] != None):
            return self.memo[i][j]
        if(j == len(self.test)):
            if(len(self.dummy) == i):
                self.memo[i][j] = True
                return True
            if(i == len(self.dummy)-1 and self.dummy[i] == '*'):
                self.memo[i][j] = True
                return True
            return False
        elif(i == len(self.dummy)):
            self.memo[i][j] = False
            return False

        if(self.dummy[i] == self.test[j]):
            # move character in both
            self.memo[i][j] = self.check(i+1, j+1)
            return self.memo[i][j]

        if(self.dummy[i] == '_'):
            # move characters in both
            self.memo[i][j] = self.check(i+1, j+1)
            return self.memo[i][j]

        if(self.dummy[i] == '?'):
            # ? corresponds to 0 character
            # ? corresponds to 1 character
            self.memo[i][j] = self.check(i+1, j) or self.check(i+1, j+1)
            return self.memo[i][j]
        if(self.dummy[i] == '*'):
            # * corresponds to 0 character
            # * corresponds to multiple character
            self.memo[i][j] = self.check(i+1, j) or self.check(i, j+1)
            return self.memo[i][j]
        self.memo[i][j] = False
        return False