from Models import MarksModel, TimetableModel
from Controller import Controller
from View import View

marks_model = MarksModel()
timetable_model = TimetableModel()

marks_controller = Controller(marks_model)
timetable_controller = Controller(timetable_model)

marks_view = View(marks_controller)
timetable_view = View(timetable_controller)

marks_controller.add_data('HTML', 'B+', 'marks_data')
timetable_controller.add_data('HTML', 'Feb 01', 'timetable_data')

marks_controller.add_data('CSS', 'A+', 'marks_data')
timetable_controller.add_data('CSS', 'Aug 14', 'timetable_data')

marks_controller.add_data('JS', 'A', 'marks_data')
timetable_controller.add_data('JS', 'Nov 21', 'timetable_data')

marks_controller.add_data('Python', 'A+', 'marks_data')
timetable_controller.add_data('Python', 'Mar 26', 'timetable_data')

print("Marks")
marks_view.print_data_list()
print()
print("Timetable")
timetable_view.print_data_list()
