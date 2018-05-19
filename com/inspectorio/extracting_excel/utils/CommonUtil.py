import xlrd
import datetime
import logging

logger = logging.getLogger(__name__)


def get_vailable(value):
    if value == 'Available':
        return True
    return False


def get_number_string(sheet, row, col):
    return str(get_number(sheet, row, col))


def get_number(sheet, row, col):
    try:
        result = int(sheet.cell(row, col).value)
        return result
    except Exception as ex:
        logger.exception(str(ex))
        raise_message_error(sheet.cell(row, col).value, sheet.name, row, col)


# get date with format yyyy-mm-dd
def get_date(sheet, row, col, datemode):
    try:
        result = datetime.datetime(*xlrd.xldate_as_tuple(sheet.cell(row, col).value, datemode)).strftime("%Y-%m-%d")
        return result
    except Exception as ex:
        logger.exception(str(ex))
        raise_message_error(sheet.cell(row, col).value, sheet.name, row, col)


def build_list_data(list_objects, general_id):
    try:
        results = []
        for obj in list_objects:
            obj.general_id = general_id
            results.append(obj.get_data())
        return results
    except Exception as ex:
        logger.exception(str(ex))


def raise_message_error(value, sheet_name, row, col):
    raise Exception('Error data {%s} at sheet {%s}; row {%s}; column {%s}. Please to check it !' %
                    (value, sheet_name, row, col))
