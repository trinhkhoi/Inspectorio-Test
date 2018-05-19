
class Vendor():
    def __init__(self, code=None, name=None, contact=None):
        self.code = code
        self.name = name
        self.contact = contact

    def get_data(self):
        return (self.code, self.name, self.contact)