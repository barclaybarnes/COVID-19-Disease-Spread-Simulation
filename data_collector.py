# data_collector.py
import pandas as pd

class DataCollector:
    def __init__(self):
        self.records = []

    def record(self, day, agents):
        states = [a.state for a in agents]
        self.records.append({
            "day": day,
            "S": states.count('S'),
            "E": states.count('E'),
            "I": states.count('I'),
            "R": states.count('R'),
            "V": states.count('V')
        })

    def to_csv(self, filename="simulation_results.csv"):
        df = pd.DataFrame(self.records)
        df.to_csv(filename, index=False)
