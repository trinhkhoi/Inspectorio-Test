from com.inspectorio.test.utils import DBUtil as du


def insert_data(vendor_id, factory_id, bmp_vendor, auditor, frm_level, date_created):
    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO general_info(vendor_id, factory_id, bmp_vendor, auditor, frm_level, date_created) VALUES (%s, %s, %s, %s, %s, %s)  RETURNING id")
    print('SQL INSERT: ', sql % (vendor_id, factory_id, bmp_vendor, auditor, frm_level, date_created))
    return du.insert(sql, (vendor_id, factory_id, bmp_vendor, auditor, frm_level, date_created))


def get_user_location(user_uid):
    # Prepare SQL query to get user location.
    sql = (
        "SELECT JSON_EXTRACT(A.data, '$.time.datetime') AS datetime, JSON_EXTRACT(A.data, '$.time.timestamp') AS timestamp, "
            "JSON_EXTRACT(A.data, '$.location.lat') AS lat, JSON_EXTRACT(A.data, '$.location.lon') AS lon, "
            " JSON_EXTRACT(A.data, '$.location.speed') AS speed "
        "FROM activities as A WHERE user = %s AND action = 'geolocation' "
        "ORDER BY updated_at DESC limit 1")
    results = du.execute(sql % user_uid)
    return results


def get_all_new_geolocation():
    # Prepare SQL query to get user location.
    sql = (
        "SELECT DISTINCT JSON_EXTRACT(A.data, '$.location.lat') AS lat, JSON_EXTRACT(A.data, '$.location.lon') AS lon "
        "FROM activities as A WHERE action = 'geolocation' "
        "AND JSON_EXTRACT(A.data, '$.location.lat') NOT IN (SELECT lat FROM geolocation) "
        "AND JSON_EXTRACT(A.data, '$.location.lon') NOT IN (SELECT lng FROM geolocation)")
    results = du.execute(sql)
    return results


def get_all_geolocation():
    # Prepare SQL query to get user location.
    sql = (
        "SELECT DISTINCT JSON_EXTRACT(A.data, '$.location.lat') AS lat, JSON_EXTRACT(A.data, '$.location.lon') AS lon "
        "FROM activities as A WHERE action = 'geolocation'")
    results = du.execute(sql)
    return results