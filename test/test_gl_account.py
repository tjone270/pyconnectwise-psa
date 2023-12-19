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

from connectwise_psa.models.gl_account import GLAccount

class TestGLAccount(unittest.TestCase):
    """GLAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GLAccount:
        """Test GLAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GLAccount`
        """
        model = GLAccount()
        if include_optional:
            return GLAccount(
                info = {
                    'key' : ''
                    },
                cogs1 = '',
                cogs10 = '',
                cogs2 = '',
                cogs3 = '',
                cogs4 = '',
                cogs5 = '',
                cogs6 = '',
                cogs7 = '',
                cogs8 = '',
                cogs9 = '',
                gl_type = 'AP',
                id = 56,
                inventory = '',
                mapped_record = connectwise_psa.models.mapped_record_reference.MappedRecordReference(
                    id = 56, 
                    name = '', ),
                mapped_type = connectwise_psa.models.mapped_type_reference.MappedTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                product_id = '',
                sales_code = '',
                segment1 = '',
                segment10 = '',
                segment2 = '',
                segment3 = '',
                segment4 = '',
                segment5 = '',
                segment6 = '',
                segment7 = '',
                segment8 = '',
                segment9 = ''
            )
        else:
            return GLAccount(
                gl_type = 'AP',
                mapped_record = connectwise_psa.models.mapped_record_reference.MappedRecordReference(
                    id = 56, 
                    name = '', ),
                mapped_type = connectwise_psa.models.mapped_type_reference.MappedTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
        )
        """

    def testGLAccount(self):
        """Test GLAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()