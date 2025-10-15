class matrix:
    def __init__(self, mat):
        self.mat = mat
    def trans(self):
        pass
    def minor(self):
        pass
    def det(self):
        pass
    def adj(self):
        pass
    def inv(self):
        if self.det()!=0:
            return (self.adj().trans())/self.det()
        else:
            print('That matrix is not invertible.')