class matrix:
    def __init__(self, mat):
        self.mat = mat
    def trans(self):
        mat2=[]
        for i in range(len(self.mat)):
            mat2+=[[]]
            for j in range(len(self.mat[i])):
                mat2[i]+=[0]
                mat2[i][j]=self.mat[j][i]
        self.mat = mat2
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
    def mat_mult(self,other_mat):
        pass
def trans_test():
    test = {"[[1, 1], [2, 2]]": matrix([[1,2],[1,2]]),
            "[[173, 3, 700], [802, 17, 1208374], [56, 212, 123]]":matrix([[173,802,56],[3,17,212],[700,1208374,123]]),
            "[["+str(matrix([[1,2], [3,4]]).mat)+", [1, 2]], ["+str(matrix(matrix([1])).mat)+", [3, 4]]]":matrix([[matrix([[1,2],[3,4]]),matrix(matrix([1]))],[[1,2],[3,4]]]),
            "[[1, 2], [3, 4], [5, 6]]":matrix([[1,3,5],[2,4,6]]),
            "error":None,
            "error":7,
            "[['e', 'y'], ['e', 'y']]":matrix([["e","e"],["y","y"]])}
    for i in test:
        try:
            test[i].trans()
            if str(test[i].mat)==i:
                print('yay!')
            else:
                print('test failed: transposes unequal.')
        except Exception as e:
            print("error:",e)
trans_test()
# matrix1 = matrix([[1,2],[1,2]])
# matrix1.trans()
# print(matrix1.mat)
