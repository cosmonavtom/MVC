class TimeTableController:
    def __init__(self, model):
        self.model = model

    def default_action(self):
        if self.model.get_dates():
            return self.model.get_dates()
        else:
            return "Нет данных!"

    def only_courses_list(self):
        courses = []
        data = self.model.get_dates()
        if data:
            for element in data:
                courses.append(element['course'])
        else:
            return "Предметов нет!"
        return courses

    def only_dates_list(self):
        dates = []
        data = self.model.get_dates()
        if data:
            for element in data:
                dates.append(element['date'])
        else:
            return "Оценок нет!"
        return dates

    def courses_dates(self):
        if self.model.get_dates():
            return self.only_courses_list(), self.only_dates_list()
        else:
            return "Предметов нет! Оценок нет!"

    def add_date(self, course, date, filename, validation):
        if validation in ['is_superuser', 'is_staff']:
            self.model.add_date(course, date, filename)
            return "Оценка успешно добавлена!"
        else:
            return "Нет доступа!"