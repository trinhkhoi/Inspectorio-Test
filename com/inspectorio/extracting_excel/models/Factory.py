
class Factory():
    def __init__(self, code=None, name=None, address=None, contact=None):
        self.code = code
        self.name = name
        self.address = address
        self.contact = contact

    def get_data(self):
        return (self.code, self.name, self.address, self.contact)