class School:
    def __init__(self):
        self.classes={}

    def add_student(self, name, grade):
        try:
            self.classes[grade].append(name)
        except KeyError as err:
            self.classes[grade]=[name]

    def roster(self):
        d=[]
        g= dict(sorted(self.classes.items()))

        for a in g.values():   
            for b in sorted(a):
                d.append(b)
        return (d)

    def grade(self, grade_number):
        try:
            return sorted(self.classes[grade_number])
        except KeyError as err:
            return []
