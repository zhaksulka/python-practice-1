import json
import os


class ResultSaver:
    def __init__(self, result, filepath):
        self.result = result
        self.filepath = filepath

    def save_json(self):
        try:
            folder = os.path.dirname(self.filepath)
            if folder and not os.path.exists(folder):
                os.makedirs(folder)
            serialisable = {
                k: (list(v) if isinstance(v, list) else v)
                for k, v in self.result.items()
            }
            with open(self.filepath, 'w', encoding='utf-8') as f:
                json.dump(serialisable, f, indent=4)
            print(f"Result saved to {self.filepath}")
        except Exception as e:
            print(f"Error saving result: {e}")
