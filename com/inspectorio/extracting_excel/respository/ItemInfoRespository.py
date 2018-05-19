from com.inspectorio.extracting_excel.utils import DBUtil as du


def insert_data(list_items):
    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO item_info(general_id, item, item_description, po_number, order_qty, available_qty, vendor_pid, "
           "assortment_items) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    du.insert_many(sql, list_items)
