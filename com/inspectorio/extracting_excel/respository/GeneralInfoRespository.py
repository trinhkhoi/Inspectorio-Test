from com.inspectorio.extracting_excel.utils import DBUtil as du


def insert_data(general_info):
    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO general_info(vendor_id, factory_id, bmp_vendor, auditor, frm_level, date_created) VALUES (%s, %s, %s, %s, %s, %s)  RETURNING id")
    print('SQL INSERT: ', sql % general_info.get_data())
    return du.insert(sql, general_info.get_data())
