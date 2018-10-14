from random import randint

class NodeBST():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None    
    def insert(self, val):
        if val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = NodeBST(val)
        elif val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = NodeBST(val)   
        else:
            if randint(1, 2) == 1:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = NodeBST(val)
            else:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = NodeBST(val)  
    def inOrderTravel(self):
        child = []
        def travel(node, child):
            child.append(node.val)
            if node.left:
                travel(node.left, child)            
            if node.right:
                travel(node.right, child)
        travel(self, child)
        return child    
    def preOrderTravel(self):
        child = []
        def travel(node, child):            
            if node.left:
                travel(node.left, child)       
            child.append(node.val)     
            if node.right:
                travel(node.right, child)
        travel(self, child)
        return child
    def postOrderTravel(self):
        child = []
        def travel(node, child):
            if node.left:
                travel(node.left, child)
            if node.right:
                travel(node.right, child)
            child.append(node.val)        
        travel(self, child)
        return child    
    def levelTravel(self, pointers):
        nextChild = []
        for i in pointers:
            if i.left:
                nextChild.append(i.left)
            if i.right:
                nextChild.append(i.right)
        if nextChild != []:
            self.levelTravel(nextChild)    
    def treeHeight(self):
        def height(root):
            if not root:
                return 0
            l = 1 + height(root.left)
            r = 1 + height(root.right)
            return max(l, r)
        return height(self)
    def printFormattedTree(self):
        heap = ["*"]*(2**(self.treeHeight())-1)
        
        
        def addToHeap(children):
            newChildren = []
            for i in children:

                heap[i[1]] = i[0].val
                if i[0].left:
                    newChildren.append([i[0].left, i[1]*2+1])
                if i[0].right:
                    newChildren.append([i[0].right, i[1]*2+2])
            if newChildren != []:
                addToHeap(newChildren)
        listChild = [[self, 0]]
        addToHeap(listChild)            
        
        sl = len(heap)//2
        sr = len(heap)
        lines = []
        while heap[sl:sr] != []:
            lines.append(heap[sl:sr])
            sl = sl // 2
            sr = sr // 2
        d = " "
        baseD = 1*d
        initD = ""
        finalLines = []
        counter = 1
        for line in lines:
            newLine = ""
            
            for i in range(len(line)):
                if i == 0:
                    newLine += initD + str(line[i])
                else:
                    newLine += baseD + str(line[i])
            initD += (len(baseD)//2 + 1)*d
            baseD = (len(baseD*2) + 1)*d
            finalLines.append(newLine)
        while finalLines != []:
            print(finalLines.pop())
            print()
def testNodeBST():
    base = 4
    x = base*2 + 1
    newBST = NodeBST(base)
    for i in range (x - 1):
        newBST.insert(randint(0, x))

    print("--")
    newBST.printFormattedTree()
    
    print(newBST.postOrderTravel())
    print(newBST.inOrderTravel())
    print(newBST.preOrderTravel())
    print(newBST.treeHeight())
testNodeBST()














