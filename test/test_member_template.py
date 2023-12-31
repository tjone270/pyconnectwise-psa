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

from connectwise_psa.models.member_template import MemberTemplate

class TestMemberTemplate(unittest.TestCase):
    """MemberTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MemberTemplate:
        """Test MemberTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MemberTemplate`
        """
        model = MemberTemplate()
        if include_optional:
            return MemberTemplate(
                info = {
                    'key' : ''
                    },
                admin_flag = True,
                agreement_invoicing_display_options = 'RemainOnInvoicingScreen',
                allow_expenses_entered_against_companies_flag = True,
                allow_in_cell_entry_on_time_sheet = True,
                auto_popup_quick_notes_with_stopwatch = True,
                auto_start_stopwatch = True,
                billable_forecast = 1.337,
                calendar = connectwise_psa.models.calendar_reference.CalendarReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                company_activity_tab_format = 'SummaryList',
                copy_column_layouts_and_filters = True,
                copy_pod_layouts = True,
                copy_shared_default_views = True,
                custom_fields = [
                    connectwise_psa.models.custom_field_value.CustomFieldValue(
                        caption = '', 
                        entry_method = 'Date', 
                        id = 56, 
                        number_of_decimals = 56, 
                        type = 'TextArea', 
                        value = connectwise_psa.models.value.value(), )
                    ],
                daily_capacity = 1.337,
                days_tolerance = 56,
                default_department = connectwise_psa.models.system_department_reference.SystemDepartmentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                default_location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                enable_mobile_flag = True,
                enter_time_against_company_flag = True,
                excluded_project_board_ids = [
                    56
                    ],
                excluded_service_board_ids = [
                    56
                    ],
                expense_approver = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                from_member_rec_id = 56,
                from_member_template_rec_id = 56,
                global_search_default_sort = 'None',
                global_search_default_ticket_filter = 'OpenRecords',
                hide_member_in_dispatch_portal_flag = True,
                hourly_cost = 1.337,
                hourly_rate = 1.337,
                id = 56,
                identifier = '',
                include_in_utilization_reporting_flag = True,
                invoice_screen_default_tab_format = 'ShowInvoicingTab',
                invoice_time_tab_format = 'SummaryList',
                invoicing_display_options = 'RemainOnInvoicingScreen',
                member_personas = [
                    56
                    ],
                minimum_hours = 1.337,
                partner_portal_flag = True,
                phone_source = '',
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
                report_card = connectwise_psa.models.report_card_reference.ReportCardReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                reports_to = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                require_expense_entry_flag = True,
                require_start_and_end_time_on_time_entry_flag = True,
                require_time_sheet_entry_flag = True,
                restrict_default_sales_territory_flag = True,
                restrict_default_warehouse_bin_flag = True,
                restrict_default_warehouse_flag = True,
                restrict_department_flag = True,
                restrict_location_flag = True,
                restrict_project_default_department_flag = True,
                restrict_project_default_location_flag = True,
                restrict_schedule_flag = True,
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
                security_location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                service_board_team_ids = [
                    56
                    ],
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
                structure_level = connectwise_psa.models.structure_reference.StructureReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                sts_user_admin_url = '',
                teams = [
                    56
                    ],
                template_description = '',
                time_approver = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                time_reminder_email_flag = True,
                time_sheet_start_date = '',
                time_zone = connectwise_psa.models.time_zone_setup_reference.TimeZoneSetupReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                title = '',
                toast_notification_flag = True,
                type = connectwise_psa.models.member_type_reference.MemberTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
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
            return MemberTemplate(
                identifier = '',
        )
        """

    def testMemberTemplate(self):
        """Test MemberTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
