
class ItemInfo():
    def __init__(self, item=None, item_description=None, po_number=None, order_qty=None, available_qty=None,
                 vendor_pid=None, assortment_item=None):
        self.general_id = None
        self.item = item
        self.item_description = item_description
        self.po_number = po_number
        self.order_qty = order_qty
        self.available_qty = available_qty
        self.vendor_pid = vendor_pid
        self.assortment_item = assortment_item

    def get_data(self):
        return (self.general_id, self.item, self.item_description, self.po_number, self.order_qty, self.available_qty,
                self.vendor_pid, self.assortment_item)