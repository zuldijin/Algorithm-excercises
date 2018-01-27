'''
Created on January 24, 2018

@author: ricardo.villa.berger
'''
from platform import node
import queue


class adjacency_list_node(object):
    def __init__(self):
        self.vertex=None
        self.edges=[]
        self.color="White"
        self.parent=None
        self.distance=None
    def __repr__(self, *args, **kwargs):
        return str(self.vertex)+"|"+str(self.edges)
   
    def __str__(self, *args, **kwargs):
        return self.__repr__()

class adjacency_list(object):
    def __init__(self):
        self.nodes=[]
        
    def insert_node_by_node(self, node):
        self.nodes.append(node)
        
    def insert_node_by_vertex(self, vertex,edges):
        tempNode=adjacency_list_node()
        tempNode.vertex=vertex
        tempNode.edges=edges
        self.insert_node_by_node(tempNode)
    
    def __repr__(self, *args, **kwargs):
        a=""
        for n in self.nodes:
            a+=str(n)+"\n"
        return a
    def getNode(self, vertex, parent):
        for node in self.nodes:
            if vertex==node.vertex:
                if parent is not None:
                    node.parent=parent
                return node
                
    def breadth_first_search(self ,beginingVertex):
        queue=[]
        root=self.getNode(beginingVertex,None)
        root.distance=0
        queue.append(root)
        while len(queue)!=0:
            node=queue.pop(0);
            newEdges=[]
            for v in node.edges:
                newVertex=self.getNode(v, None)
                if newVertex is not None and newVertex.color=="White":
                    newVertex=self.getNode(v, node)
                    newVertex.color="gray"
                    newVertex.distance=node.distance+1
                    queue.append(newVertex)
                    newEdges.append(newVertex)
            node.color="Black"
            node.edges=newEdges
        return root
        
if __name__ == '__main__':
    graph=adjacency_list()
    graph.insert_node_by_vertex(1, [2,5])
    graph.insert_node_by_vertex(2, [1,5,3,4])
    graph.insert_node_by_vertex(3, [2,4])
    graph.insert_node_by_vertex(4, [2,5,3])
    graph.insert_node_by_vertex(5, [4,1,2])
    print (graph.breadth_first_search(3))
