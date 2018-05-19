from com.inspectorio.extracting_excel.utils import DBUtil as du


def insert_data(list_pom_items):
    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO pom_info(general_id, vendor_pid, dpci, po_included, insp_type, po_qty, available_qty, description, is_pwi) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
    du.insert_many(sql, list_pom_items)
