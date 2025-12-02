import termcolor as tcr
class matrix:
    def __init__(self, mat):
        self.mat = mat
        self.isTrans = False
    def trans(self):
        mat2=[]
        for i in range(len(self.mat[0])):
            mat2+=[[]]
            for j in range(len(self.mat)):
                mat2[i]+=[0]
                mat2[i][j]=self.mat[j][i]
        self.mat = mat2
        self.isTrans = True
    def minor(self):
        pass
    def det(self):
        pass
    def adj(self):
        pass
    def inv(self):
        if self.det()!=0:
            return self.scalar_mult((self.adj().trans()),1/self.det())
        else:
            print('That matrix is not invertible.')
    def mat_mult(self,other_mat):
        if len(self.mat)!=len(other_mat[0]):
            print("These matrices are not compatible under a normal definition of matrix multiplication.")
        else:
            newMat=[]
            for i in self.mat:
                newMat.append([])
            summand = 0
            for k in range(len(self.mat)):
                for i in range(len(other_mat)):
                    summand = 0
                    for j in range(len(self.mat[0])):
                        summand+=(self.mat[k][j])*(other_mat[j][i])
                        print(summand)
                    newMat[i]+=[summand]
            self.mat = newMat
            print(self.mat)
            self.trans()
            print(self.mat)
    def scalar_mult(self, scalar):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.mat[i][j]=self.mat[i][j]*scalar
    def discretize(self):
        for i in range(len(self.mat)):
            for j in range(len(self.mat[0])):
                self.mat[i][j]=int(self.mat[i][j])
    def print(self):
        flag = [(91, 206, 250), (245, 169, 184), "white", (245, 169, 184), (91, 206, 250)]
        if not self.isTrans:
            for i in range(len(self.mat)):
                print(self.mat[i])
        else:
            for i in range(len(self.mat)):
                tcr.cprint(self.mat[i], flag[i%5])
def trans_test():
    test = {"[[1, 1], [2, 2]]": matrix([[1,2],[1,2]]),
            "[[173, 3, 700], [802, 17, 1208374], [56, 212, 123]]":matrix([[173,802,56],[3,17,212],[700,1208374,123]]),
            "[["+str(matrix([[1,2], [3,4]]).mat)+", [1, 2]], ["+str(matrix(matrix([1])).mat)+", [3, 4]]]":matrix([[matrix([[1,2],[3,4]]),matrix(matrix([1]))],[[1,2],[3,4]]]),
            "[[1, 2], [3, 4], [5, 6]]":matrix([[1,3,5],[2,4,6]]),
            "error":None,
            "error":7,
            "[7]":[7],
            "[['e', 'y'], ['e', 'y']]":matrix([["e","e"],["y","y"]])}
    for i in test:
        try:
            test[i].trans()
            if str(test[i].mat)==i:
                print('yay!')
            else:
                print('test failed: transposes unequal.')
        except Exception as e:
            print("error:",str(e)+"; expected:",i)
matrix([[1,2],[3,4]]).mat_mult([[1,2],[3,4]])
# matrix1 = matrix([[1,2],[1,2]])
# matrix1.trans()
# print(matrix1.mat)
