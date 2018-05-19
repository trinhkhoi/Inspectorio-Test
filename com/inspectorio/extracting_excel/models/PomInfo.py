
class PomInfo():
    def __init__(self, vendor_pid=None, dpci=None, po_included=None, insp_style=None, po_qty=None,
                 available_qty=None, description=None, pwi=False):
        self.general_id = None
        self.vendor_pid = vendor_pid
        self.dpci = dpci
        self.po_included = po_included
        self.insp_style = insp_style
        self.po_qty = po_qty
        self.available_qty = available_qty
        self.description = description
        self.pwi =pwi

    def get_data(self):
        return (self.general_id, self.vendor_pid, self.dpci, self.po_included, self.insp_style, self.po_qty,
                self.available_qty, self.description, self.pwi)