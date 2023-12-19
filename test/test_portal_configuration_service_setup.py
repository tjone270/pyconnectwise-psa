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

from connectwise_psa.models.portal_configuration_service_setup import PortalConfigurationServiceSetup

class TestPortalConfigurationServiceSetup(unittest.TestCase):
    """PortalConfigurationServiceSetup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PortalConfigurationServiceSetup:
        """Test PortalConfigurationServiceSetup
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PortalConfigurationServiceSetup`
        """
        model = PortalConfigurationServiceSetup()
        if include_optional:
            return PortalConfigurationServiceSetup(
                info = {
                    'key' : ''
                    },
                actual_hours_flag = True,
                approval_status_flag = True,
                assigned_resources_flag = True,
                budget_hours_flag = True,
                closed_tasks_flag = True,
                contact_flag = True,
                display_closed_tickets_option = 'DoNotDisplay',
                enable_chat_assist_flag = True,
                entered_date_flag = True,
                fixed_fee_ticket_template = connectwise_psa.models.service_signoff_reference.ServiceSignoffReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                id = 56,
                last_update_flag = True,
                open_tasks_flag = True,
                required_date_flag = True,
                service_board_flag = True,
                service_sub_type_flag = True,
                service_sub_type_item_flag = True,
                service_type_flag = True,
                site_name_flag = True,
                sla_info_flag = True,
                status_flag = True,
                time_materials_ticket_template = connectwise_psa.models.service_signoff_reference.ServiceSignoffReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return PortalConfigurationServiceSetup(
                display_closed_tickets_option = 'DoNotDisplay',
        )
        """

    def testPortalConfigurationServiceSetup(self):
        """Test PortalConfigurationServiceSetup"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
