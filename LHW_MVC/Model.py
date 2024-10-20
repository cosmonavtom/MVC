import json


class TimeTableModel:

    def __init__(self):
        self.dates = []

    def get_dates(self):
        return self.dates

    def add_date(self, course, date, filename):
        data = {}
        data['course'] = course
        data['date'] = date
        self.dates.append(data)
        self.update_json(filename)

    def update_json(self, filename):
        with open(filename, 'w', encoding='utf-8') as fp:
            json.dump(self.dates, fp, ensure_ascii=False, indent=2)