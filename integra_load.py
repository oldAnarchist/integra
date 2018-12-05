import os, ntpath as np
class inputdata:
    # print('huy')
    def __init__(self, path):
        self.ampl = list()
        self.time = list()
        print('start path = {}'.format(path))
        with open(path) as file:
            for i in file:
                try:
                    self.ampl.append(float(i.split(',')[0]))
                except ValueError:
                    pass
                try:
                    self.time.append(float(i.split(',')[1]))
                except ValueError:
                    pass


class Phase:
    def __init__(self, path):
        self.sin = inputdata(path)
        self.cos = inputdata(self.get_pair_path(np.basename(path)))
    def get_pair_path(self, path):
        val = path.split('.')
        num = int(val[0][-1]) % 2
        if num == 0:
            return './'+ val[0][:len(val[0])-1] + str(int(val[0][-1])-1) + '.' + val[1]
        else:
            return './' + val[0][:len(val[0]) - 1] + str(int(val[0][-1]) + 1) + '.' + val[1]
def folderprocess(path: str):
    if os.path.exists(path):
        ls = os.listdir(path)
        print(ls)

# folderprocess('./')
# file1 = inputdata('./exp2-1_1.csv')
# file2 = inputdata('./exp2-1_2.csv')
phase1 = Phase('./exp2-1_1.csv')
# for i in file2.ampl:
#     print(i)




# phase1 = faza('111')

# phase1.sin = file1
# phase1.cos = file2

