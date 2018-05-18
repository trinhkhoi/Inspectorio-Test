from com.inspectorio.test.utils import DBUtil as du


def insert_data(list_sip_elements):
    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO sip_elements(general_id, vendor_pid, ppr_document, red_seal, technical_spec, final_item_form, "
                        "total_program_quantity, color_standard, production_color, trim_accessories, yellow_seal, "
                        "product_testing_result, floor_ready_requirement, retail_packaging_design, carton_mark, "
                        "factory_internal_report, tcps_report, completed_packing_list) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    du.insert_many(sql, list_sip_elements)


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