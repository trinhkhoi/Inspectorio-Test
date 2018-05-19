from com.inspectorio.extracting_excel.utils import DBUtil as du

# insert a factory object to database
def insert_data(factory):
    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO factory(code, name, address, contacts) VALUES (%s, %s, %s, %s) RETURNING id")
    print('SQL INSERT: ', sql % factory.get_data())
    return du.insert(sql, factory.get_data())


# return a factory by code
def get_factory_by_code(code):
    # Prepare SQL query to get user location.
    sql = (
        "SELECT id FROM factory WHERE code = '%s'")
    results = du.execute(sql % code)
    return results