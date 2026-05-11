class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}

    def analyse(self):
        print("Not implemented — use a child class")

    def print_results(self):
        for key, value in self.result.items():
            print(f"{key}: {value}")

    def __str__(self):
        return f"DataAnalyser: base class, {len(self.students)} students"


class GpaAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        try:
            gpas = list(
                filter(
                    lambda x: x is not None,
                    map(
                        lambda s: float(s["GPA"]) if s.get("GPA") else None,
                        self.students
                    )
                )
            )
            high_performers = list(filter(lambda g: g > 3.5, gpas))

            self.result = {
                "total_students": len(self.students),
                "average_gpa": round(sum(gpas) / len(gpas), 2) if gpas else 0,
                "max_gpa": max(gpas) if gpas else 0,
                "min_gpa": min(gpas) if gpas else 0,
                "high_performers": len(high_performers),
            }
        except Exception as e:
            print(f"Analysis error: {e}")

    def print_results(self):
        print("=" * 30)
        print("GPA ANALYSIS REPORT")
        print("=" * 30)
        super().print_results()
        print("=" * 30)

    def __str__(self):
        return f"GpaAnalyser: GPA Statistics, {len(self.students)} students"


class CountryAnalyser(DataAnalyser):
    def __init__(self, students):
        super().__init__(students)

    def analyse(self):
        try:
            country_counts = {}
            for s in self.students:
                c = s.get("country", "Unknown")
                country_counts[c] = country_counts.get(c, 0) + 1

            sorted_countries = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)

            self.result = {
                "total_students": len(self.students),
                "total_countries": len(country_counts),
                "top_3": sorted_countries[:3],
                "all_countries": sorted_countries,
            }
        except Exception as e:
            print(f"Analysis error: {e}")

    def print_results(self):
        print("=" * 30)
        print("COUNTRY ANALYSIS REPORT")
        print("=" * 30)
        for key, value in self.result.items():
            if key != "all_countries":
                print(f"{key}: {value}")
        print("=" * 30)

    def __str__(self):
        return f"CountryAnalyser: Country Analysis, {len(self.students)} students"
