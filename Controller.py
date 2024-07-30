class Controller:

    def __init__(self, model):
        self.model = model

    def show_model_as_list(self):
        return self.model.get_data()

    def add_data(self, course, data, filename):
        self.model.add_data(course, data, filename)
