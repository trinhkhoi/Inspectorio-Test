from xlrd import open_workbook
import xlrd
import datetime
from com.inspectorio.test.respository import VendorRespository as vdRespository
from com.inspectorio.test.respository import FactoryRespository as facRespository
from com.inspectorio.test.respository import GeneralInfoRespository as genRespository
from com.inspectorio.test.respository import PomInfoRespository as pomRespository
from com.inspectorio.test.respository import PIFInfoRespository as pifRespository
from com.inspectorio.test.respository import ItemInfoRespository as itemRespository
from com.inspectorio.test.respository import SipElementRespository as sipRespository


def read_excel_file(path):
    wb = open_workbook(path)
    print('Load excel file successfully ------- ')
    general_id = None
    for sheet in wb.sheets():
        print('sheet name: ', sheet.name)
        if sheet.name == 'Inspection Detail':
            date = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell(0, 1).value, wb.datemode)).strftime("%Y-%m-%d")
            vendor_code = str(int(sheet.cell(1, 1).value))
            vendor_name = sheet.cell(1, 2).value
            bpm_vendor = sheet.cell(1, 7).value
            vendor_contact = sheet.cell(2, 1).value
            factory_code = str(int(sheet.cell(3, 1).value))
            factory_name = sheet.cell(3, 2).value
            factory_address = sheet.cell(4,1).value
            factory_contact = sheet.cell(5,1).value
            level = sheet.cell(3, 5).value
            auditor = sheet.cell(6,1).value

            vendor_id = vdRespository.insert_data(vendor_code, vendor_name, vendor_contact)
            print('vendor_id: ', vendor_id)
            factory_id = facRespository.insert_data(factory_code, factory_name, factory_address, factory_contact)
            print('factory_id: ', factory_id)
            general_id = genRespository.insert_data(vendor_id, factory_id, bpm_vendor, auditor, level, date)
            print('general_id: ', general_id)

            number_of_rows = sheet.nrows
            pom_items = []
            for row in range(12, number_of_rows):
                if sheet.cell(row, 0).value != '':
                    vendor_pid = str(int(sheet.cell(row, 0).value))
                    dpci = str(int(sheet.cell(row, 1).value))
                    po_included = str(int(sheet.cell(row, 2).value))
                    insp_style = sheet.cell(row, 3).value
                    po_qty = int(sheet.cell(row, 4).value)
                    available_qty = int(sheet.cell(row, 5).value)
                    description = sheet.cell(row, 6).value
                    pwi = True
                    if str(sheet.cell(row, 7).value).lower() == 'no':
                        pwi = False

                    pom_items.append((general_id, vendor_pid, dpci, po_included, insp_style, po_qty, available_qty,
                                               description, pwi))

            if len(pom_items) > 0:
                pomRespository.insert_data(pom_items)
        elif 'PIF Detail - FRI' == sheet.name and general_id is not None:
            number_of_rows = sheet.nrows
            print(sheet.name, ': ', number_of_rows)
            pif_items = []
            items = []
            sip_elements = []
            for row in range(3, number_of_rows):
                if sheet.cell(row, 0).value != '':
                    print(sheet.cell(row, 0).value)
                    vendor_pid = str(int(sheet.cell(row, 0).value))
                    po_number = str(int(sheet.cell(row, 2).value))
                    purpose = str(sheet.cell(row, 3).value)
                    ship_begin_date = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell(row, 4).value, wb.datemode)).strftime("%Y-%m-%d")
                    ship_end_date = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell(row, 5).value, wb.datemode)).strftime("%Y-%m-%d")
                    pif_items.append((general_id, vendor_pid, po_number, purpose, ship_begin_date, ship_end_date))
                
                if sheet.cell(row, 7).value != '':
                    item = str(int(sheet.cell(row, 7).value))
                    item_description = sheet.cell(row, 8).value
                    po_number = str(int(sheet.cell(row, 9).value))
                    order_qty = int(sheet.cell(row, 10).value)
                    available_qty = int(sheet.cell(row, 11).value)
                    vendor_pid = str(int(sheet.cell(row, 12).value))
                    assortment_item = sheet.cell(row, 13).value if sheet.cell(row, 13).value != '' else ''
                    items.append((general_id, item, item_description, po_number, order_qty, available_qty, vendor_pid, assortment_item))
                    
                if sheet.cell(row, 21).value != '':
                    vendor_pid = str(int(sheet.cell(row, 21).value))
                    ppr_document = True
                    red_seal = True
                    technical_spec = True
                    final_item_form = True
                    total_program_quantity = True
                    color_standard = True
                    production_color = True
                    trim_accessories = True
                    yellow_seal = True
                    product_testing_result = True
                    floor_ready_requirement = True
                    retail_packaging_design = True
                    carton_mark = True
                    factory_internal_report = True
                    tcps_report = True
                    completed_packing_list = True

                    # check ppr document
                    if sheet.cell(row, 22).value != 'Available':
                        ppr_document = False

                    # check red seal sample
                    if sheet.cell(row, 23).value != 'Available':
                        red_seal = False

                    # check technical specs and construction
                    if sheet.cell(row, 24).value != 'Available':
                        technical_spec = False

                    # check final item set-up form
                    if sheet.cell(row, 25).value != 'Available':
                        final_item_form = False

                    # check total program quantity and deliveries
                    if sheet.cell(row, 26).value != 'Available':
                        total_program_quantity = False

                    # check color standards
                    if sheet.cell(row, 27).value != 'Available':
                        color_standard = False

                    # check production color/finish representation
                    if sheet.cell(row, 28).value != 'Available':
                        production_color = False

                    # check trims, accessories, hardwares, components and labeling
                    if sheet.cell(row, 29).value != 'Available':
                        trim_accessories = False

                    # check yellow seal sample
                    if sheet.cell(row, 30).value != 'Available':
                        yellow_seal = False

                    # check product testing results
                    if sheet.cell(row, 31).value != 'Available':
                        product_testing_result = False

                    # check floor ready requirements
                    if sheet.cell(row, 32).value != 'Available':
                        floor_ready_requirement = False

                    # check retail packing design sample
                    if sheet.cell(row, 33).value != 'Available':
                        retail_packaging_design = False

                    # check carton marks and labels
                    if sheet.cell(row, 34).value != 'Available':
                        carton_mark = False

                    # check factory internal report - inspection and testing
                    if sheet.cell(row, 35).value != 'Available':
                        factory_internal_report = False

                    # check tcps inspection report
                    if sheet.cell(row, 36).value != 'Available':
                        tcps_report = False

                    # check completed packing list
                    if sheet.cell(row, 37).value != 'Available':
                        completed_packing_list = False

                    sip_elements.append((general_id, vendor_pid, ppr_document, red_seal, technical_spec, final_item_form,
                                         total_program_quantity, color_standard, production_color, trim_accessories, yellow_seal,
                                         product_testing_result, floor_ready_requirement, retail_packaging_design,
                                         carton_mark, factory_internal_report, tcps_report, completed_packing_list))

            print(pif_items)
            if len(pif_items) > 0:
                pifRespository.insert_data(pif_items)

            print(items)
            if len(items) > 0:
                itemRespository.insert_data(items)

            print(sip_elements)
            if len(sip_elements) > 0:
                sipRespository.insert_data(sip_elements)