import xlrd
import datetime


def get_vailable(value):
    if value == 'Available':
        return True
    return False


def get_number_string(value):
    return str(get_number(value))

def get_number(value):
    return int(value)

# get date with format yyyy-mm-dd
def get_date(value, datemode):
    return datetime.datetime(*xlrd.xldate_as_tuple(value, datemode)).strftime("%Y-%m-%d")


def build_list_data(list_objects, general_id):
    results = []
    for obj in list_objects:
        obj.general_id = general_id
        results.append(obj.get_data())
    return results