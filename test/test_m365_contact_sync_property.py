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

from connectwise_psa.models.m365_contact_sync_property import M365ContactSyncProperty

class TestM365ContactSyncProperty(unittest.TestCase):
    """M365ContactSyncProperty unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> M365ContactSyncProperty:
        """Test M365ContactSyncProperty
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `M365ContactSyncProperty`
        """
        model = M365ContactSyncProperty()
        if include_optional:
            return M365ContactSyncProperty(
                info = {
                    'key' : ''
                    },
                company_rec_id = 56,
                exclude_include_flag = True,
                id = 56,
                include_exclude_type = 'All',
                property_type = 'City',
                wild_card = ''
            )
        else:
            return M365ContactSyncProperty(
        )
        """

    def testM365ContactSyncProperty(self):
        """Test M365ContactSyncProperty"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
