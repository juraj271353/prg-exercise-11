class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

grades = StudentsGrades([10,25,60,55,99])
print(grades.get_by_index(2))
print(grades.count())