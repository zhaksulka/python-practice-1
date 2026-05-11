import csv


class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.students = []

    def load(self):
        try:
            with open(self.filepath, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.students = [row for row in reader]
            print(f"Loaded {len(self.students)} students from {self.filepath}")
        except FileNotFoundError:
            print(f"Error: file not found — {self.filepath}")
        except Exception as e:
            print(f"Error loading file: {e}")

    def preview(self):
        print("\n--- Preview (first 3 rows) ---")
        for row in self.students[:3]:
            print(dict(list(row.items())[:5]))
        print("------------------------------\n")
