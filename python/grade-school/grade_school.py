class School:
    def __init__(self):
        self.students = {}
        self.scores = {}

    def add_student(self, name, grade):
        self.students[name] = grade
        if grade in self.scores:
            self.scores[grade].append(name)
        else:
            self.scores[grade] = [name]

    def roster(self):
        students = []
        for i in range(1, 11):
            if i in self.scores:
                students.extend(sorted(self.scores[i]))

        return students

    def grade(self, grade_number):
        try:
            grades = self.scores[grade_number]
            return sorted(grades)
        except KeyError:
            return []
