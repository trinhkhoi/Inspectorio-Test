
class GeneralInfo():
    def __init__(self, bpm_vendor=None, auditor=None, level=None, date=None):
        self.bpm_vendor = bpm_vendor
        self.auditor = auditor
        self.level = level
        self.date = date
        self.vendor_id = None
        self.factory_id = None

    def get_data(self):
        return (self.vendor_id, self.factory_id, self.bpm_vendor, self.auditor, self.level, self.date)