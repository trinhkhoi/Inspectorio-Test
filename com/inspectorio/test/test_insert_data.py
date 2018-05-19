import unittest
from com.inspectorio.extracting_excel.models.Vendor import Vendor
from com.inspectorio.extracting_excel.models.Factory import Factory
from com.inspectorio.extracting_excel.respository import VendorRespository as vRespository
from com.inspectorio.extracting_excel.respository import FactoryRespository as facRespository
from django.db import connection

class VendorTest(unittest.TestCase):
    def setUp(self):
        connection.cursor().execute("CREATE TABLE vendor("
                                    "id SERIAL PRIMARY KEY NOT NULL,"
                                    "code CHAR(50),"
                                    "name TEXT,"
                                    "contacts VARCHAR(255));")

    def tearDown(self):
        connection.cursor().execute("DROP TABLE vendor;")

    def test_insert_data(self):
        vendor = Vendor('123456', 'name_test', 'contact_test')
        id = vRespository.insert_data(vendor)
        print('id: ', id)
        self.assertEquals(id, 1)


class FactoryTest(unittest.TestCase):
    def setUp(self):
        connection.cursor().execute("CREATE TABLE factory("
                                    "id SERIAL PRIMARY KEY NOT NULL,"
                                    "code CHAR(50),"
                                    "name TEXT,"
                                    "address VARCHAR(255),"
                                    "contacts VARCHAR(255));")

    def tearDown(self):
        connection.cursor().execute("DROP TABLE factory;")

    def test_insert_data(self):
        factory = Factory('123456', 'name_test', 'address_test', 'contact_test')
        id = facRespository.insert_data(factory)
        print('id: ', id)
        self.assertEquals(id, 1)