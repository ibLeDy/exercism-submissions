children = [
    "Alice",
    "Bob",
    "Charlie",
    "David",
    "Eve",
    "Fred",
    "Ginny",
    "Harriet",
    "Ileana",
    "Joseph",
    "Kincaid",
    "Larry",
]

plant_names = {
    "V": "Violets",
    "R": "Radishes",
    "G": "Grass",
    "C": "Clover",
}


class Garden(object):
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        self.students = students
        self.student_plants = {}
        self.get_students()
        self.get_plants()

    def get_students(self):
        plants = self.diagram.split()
        students_plants = {}

        for row in plants:
            count = 0
            for i in range(0, len(row), 2):
                if self.students is None:
                    name = children[count]
                else:
                    name = sorted(self.students)[count]

                if name in students_plants:
                    students_plants[name].extend([row[i], row[i + 1]])
                else:
                    students_plants[name] = [row[i], row[i + 1]]

                count += 1

        self.students_plants = students_plants

    def get_plants(self):
        for student in self.students_plants:
            student_plants = [plant_names[p] for p in self.students_plants[student]]
            self.student_plants[student] = student_plants

    def plants(self, name):
        return self.student_plants[name]
