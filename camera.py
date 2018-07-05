import numpy
from module import module

class camera(module):
    def __init__(self, debug=false)
        self.name="rgb camera"
        self.on_message="recieving visual data"
        self.data_message="rgb image"
        self.image_size=[24, 24]
        if debug==True:
            self.sampleData=np.load("sampleData.npz")['arr_0']
            self.setImageSize(self.sampleData.rows, self.sampleData.cols)
        else:
            self.sampleData=None
    
    def setImageSize(self, rows, cols):
        if rows>0 and cols>0:
            self.image_size=[rows, cols]

    def getData(self):
        if sampleData is not None:
            return sampleData
        else:
            return np.zeros((self.image_size[0], self.image_size[1], 3))


