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

from connectwise_psa.models.graph_user_csv import GraphUserCsv

class TestGraphUserCsv(unittest.TestCase):
    """GraphUserCsv unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GraphUserCsv:
        """Test GraphUserCsv
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GraphUserCsv`
        """
        model = GraphUserCsv()
        if include_optional:
            return GraphUserCsv(
                account_enabled = True,
                address = '',
                city = '',
                country = '',
                department = '',
                display_name = '',
                employee_type = '',
                first_name = '',
                id = '',
                is_matched_contact = True,
                job_title = '',
                last_name = '',
                mail = '',
                manage_contact_name = '',
                manage_contact_rec_id = 56,
                manager = connectwise_psa.models.manager.Manager(
                    account_enabled = True, 
                    address = '', 
                    city = '', 
                    contact_rec_id = 56, 
                    country = '', 
                    date_entered_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    department = '', 
                    directory_roles = [
                        ''
                        ], 
                    display_name = '', 
                    employee_type = '', 
                    entered_by = '', 
                    fax = '', 
                    first_name = '', 
                    groups = [
                        ''
                        ], 
                    id = '', 
                    language = '', 
                    last_name = '', 
                    last_update_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    licenses = [
                        connectwise_psa.models.m365_license.M365License(
                            description = '', 
                            id = '', )
                        ], 
                    mail = '', 
                    mail_nickname = '', 
                    manager = connectwise_psa.models.manager.Manager(
                        account_enabled = True, 
                        address = '', 
                        city = '', 
                        contact_rec_id = 56, 
                        country = '', 
                        date_entered_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        department = '', 
                        display_name = '', 
                        employee_type = '', 
                        entered_by = '', 
                        fax = '', 
                        first_name = '', 
                        id = '', 
                        language = '', 
                        last_name = '', 
                        last_update_utc = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        mail = '', 
                        mail_nickname = '', 
                        manager_id = '', 
                        manager_id = '', 
                        microsoft_365_contact_rec_id = 56, 
                        mobile_phone = '', 
                        office = '', 
                        phone_number = '', 
                        postal_code = '', 
                        principal_name = '', 
                        proxy_addresses = [
                            ''
                            ], 
                        state = '', 
                        tenant_id = '', 
                        title = '', 
                        updated_by = '', 
                        usage_location = '', 
                        user_type = '', ), 
                    manager_id = '', 
                    manager_id = '', 
                    microsoft_365_contact_rec_id = 56, 
                    mobile_phone = '', 
                    office = '', 
                    phone_number = '', 
                    postal_code = '', 
                    principal_name = '', 
                    proxy_addresses = [
                        ''
                        ], 
                    state = '', 
                    tenant_id = '', 
                    title = '', 
                    updated_by = '', 
                    usage_location = '', 
                    user_type = '', ),
                mobile_phone = '',
                nick_name = '',
                postal_code = '',
                principal_name = '',
                proxy_addresses = [
                    ''
                    ],
                state = ''
            )
        else:
            return GraphUserCsv(
        )
        """

    def testGraphUserCsv(self):
        """Test GraphUserCsv"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
