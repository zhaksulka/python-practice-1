import os
import csv
import json


# ─────────────────────────────────────────────
# Practice 6 — OOP Classes
# ─────────────────────────────────────────────

class FileManager:
    """Checks that the CSV file exists and creates the output folder."""

    def __init__(self, filename):
        self.filename = filename

    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found. Please download the file from LMS.")
            return False

    def create_output_folder(self, folder='output'):
        print("Checking output folder...")
        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")


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


class ResultSaver:
    """Saves the analysis result to a JSON file."""

    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path

    def save_json(self):
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                json.dump(self.result, f, indent=4)
            print(f"Result saved to {self.output_path}")
        except Exception as e:
            print(f"Error saving file: {e}")


# ─────────────────────────────────────────────
# Practice 5 — Functions
# ─────────────────────────────────────────────

def check_files():
    """Checks if students.csv exists and creates the output/ folder."""
    print("Checking file...")
    if not os.path.exists('students.csv'):
        print("Error: students.csv not found. Please download the file from LMS.")
        return False
    print("File found: students.csv")
    print("Checking output folder...")
    if not os.path.exists('output'):
        os.makedirs('output')
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")
    return True


def load_data(filename):
    """Opens and reads the CSV file; returns a list of row dicts."""
    print("Loading data...")
    try:
        with open(filename, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            students = list(reader)
        print(f"Data loaded successfully: {len(students)} students")
        return students
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the filename.")
    except Exception as e:
        print(f"Error: {e}")
    return []


def preview_data(students, n=5):
    """Prints the first n rows of the student list."""
    print(f"First {n} rows:")
    print("-" * 30)
    for row in students[:n]:
        print(f"{row['student_id']} | {row['age']} | {row['gender']} | {row['country']} | GPA: {row['GPA']}")
    print("-" * 30)


def analyse_gpa(students):
    """Variant A analysis: avg, max, min GPA and count of high performers (GPA > 3.5)."""
    gpas = []
    high_performers = 0
    for row in students:
        try:
            gpa = float(row['GPA'])
            gpas.append(gpa)
            if gpa > 3.5:
                high_performers += 1
        except ValueError:
            print(f"Warning: could not convert value for student {row['student_id']} — skipping row.")
            continue

    avg_gpa = round(sum(gpas) / len(gpas), 2)
    return {
        "total_students": len(students),
        "average_gpa": avg_gpa,
        "max_gpa": max(gpas),
        "min_gpa": min(gpas),
        "high_performers": high_performers
    }


def lambda_map_filter_section(students):
    """Practice 5 Task A3 — lambda, map, filter demonstrations."""
    print("-" * 30)
    print("Lambda / Map / Filter")
    print("-" * 30)

    high_gpa = list(filter(lambda s: float(s['GPA']) > 3.8, students))
    print(f"{'GPA > 3.8':<30}: {len(high_gpa)}")

    gpa_values = list(map(lambda s: float(s['GPA']), students))
    print(f"{'GPA values (first 5)':<30}: {gpa_values[:5]}")

    hard_workers = list(filter(lambda s: float(s['study_hours_per_day']) > 4, students))
    print(f"{'study_hours_per_day > 4':<30}: {len(hard_workers)}")
    print("-" * 30)


# ─────────────────────────────────────────────
# Main program
# ─────────────────────────────────────────────

def main():
    # ── Practice 6 OOP flow ──────────────────
    fm = FileManager('students.csv')
    if not fm.check_file():
        print('Stopping program.')
        exit()
    fm.create_output_folder()

    dl = DataLoader('students.csv')
    dl.load()
    dl.preview()

    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()

    saver = ResultSaver(analyser.result, 'output/result.json')
    saver.save_json()

    print()

    # ── Practice 5 functions flow ────────────
    students = load_data('students.csv')
    preview_data(students)

    result = analyse_gpa(students)
    print("-" * 30)
    print("GPA Analysis")
    print("-" * 30)
    print(f"{'Total students':<20}: {result['total_students']}")
    print(f"{'Average GPA':<20}: {result['average_gpa']}")
    print(f"{'Highest GPA':<20}: {result['max_gpa']}")
    print(f"{'Lowest GPA':<20}: {result['min_gpa']}")
    print(f"{'Students GPA>3.5':<20}: {result['high_performers']}")
    print("-" * 30)

    lambda_map_filter_section(students)

    # ── Exception handling tests (Practice 5 Task A4) ──
    load_data('wrong_file.csv')

    # ── Practice 4 JSON summary ──────────────
    result_p4 = {
        "analysis": "GPA Statistics",
        "total_students": result["total_students"],
        "average_gpa": result["average_gpa"],
        "max_gpa": result["max_gpa"],
        "min_gpa": result["min_gpa"],
        "high_performers": result["high_performers"]
    }
    with open('output/result.json', 'w', encoding='utf-8') as f:
        json.dump(result_p4, f, indent=4)

    print("=" * 30)
    print("ANALYSIS RESULT")
    print("=" * 30)
    print(f"{'Analysis':<20}: GPA Statistics")
    print(f"{'Total students':<20}: {result_p4['total_students']}")
    print(f"{'Average GPA':<20}: {result_p4['average_gpa']}")
    print(f"{'Highest GPA':<20}: {result_p4['max_gpa']}")
    print(f"{'Lowest GPA':<20}: {result_p4['min_gpa']}")
    print(f"{'High performers':<20}: {result_p4['high_performers']}")
    print("=" * 30)
    print("Result saved to output/result.json")


if __name__ == '__main__':
    main()
