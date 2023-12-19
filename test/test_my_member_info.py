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

from connectwise_psa.models.my_member_info import MyMemberInfo

class TestMyMemberInfo(unittest.TestCase):
    """MyMemberInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MyMemberInfo:
        """Test MyMemberInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MyMemberInfo`
        """
        model = MyMemberInfo()
        if include_optional:
            return MyMemberInfo(
                info = {
                    'key' : ''
                    },
                allow_expenses_entered_against_companies_flag = True,
                daily_capacity = 1.337,
                default_department = connectwise_psa.models.system_department_reference.SystemDepartmentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                default_email = '',
                default_location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                enter_time_against_company_flag = True,
                excluded_project_board_ids = [
                    56
                    ],
                excluded_service_board_ids = [
                    56
                    ],
                first_name = '',
                full_name = '',
                id = 56,
                identifier = '',
                inactive_flag = True,
                last_name = '',
                license_class = 'A',
                middle_initial = '',
                photo = connectwise_psa.models.document_reference.DocumentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                project_default_board = connectwise_psa.models.project_board_reference.ProjectBoardReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                project_default_department = connectwise_psa.models.system_department_reference.SystemDepartmentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                project_default_location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                require_expense_entry_flag = True,
                require_start_and_end_time_on_time_entry_flag = True,
                require_time_sheet_entry_flag = True,
                restrict_default_warehouse_bin_flag = True,
                restrict_default_warehouse_flag = True,
                restrict_project_default_department_flag = True,
                restrict_project_default_location_flag = True,
                restrict_service_default_department_flag = True,
                restrict_service_default_location_flag = True,
                sales_default_location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                schedule_capacity = 1.337,
                schedule_default_department = connectwise_psa.models.system_department_reference.SystemDepartmentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                schedule_default_location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                service_default_board = connectwise_psa.models.board_reference.BoardReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                service_default_department = connectwise_psa.models.system_department_reference.SystemDepartmentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                service_default_location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                service_location = connectwise_psa.models.service_location_reference.ServiceLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                sso_client_id = '',
                sso_session_flag = True,
                time_zone = connectwise_psa.models.time_zone_setup_reference.TimeZoneSetupReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                use_browser_language_flag = True,
                warehouse = connectwise_psa.models.warehouse_reference.WarehouseReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    locked_flag = True, 
                    name = '', ),
                warehouse_bin = connectwise_psa.models.warehouse_bin_reference.WarehouseBinReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                work_role = connectwise_psa.models.work_role_reference.WorkRoleReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                work_type = connectwise_psa.models.work_type_reference.WorkTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return MyMemberInfo(
        )
        """

    def testMyMemberInfo(self):
        """Test MyMemberInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()