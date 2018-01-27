from binaryTree.branch import branch

class Btree(object):
    def __init__(self):
        self.root=None
        
    def add(self, values):
        if self.root is None:
            self.root=branch(values.pop(0))
        for n in values:
            self.root.add(n)
    
    @staticmethod
    def max_hight(tree):
        if tree is None:
            return 0
        rightHight=Btree.max_hight(tree.right_leaf)+1 if tree.right_leaf else 1
        leftHight=Btree.max_hight(tree.left_leaf)+1 if tree.left_leaf else 1
        return max(rightHight,leftHight) 
    
    def __reper__(self):
        return Btree.toString(self.root)
    
    def __str__(self, *args, **kwargs):
        return self.__reper__()
    
    @staticmethod
    def toString(tree,level=0):
        if tree is not None:
            return "\n"+("\t"*level)+str(tree.value)+Btree.toString(tree.right_leaf, level+1)+Btree.toString(tree.left_leaf, level+1)
        else:
            return ''
        
    @staticmethod
    def getmin(tree):
        if(tree.left_leaf):
            return Btree.getmin(tree.left_leaf)
        else:
            return tree.value
        
    @staticmethod
    def getmax(tree):
        if(tree.right_leaf):
            return Btree.getmax(tree.right_leaf)
        else:
            return tree.value
        
    @staticmethod
    def walktree(tree,result=[]):
        if tree:
            if (tree.left_leaf ):
                Btree.walktree(tree.left_leaf, result)
            result.append(tree.value)
            if(tree.right_leaf):
                Btree.walktree(tree.right_leaf, result)
        return result
    
if(__name__=='__main__'):
    numbers=[3,7,2,6,9,4,8,5,1,10]
    #numbers=[1,2,3,4,5,6,7,8,9,10]
    bt=Btree()
    bt.add(numbers)
    print ('hight:'+str(Btree.max_hight(bt.root)))
    print ('min:'+str(Btree.getmin(bt.root)))
    print ('max:'+str(Btree.getmax(bt.root)))
    print ('walk:'+str(Btree.walktree(bt.root)))