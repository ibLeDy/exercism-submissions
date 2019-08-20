class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.rows = []
        
        for row in matrix_string.split("\n"):
            self.rows.append([int(i) for i in row.split(" ")])

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return [row[index-1] for row in self.rows]
