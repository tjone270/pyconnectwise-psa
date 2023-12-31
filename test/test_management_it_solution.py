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

from connectwise_psa.models.management_it_solution import ManagementItSolution

class TestManagementItSolution(unittest.TestCase):
    """ManagementItSolution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ManagementItSolution:
        """Test ManagementItSolution
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManagementItSolution`
        """
        model = ManagementItSolution()
        if include_optional:
            return ManagementItSolution(
                info = {
                    'key' : ''
                    },
                continuum_api_password = '',
                continuum_api_username = '',
                global_login_flag = True,
                global_login_password = '',
                global_login_username = '',
                id = 56,
                level_api_password = '',
                level_api_username = '',
                level_var_domain = '',
                management_it_solution_type = 'LevelPlatforms',
                management_server_url = '',
                management_solution_name = '',
                n_able_password = '',
                n_able_username = '',
                name = '',
                no_display_flag = True,
                override_login_location_flag = True,
                override_web_service_location_flag = True,
                portal_override_login_url = '',
                using_ssl_flag = True,
                webservice_override_url = ''
            )
        else:
            return ManagementItSolution(
                management_it_solution_type = 'LevelPlatforms',
                name = '',
        )
        """

    def testManagementItSolution(self):
        """Test ManagementItSolution"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
