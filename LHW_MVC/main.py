from Model import TimeTableModel
from View import TimeTableView
from Controller import TimeTableController


if __name__ == '__main__':
    model = TimeTableModel()
    controller = TimeTableController(model)
    view = TimeTableView(controller)

    view.print_default_action()
    view.print_courses_list()
    view.print_dates_list()
    view.print_courses_dates()
    view.add_date('HTML', 'Feb 01', 'dates_file.json', 'is_staff')
    view.add_date('CSS', 'Apr 14', 'dates_file.json', 'is_staff')
    view.add_date('JavaScript', 'Jul 15', 'dates_file.json', 'is_staff')
    view.add_date('Python', 'Aug 30', 'dates_file.json', 'is_superuser')
    view.add_date('Django', 'Oct 20', 'dates_file.json')
    view.print_default_action()
    view.print_courses_list()
    view.print_dates_list()
    view.print_courses_dates()
