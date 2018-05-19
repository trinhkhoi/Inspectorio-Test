from com.inspectorio.extracting_excel.utils import DBUtil as du


def insert_data(list_pifs):
    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO pif_info(general_id, vendor_pid, po_number, purpose, ship_begin_date, ship_end_date) VALUES (%s, %s, %s, %s, %s, %s)")
    du.insert_many(sql, list_pifs)
