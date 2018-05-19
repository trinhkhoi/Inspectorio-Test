
class PifInfo():
    def __init__(self, vendor_pid=None, po_number=None, purpose=None, ship_begin_date=None, ship_end_date=None):
        self.general_id = None
        self.vendor_pid = vendor_pid
        self.po_number = po_number
        self.purpose = purpose
        self.ship_begin_date = ship_begin_date
        self.ship_end_date = ship_end_date

    def get_data(self):
        return (self.general_id, self.vendor_pid, self.po_number, self.purpose, self.ship_begin_date, self.ship_end_date)