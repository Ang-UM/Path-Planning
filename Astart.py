import math
from OrderedList import OrderedList,Node
import matplotlib.pyplot as plt
class Astart:
    def __init__(self):
        path = OrderedList()

    def getcenterpoint(node):
        x = node[0].x
        y = node[0].y
        centrex = (node[0].x + node[0].width) / 2
        centrey = (node[0].y + node[0].height) / 2
        return centrex, centrey

    def getdistance(self,x1, y1, x2, y2):
        return math.sqrt((x1 - x2) * (x1-x2) + (y1-y2)*(y1 - y2))

    def Astartprocessing(self,initalnode,goalnode,freeNodes,ax):
        #inital point
        g = plt.Rectangle((initalnode[0].x, initalnode[0].y), initalnode[0].width, initalnode[0].height, facecolor='red')
        ax.add_patch(g)
        #goal point
        g = plt.Rectangle((goalnode[0].x, goalnode[0].y), goalnode[0].width, goalnode[0].height, facecolor='green')
        ax.add_patch(g)

        unvisitedlist = OrderedList()
        stop = False    #check meet goal
        foundpath = False
        visitedlist = OrderedList()

        unvisitedlist.add(initalnode[0])
        k = 1
        while(stop == False  and foundpath == False):
            currnode = unvisitedlist.pop().getData()
            cost = self.findactualcost(currnode)
            visitedlist.add(currnode)
            #check close to goal

            if(currnode.x <= goalnode[0].x <= currnode.x+currnode.width and currnode.y <= goalnode[0].y <= currnode.y+currnode.height):
                foundpath = True
            #find 8 direction's node
            if(stop == False):
                nearnodes = self.findAround(currnode,freeNodes)

                #change actual cost in nearnodes
                for node in nearnodes:
                    prex = node.x + node.width/2
                    prey = node.y + node.height/2
                    currx = currnode.x +currnode.width/2
                    curry =  currnode.x+currnode.height/2
                    node.gValue =  cost + self.getdistance(prex,prey,currx,curry)

                    found  = unvisitedlist.search(node)
                    if(found != None):
                        if(found.gValue > node.gValue):
                            found.gValue = node.gValue
                            found.father = currnode

                    else:
                        if(visitedlist.search(node) == None):
                            node.father = currnode
                            unvisitedlist.add(node)

            if(unvisitedlist == None):
                stop = True
                print("there is no path")

        if(foundpath == True):
            while (currnode.father!= None):
                #print("currx = ", currnode.x, "curry = ", currnode.y, "goalx = ", goalnode[0].x, "goaly = ",
                      #goalnode[0].y)
                g = plt.Rectangle((currnode.x, currnode.y), currnode.width, currnode.height, facecolor='gray')
                ax.add_patch(g)
                currnode = currnode.father





    def findactualcost(self,currnode):
        cost = 0
        fathernode = currnode.father
        while(fathernode != None):
            cost = cost + self.getdistance(currnode.x,currnode.y,fathernode.x,fathernode.y)
            currnode = currnode.father
            fathernode = fathernode.father
        return cost

    def findAround(self,currnode,freeNodes):
        aroundnotes = []
        rectangleX = currnode.x
        rectangleY = currnode.y
        rectangleHeight = currnode.height
        rectangleWidth = currnode.width
        for node in freeNodes:
            nodeX = node[0].x
            nodeY = node[0].y
            nodeHeight = node[0].height
            nodeWidth = node[0].width
            if (rectangleY + rectangleHeight == nodeY and not (nodeX + nodeWidth < rectangleX) and not (
                    nodeX > rectangleX + rectangleWidth)):
                aroundnotes.append(node[0])

            elif (nodeX == rectangleX + rectangleWidth and not (nodeY > rectangleY + rectangleHeight) and not (
                    nodeY + nodeHeight < rectangleY)):
                aroundnotes.append(node[0])

            elif (nodeY + nodeHeight == rectangleY and not (nodeX + nodeWidth < rectangleX) and not (
                    nodeX > rectangleX + rectangleWidth)):
                aroundnotes.append(node[0])
            elif (nodeX + nodeWidth == rectangleX and not (nodeY > rectangleY + rectangleHeight) and not (
                    nodeY + nodeHeight < rectangleY)):
                aroundnotes.append(node[0])

        return aroundnotes