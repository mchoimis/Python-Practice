'''
http://www.codeproject.com/Articles/369387/Data-Clustering-Simulation-in-Python-and-PyGame

Created on Apr 19, 2012

@author: Cyberhornet
'''
import random
import math

class pyDataCluster:
    '''
    classdocs
    '''


    def __init__(self,numberOfCluster,Data,initialPoints=[]):
        '''
        Constructor
        '''
        self.Kgroups=numberOfCluster
        self.Data=Data
        self.Cluster=[]
        self.Kmeans=initialPoints
        self.initialMeanPositions()
        self.terminat=True
    
    def initialMeanPositions(self):
        if not self.Kmeans:
            while True:
                ptx=random.randint(1,500)
                pty=random.randint(1,500)
                if len(self.Kmeans)==self.Kgroups:
                    break
                if ([ptx,pty]) not in self.Kmeans:
                    self.Kmeans.append([ptx,pty])
        
    def clusterSpace(self):
        self.Cluster=[]
        for i in range(self.Kgroups):
            self.Cluster.append([])
               
    def getClusterGroup(self,point):
        dist=[]
        for i in self.Kmeans:
            dist.append(math.fabs(point[0]-i[0])+math.fabs(point[1]-i[1]))
        minIndex = dist.index(min(dist))
        return minIndex
                   
    def setMeans(self):
        means=[]
        x=0
        y=0
        for i in self.Cluster:
            for j in i:
                x=x+j[0]
                y=y+j[1]
            means.append([math.floor(x/len(i)),math.floor(y/len(i))])
            x=0
            y=0
        if(self.Kmeans==means):
            self.terminat=False
        self.Kmeans=[]
        self.Kmeans=means
    
    def createCluster(self):
        self.clusterSpace()
        for i in self.Data:
            point=[i[0],i[1]]
            group=self.getClusterGroup(point)
            self.Cluster[group].append(i)
        self.setMeans()
        return(self.Cluster)
    
    def finalCluster(self):
        while self.terminat:
            clus=self.createCluster()
        return(clus)    
