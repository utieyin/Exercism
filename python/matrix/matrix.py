class Matrix:
    def __init__(self, matrix_string):
        result = []
        for k in matrix_string.split("\n"):
            k = [int(x) for x in k.split()]
            result.append(k)
        self.result =result

    def row(self, index):
        if self.result[index-1]:
            return self.result[index-1]
        else:
            raise Exception("Key not present in dict")

    def column(self, index):
        pos = index-1
        a = 0
        p = 0
        t = {}
        for k in range(len(self.result[p])):
            while a < len(self.result[p]):
                row = []
                for f in range(len(self.result)):
                    row.append(self.result[f][a])
                t[a] = row
                a += 1
        if pos in t:
            return t[pos]
        else:
            raise Exception("Key not in dict")