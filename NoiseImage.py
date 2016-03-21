
from random import randint

class NoiseImage:
    
    def __init__(self, width, height, data, imagesCount):
        self.width = width
        self.height = height
        self.data = data
        self.splitedImages = []
        self.imagesCount = imagesCount
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def getOriginalData(self):
        return self.data
    
    def getSplitedImages(self):
        if len(self.splitedImages) == 0:
            self.split()
        return self.splitedImages
    
    def split(self):
        for i in xrange(self.imagesCount):
            self.splitedImages.append([])
        
        for index in xrange(len(self.data)):
            pc = 0
            nc = 0
            for part in xrange(self.imagesCount):
                if pc + nc + 1 == self.imagesCount:
                    if pc % 2 == int(self.data[index]):
                        self.splitedImages[part].append(1)
                    else:
                        self.splitedImages[part].append(0)
                else:
                    if randint(0, 1):
                        pc += 1
                        self.splitedImages[part].append(1)
                    else:
                        nc += 1
                        self.splitedImages[part].append(0)