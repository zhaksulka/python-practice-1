from analytics import FileManager, DataLoader, ResultSaver, Report
from analytics.analyser import GpaAnalyser, CountryAnalyser

# ── File & folder setup ────────────────────────────────────────────────────────
fm = FileManager('students.csv')
fm.check_file()
fm.create_output_folder()

# ── Load data ──────────────────────────────────────────────────────────────────
dl = DataLoader('students.csv')
dl.load()
dl.preview()

# ── Task 5 — Polymorphism ──────────────────────────────────────────────────────
# Small sample for the second analyser to keep output concise
sample_10 = dl.students[:10]

analysers = [GpaAnalyser(dl.students), CountryAnalyser(sample_10)]

print("-" * 30)
print("Running all analysers:")
print("-" * 30)

for a in analysers:
    print(a)
    a.analyse()
    a.print_results()

# ── Task 4 — Report (uses GpaAnalyser result) ──────────────────────────────────
saver = ResultSaver(analysers[0].result, 'output/result.json')
report = Report(analysers[0], saver)
report.generate()
