students = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
plants = ["G", "C", "R", "V"]
grass = plants[0]
clover = plants[1]
radished = plants[2]
violets = plants[3]

class Garden(object):
    def __init__(self, diagram, students=students):
        self.diagram = diagram
        self.students = students

    def plants(self):
        plants = []
        for student in students:
            plants.append(diagram)
        print(plants)

    def students(self):
        students = list(self.students)
        print(students)

    def is_full(self):
        children = 12
        cups = 4 * children
        rows = 2

garden = Garden("VRCGVVRVCGGCCGVRGCVCGCGV\nVRCCCGCRRGVCGCRVVCVGCGCV")
print(garden.students)
print(garden.plants)