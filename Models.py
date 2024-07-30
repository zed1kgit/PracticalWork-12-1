import json


class MarksModel:

    def __init__(self):
        self.marks = []

    def get_data(self):
        return self.marks

    def add_data(self, course, mark, filename):
        data = {'course': course, 'mark': mark}
        self.marks.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, "w", encoding="utf-8") as fh:
            json.dump(self.marks, fh, ensure_ascii=False, indent=2)


class TimetableModel:

    def __init__(self):
        self.dates = []

    def get_data(self):
        return self.dates

    def add_data(self, course, date, filename):
        data = {'course': course, 'date': date}
        self.dates.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, "w", encoding="utf-8") as fh:
            json.dump(self.dates, fh, ensure_ascii=False, indent=2)
