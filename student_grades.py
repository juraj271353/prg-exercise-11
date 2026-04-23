import matplotlib.pyplot as plt
from sorting import random_numbers

class StudentsGrades:
    def __init__(self, scores):
        self.scores = scores

    def get_by_index(self, index):
        return self.scores[index]

    def count(self):
        return len(self.scores)

    def get_grade(self, index):
        points = self.scores[index]

        if points >= 90:
            return "A"
        elif points >= 80:
            return "B"
        elif points >= 70:
            return "C"
        elif points >= 60:
            return "D"
        elif points >= 50:
            return "E"
        else:
            return "F"


    def find(self,value):
        results = []

        for i in range(len(self.scores)):
            if self.scores[i] == value:
                results.append(i)

        return results


    def get_sorted(self):
        scores = self.scores.copy()
        n = len(scores)

        for i in range(n):
            for j in range(0, n - i - 1):
                if scores[j] > scores[j + 1]:
                    scores[j], scores[j + 1] = scores[j + 1], scores[j]

        return scores


def main():
    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])

    print(results.count())  # 9
    print(results.get_by_index(2))  # 91
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]

    print(results.get_grade(2))  # A (91 bodů)
    print(results.get_grade(6))  # A (100 bodů)
    print(results.get_grade(7))  # F (38 bodů)

    values = results.scores
    plt.hist(values, bins=5)
    plt.show()

    print(results.find(100))  # [6]
    print(results.find(50))  # [4]
    print(results.find(77))  # []

    print(results.get_sorted())  # [38, 42, 50, 58, 67, 73, 85, 91, 100]
    print(results.scores)  # [85, 42, 91, 67, 50, 73, 100, 38, 58]  ← beze změny


    results = StudentsGrades([85, 42, 91, 67, 50, 73, 100, 38, 58])
    print("Pocet studentu", results.count())

    for i in range(results.count()):
        points = results.get_by_index(i)
        grade = results.get_grade(i)
        print(f"Student {i}: {points} points- {grade}")

    print("Studenti so 100 bodmi", results.find(100))

    print("Zoradene vysledky", results.get_sorted())

    random_results = StudentsGrades(random_numbers(30, 0, 100))
    print(random_results.count())
    print(random_results.get_sorted())


if __name__ == "__main__":
    main()