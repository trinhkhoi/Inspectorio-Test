from xlrd import open_workbook
from com.inspectorio.extracting_excel.respository import VendorRespository as vdRespository
from com.inspectorio.extracting_excel.respository import FactoryRespository as facRespository
from com.inspectorio.extracting_excel.respository import GeneralInfoRespository as genRespository
from com.inspectorio.extracting_excel.respository import PomInfoRespository as pomRespository
from com.inspectorio.extracting_excel.respository import PIFInfoRespository as pifRespository
from com.inspectorio.extracting_excel.respository import ItemInfoRespository as itemRespository
from com.inspectorio.extracting_excel.respository import SipElementRespository as sipRespository
from com.inspectorio.extracting_excel.utils import CommonUtil as cUtil
from com.inspectorio.extracting_excel.models.Vendor import Vendor
from com.inspectorio.extracting_excel.models.Factory import Factory
from com.inspectorio.extracting_excel.models.GeneralInfo import GeneralInfo
from com.inspectorio.extracting_excel.models.PomInfo import PomInfo
from com.inspectorio.extracting_excel.models.PifInfo import PifInfo
from com.inspectorio.extracting_excel.models.ItemInfo import ItemInfo
from com.inspectorio.extracting_excel.models.SipElement import SipElement


def read_excel_file(excel_file):
    wb = open_workbook(file_contents=excel_file.read())
    print('Load excel file successfully ------- ')
    vendor = Vendor()
    factory = Factory()
    general_info = GeneralInfo()
    pom_items = []
    pif_items = []
    items = []
    sip_elements = []
    for sheet in wb.sheets():
        print('sheet name: ', sheet.name)
        if sheet.name == 'Inspection Detail':
            vendor = get_vendor(sheet)
            factory = get_factory(sheet)
            general_info = get_general_info(sheet, wb.datemode)
            pom_items = get_pom_info(sheet)

        elif 'PIF Detail - FRI' == sheet.name:
            pif_items, items, sip_elements = extract_pif_detail_sheet(sheet, wb.datemode)

    # save extracted data to database
    store_data_extracted(vendor, factory, general_info, pom_items, pif_items, items, sip_elements)


# return vendor object which obtains from excel
def get_vendor(sheet):
    if sheet.cell(1, 1).value != '':
        vendor_code = cUtil.get_number_string(sheet.cell(1, 1).value)
        vendor_name = sheet.cell(1, 2).value
        vendor_contact = sheet.cell(2, 1).value
        vendor = Vendor(vendor_code, vendor_name, vendor_contact)
        return vendor
    else:
        raise Exception('Missing vendor information. Please check the vendor information!')


# return factory object which obtains from excel
def get_factory(sheet):
    if sheet.cell(3, 1).value != '':
        factory_code = cUtil.get_number_string(sheet.cell(3, 1).value)
        factory_name = sheet.cell(3, 2).value
        factory_address = sheet.cell(4, 1).value
        factory_contact = sheet.cell(5, 1).value
        factory = Factory(
            factory_code,
            factory_name,
            factory_address,
            factory_contact)
        return factory
    else:
        raise Exception('Missing factory information. Please check the factory information!')


# return general information which is extracted form excel file
def get_general_info(sheet, datemode):
    if sheet.cell(0, 1).value != '':
        date = cUtil.get_date(sheet.cell(0, 1).value, datemode)
        bpm_vendor = sheet.cell(1, 7).value
        level = sheet.cell(3, 5).value
        auditor = sheet.cell(6, 1).value
        general_info = GeneralInfo(bpm_vendor, auditor, level, date)
        return general_info
    else:
        raise Exception('Missing date of general information. Please check the date information!')


# return a list of pom_info objects
def get_pom_info(sheet):
    number_of_rows = sheet.nrows
    pom_items = []
    for row in range(12, number_of_rows):
        if sheet.cell(row, 0).value != '':
            vendor_pid = cUtil.get_number_string(sheet.cell(row, 0).value)
            dpci = cUtil.get_number_string(sheet.cell(row, 1).value)
            po_included = cUtil.get_number_string(sheet.cell(row, 2).value)
            insp_style = sheet.cell(row, 3).value
            po_qty = cUtil.get_number(sheet.cell(row, 4).value)
            available_qty = cUtil.get_number(sheet.cell(row, 5).value)
            description = sheet.cell(row, 6).value
            pwi = True
            if str(sheet.cell(row, 7).value).lower() == 'no':
                pwi = False

            pom_info = PomInfo(vendor_pid, dpci, po_included, insp_style, po_qty, available_qty, description, pwi)
            pom_items.append(pom_info)

    return pom_items


# extract PIF Detail - FRI sheet
def extract_pif_detail_sheet(sheet, datemode):
    number_of_rows = sheet.nrows
    pif_items = []
    items = []
    sip_elements = []

    for row in range(3, number_of_rows):
        pif_info = get_pif_info(sheet, row, datemode)
        if pif_info is not None:
            pif_items.append(pif_info)

        item_info = get_item_info(sheet, row)
        if item_info is not None:
            items.append(item_info)

        sip_element = get_sip_element(sheet, row)
        if sip_element is not None:
            sip_elements.append(sip_element)

    return pif_items, items, sip_elements


# extract pif info table
def get_pif_info(sheet, row, datemode):
    if sheet.cell(row, 0).value != '':
        print(sheet.cell(row, 0).value)
        vendor_pid = cUtil.get_number_string(sheet.cell(row, 0).value)
        po_number = cUtil.get_number_string(sheet.cell(row, 2).value)
        purpose = sheet.cell(row, 3).value
        ship_begin_date = cUtil.get_date(sheet.cell(row, 4).value, datemode)
        ship_end_date = cUtil.get_date(sheet.cell(row, 5).value, datemode)
        pif_info = PifInfo(vendor_pid, po_number, purpose, ship_begin_date, ship_end_date)
        return pif_info
    return None


# extract item info table
def get_item_info(sheet, row):
    if sheet.cell(row, 7).value != '':
        item = cUtil.get_number_string(sheet.cell(row, 7).value)
        item_description = sheet.cell(row, 8).value
        po_number = cUtil.get_number_string(sheet.cell(row, 9).value)
        order_qty = cUtil.get_number(sheet.cell(row, 10).value)
        available_qty = cUtil.get_number(sheet.cell(row, 11).value)
        vendor_pid = cUtil.get_number_string(sheet.cell(row, 12).value)
        assortment_item = sheet.cell(row, 13).value if sheet.cell(row, 13).value != '' else ''
        item_info = ItemInfo(item, item_description, po_number, order_qty, available_qty, vendor_pid, assortment_item)
        return item_info
    return None


# extract sip element table
def get_sip_element(sheet, row):
    if sheet.cell(row, 21).value != '':
        vendor_pid = str(int(sheet.cell(row, 21).value))
        ppr_document = cUtil.get_vailable(sheet.cell(row, 22).value)
        red_seal = cUtil.get_vailable(sheet.cell(row, 23).value)
        technical_spec = cUtil.get_vailable(sheet.cell(row, 24).value)
        final_item_form = cUtil.get_vailable(sheet.cell(row, 25).value)
        total_program_quantity = cUtil.get_vailable(sheet.cell(row, 26).value)
        color_standard = cUtil.get_vailable(sheet.cell(row, 27).value)
        production_color = cUtil.get_vailable(sheet.cell(row, 28).value)
        trim_accessories = cUtil.get_vailable(sheet.cell(row, 29).value)
        yellow_seal = cUtil.get_vailable(sheet.cell(row, 30).value)
        product_testing_result = cUtil.get_vailable(sheet.cell(row, 31).value)
        floor_ready_requirement = cUtil.get_vailable(sheet.cell(row, 32).value)
        retail_packaging_design = cUtil.get_vailable(sheet.cell(row, 33).value)
        carton_mark = cUtil.get_vailable(sheet.cell(row, 34).value)
        factory_internal_report = cUtil.get_vailable(sheet.cell(row, 35).value)
        tcps_report = cUtil.get_vailable(sheet.cell(row, 36).value)
        completed_packing_list = cUtil.get_vailable(sheet.cell(row, 37).value)

        sip_element = SipElement(vendor_pid, ppr_document, red_seal, technical_spec,
                             final_item_form, total_program_quantity, color_standard, production_color,
                             trim_accessories, yellow_seal, product_testing_result, floor_ready_requirement,
                             retail_packaging_design, carton_mark, factory_internal_report, tcps_report,
                             completed_packing_list)
        return sip_element
    return None


# save extracted data to database
def store_data_extracted(vendor, factory, general_info, pom_items, pif_items, items, sip_elements):
    # save vendor
    vendor_id = save_vendor_info(vendor)
    # save factory
    factory_id = save_factory_info(factory)
    # save general information
    general_id = save_general_info(general_info, vendor_id, factory_id)

    if general_id is not None and len(pom_items) > 0:
        pomRespository.insert_data(cUtil.build_list_data(pom_items, general_id))

    if general_id is not None and len(pif_items) > 0:
        pifRespository.insert_data(cUtil.build_list_data(pif_items, general_id))

    if general_id is not None and len(items) > 0:
        itemRespository.insert_data(cUtil.build_list_data(items, general_id))

    if general_id is not None and len(sip_elements) > 0:
        sipRespository.insert_data(cUtil.build_list_data(sip_elements, general_id))


# save vendor to database
def save_vendor_info(vendor):
    exist_vendors = vdRespository.get_vendor_by_code(vendor.code)
    if len(exist_vendors) > 0:
        vendor_id = exist_vendors[0]
        return vendor_id

    vendor_id = vdRespository.insert_data(vendor)
    print('vendor_id: ', vendor_id)
    return vendor_id


# save factory to database
def save_factory_info(factory):
    exist_factories = facRespository.get_factory_by_code(factory.code)
    if len(exist_factories) > 0:
        factory_id = exist_factories[0]
        return factory_id

    factory_id = facRespository.insert_data(factory)
    print('factory_id: ', factory_id)
    return factory_id


# save general info to database
def save_general_info(general_info, vendor_id, factory_id):
    general_info.vendor_id = vendor_id
    general_info.factory_id = factory_id
    general_id = genRespository.insert_data(general_info)
    print('general_id: ', general_id)
    return general_id