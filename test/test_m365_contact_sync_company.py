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

from connectwise_psa.models.m365_contact_sync_company import M365ContactSyncCompany

class TestM365ContactSyncCompany(unittest.TestCase):
    """M365ContactSyncCompany unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> M365ContactSyncCompany:
        """Test M365ContactSyncCompany
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `M365ContactSyncCompany`
        """
        model = M365ContactSyncCompany()
        if include_optional:
            return M365ContactSyncCompany(
                info = {
                    'key' : ''
                    },
                are_all_microsoft365_contact_sync_inactive = True,
                company_id = '',
                company_rec_id = 56,
                contacts = [
                    connectwise_psa.models.graph_user_csv.Graph_User_Csv(
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
                        state = '', )
                    ],
                display_name = '',
                id = 56,
                inactive_flag_tenant = True,
                m365_tenant = connectwise_psa.models.m365_tenant.M365Tenant(
                    id = '', 
                    name = '', ),
                parent_tenant_id = '',
                sync_flag = True,
                tenant_id = ''
            )
        else:
            return M365ContactSyncCompany(
        )
        """

    def testM365ContactSyncCompany(self):
        """Test M365ContactSyncCompany"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
