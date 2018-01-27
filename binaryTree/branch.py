'''
Created on Nov 6, 2017

@author: ricardo.villa.berger
'''

class branch(object):

    def __init__(self, value):
        self.value = value
        self.right_leaf = None
        self.left_leaf = None
    
    @staticmethod
    def spacesForValue(value):
        sapce_number=5
        if (value=="Half"):
            return " "*(sapce_number//4)
        if (type(value)==type(1)):
            return " "*(sapce_number-value)
        else:
            if(value is None):
                return " "*(sapce_number-4)
            else:
                lenght = len(str(value))
                spaces = " "*(sapce_number-lenght if lenght<=7 else 1)
                return spaces

    def __reper__(self):
        this=str(self.value)
        left=str(self.left_leaf.value if self.left_leaf != None else "None")
        right=str(self.right_leaf.value if self.right_leaf != None else "None")
        preoutput=branch.spacesForValue(this) + "/" + branch.spacesForValue(left) + "\\\n"+branch.spacesForValue(right)+"{}" + branch.spacesForValue(right) + "{}"
        printable =  preoutput.format(this,left,right)
        return str(printable)
    def add(self, value):
        if (value<self.value):
            if self.left_leaf is None:
                self.left_leaf=branch(value)
            else:
                self.left_leaf.add(value)
        else:
            if self.right_leaf is None:
                self.right_leaf=branch(value)
            else:
                self.right_leaf.add(value)
    def __str__(self):
        return self.__reper__()

if __name__=="__main__":
    b = branch(3)
    print(b)
