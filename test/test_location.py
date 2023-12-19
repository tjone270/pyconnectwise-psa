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

from connectwise_psa.models.location import Location

class TestLocation(unittest.TestCase):
    """Location unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Location:
        """Test Location
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Location`
        """
        model = Location()
        if include_optional:
            return Location(
                info = {
                    'key' : ''
                    },
                calendar = connectwise_psa.models.calendar_reference.CalendarReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                client_flag = True,
                department_ids = [
                    56
                    ],
                id = 56,
                location_flag = True,
                manager = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                name = '',
                override_address_line1 = '',
                override_address_line2 = '',
                override_city = '',
                override_country = connectwise_psa.models.country_reference.CountryReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                override_fax_number = '',
                override_phone_number = '',
                override_state = '',
                override_zip = '',
                owa_url = '',
                owner_level_id = 56,
                payroll_xref = '',
                reports_to = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                sales_rep = '',
                structure_level = connectwise_psa.models.corporate_structure_level_reference.CorporateStructureLevelReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                time_zone_setup = connectwise_psa.models.time_zone_setup_reference.TimeZoneSetupReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                work_role_ids = [
                    56
                    ]
            )
        else:
            return Location(
                name = '',
        )
        """

    def testLocation(self):
        """Test Location"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
