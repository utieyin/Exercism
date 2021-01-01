class Matrix:
    def __init__(self, matrix_string):
        value = matrix_string.split("\n")
        self.value =value

    def row(self, index):
        result = {}
        for i, k in enumerate(self.value):
            k = k.strip()
            result[i] = k
        pos = index -1

        if pos in result:
            res = [int(x) for x in result[pos].split()]
            return res
        else:
            raise Exception("Key not present in dict")

    def column(self, index):
        pos = index-1
        result = []
        a = 0
        p = 0
        t = {}
        for k in self.value:
            k = [int(x) for x in k.split()]
            result.append(k)

        for k in range(len(result[p])):
            while a < len(result[p]):
                row = []
                for f in range(len(result)):
                    row.append(result[f][a])
                t[a] = row
                a += 1
                break;
        if pos in t:
            return t[pos]
        else:
            raise Exception("Key not in dict")

