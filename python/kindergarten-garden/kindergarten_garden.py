class Garden:
    def __init__(self, diagram, students=[]):
        de = [
            "Charlie",
            "Alice",
            "David",
            "Eve",
            "Fred",
            "Ginny",
            "Bob",
            "Harriet",
            "Ileana",
            "Joseph",
            "Kincaid",
            "Larry",
        ]
        diagram = diagram.split("\n")
        self.various_plants = {
            "G": "Grass",
            "C": "Clover",
            "R": "Radishes",
            "V": "Violets",
        }
        rows = [x for x in diagram]
        self.h = [[b[i : i + 2] for i in range(0, len(b), 2)] for b in rows]
        self.students = sorted(students or de)

    def plants(self, name):
        ta = []
        for g in self.h:
            pos = [x for x in g[self.students.index(name)]]
            for i in pos:
                if i in self.various_plants:
                    ta.append(self.various_plants[i])
        return ta