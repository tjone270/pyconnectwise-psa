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

from connectwise_psa.models.company_management_summary import CompanyManagementSummary

class TestCompanyManagementSummary(unittest.TestCase):
    """CompanyManagementSummary unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyManagementSummary:
        """Test CompanyManagementSummary
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyManagementSummary`
        """
        model = CompanyManagementSummary()
        if include_optional:
            return CompanyManagementSummary(
                info = {
                    'key' : ''
                    },
                agreement = connectwise_psa.models.agreement_reference.AgreementReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    type = '', ),
                alerts_generated = '',
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                cpu_utilization = 1.337,
                device_type = 'WorkstationsAndServers',
                disk_cleanups = 56,
                disk_defragmentations = 56,
                disk_space_cleaned_mb = 56,
                failed_backup_jobs = 56,
                fully_patched_machines = 56,
                group_identifier = '',
                id = 56,
                internet_connectivity = 1.337,
                management_solution = connectwise_psa.models.management_solution_reference.ManagementSolutionReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    setup_name = '', ),
                memory_utilization = 1.337,
                missing_more_five_patches_machines = 56,
                missing_one_two_patches_machines = 56,
                missing_security_patches = '',
                missing_three_five_patches_machines = 56,
                missing_unscanned_patches_machines = 56,
                server_availability = 56,
                servers_disk_space_low = 56,
                servers_offline = 56,
                snmp_machines = 56,
                spyware_items_removed = 56,
                successful_backup_jobs = 56,
                total_managed_machines = 56,
                total_notifications = 56,
                total_servers = 56,
                total_windows_servers = 56,
                total_windows_workstations = 56,
                total_workstations = 56,
                viruses_removed = 56,
                windows_patches_installed = 56
            )
        else:
            return CompanyManagementSummary(
                group_identifier = '',
        )
        """

    def testCompanyManagementSummary(self):
        """Test CompanyManagementSummary"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()