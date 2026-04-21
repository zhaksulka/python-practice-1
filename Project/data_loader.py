import csv


class DataLoader:
    """Loads the CSV file and previews the data."""

    def __init__(self, filename):
        self.filename = filename
        self.students = []

    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found. Please check the filename.")
        except Exception as e:
            print(f"Error: {e}")
        return self.students

    def preview(self, n=5):
        print(f"First {n} rows:")
        print("-" * 30)
        for row in self.students[:n]:
            print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
        print("-" * 30)
