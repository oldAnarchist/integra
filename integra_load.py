class inputdata:
    def __init__(self, path):
        self.ampl = list()
        self.time = list()
        # Тут по переменной path закачиваем в себя данные

class faza:
    def __init__(self, path):
        self.sin = inputdata(path)
        self.cos = inputdata(get_pair_path(path))
    def get_pair_path(path):
        return path

file1 = inputdata('exp2-1_1.csv')
file2 = inputdata('exp2-1_2.csv')

phase1 = faza('111')

phase1.sin = file1
phase1.cos = file2

