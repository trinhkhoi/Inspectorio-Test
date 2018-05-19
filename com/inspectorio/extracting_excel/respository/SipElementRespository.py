from com.inspectorio.extracting_excel.utils import DBUtil as du


def insert_data(list_sip_elements):
    # Prepare SQL query to INSERT a record into the database.
    sql = ("INSERT INTO sip_elements(general_id, vendor_pid, ppr_document, red_seal, technical_spec, final_item_form, "
                        "total_program_quantity, color_standard, production_color, trim_accessories, yellow_seal, "
                        "product_testing_result, floor_ready_requirement, retail_packaging_design, carton_mark, "
                        "factory_internal_report, tcps_report, completed_packing_list) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
    du.insert_many(sql, list_sip_elements)
