from com.inspectorio.extracting_excel.utils import DBUtil as du
from com.inspectorio.extracting_excel.models import Vendor

# insert a vendor object to database
def insert_data(vendor):
    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO vendor(code, name, contacts) VALUES (%s, %s, %s) RETURNING id;")
    print('SQL INSERT: ', sql % vendor.get_data())
    return du.insert(sql, vendor.get_data())


# return a vendor by code
def get_vendor_by_code(code):
    sql = (
        "SELECT id FROM vendor WHERE code = '%s'")
    results = du.execute(sql % code)
    return results