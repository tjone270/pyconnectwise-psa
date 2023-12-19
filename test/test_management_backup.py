# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from connectwise_psa.models.management_backup import ManagementBackup

class TestManagementBackup(unittest.TestCase):
    """ManagementBackup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagementBackup:
        """Test ManagementBackup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagementBackup`
        """
        model = ManagementBackup()
        if include_optional:
            return ManagementBackup(
                info = {
                    'key' : ''
                    },
                billing_level = 'Detail',
                id = 56,
                item = connectwise_psa.models.catalog_item_reference.CatalogItemReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                type = connectwise_psa.models.agreement_type_reference.AgreementTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return ManagementBackup(
                billing_level = 'Detail',
        )
        """

    def testManagementBackup(self):
        """Test ManagementBackup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
