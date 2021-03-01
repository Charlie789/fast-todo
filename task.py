class Task:
    def __init__(self, title, isComplited=False):
        self.title = title
        self.isComplited = isComplited

    def complete_task(self):
        self.isComplited = True

    def incomplete_task(self):
        self.isComplited = False