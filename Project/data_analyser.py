class DataAnalyser:
    """Runs Variant A GPA analysis."""

    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        gpas = []
        high_performers = 0
        for row in self.students:
            try:
                gpa = float(row['GPA'])
                gpas.append(gpa)
                if gpa > 3.5:
                    high_performers += 1
            except ValueError:
                print(f"Warning: could not convert value for student {row['student_id']} — skipping row.")
                continue

        avg_gpa = round(sum(gpas) / len(gpas), 2)
        max_gpa = max(gpas)
        min_gpa = min(gpas)

        self.result = {
            "analysis": "GPA Statistics",
            "total_students": len(self.students),
            "average_gpa": avg_gpa,
            "max_gpa": max_gpa,
            "min_gpa": min_gpa,
            "high_performers": high_performers
        }
        return self.result

    def print_results(self):
        print("-" * 30)
        print("GPA Analysis")
        print("-" * 30)
        print(f"{'Total students':<20}: {self.result['total_students']}")
        print(f"{'Average GPA':<20}: {self.result['average_gpa']}")
        print(f"{'Highest GPA':<20}: {self.result['max_gpa']}")
        print(f"{'Lowest GPA':<20}: {self.result['min_gpa']}")
        print(f"{'Students GPA>3.5':<20}: {self.result['high_performers']}")
        print("-" * 30)
