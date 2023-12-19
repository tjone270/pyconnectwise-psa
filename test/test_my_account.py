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

from connectwise_psa.models.my_account import MyAccount

class TestMyAccount(unittest.TestCase):
    """MyAccount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MyAccount:
        """Test MyAccount
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MyAccount`
        """
        model = MyAccount()
        if include_optional:
            return MyAccount(
                info = {
                    'key' : ''
                    },
                agreement_invoicing_display_options = 'RemainOnInvoicingScreen',
                allow_expenses_entered_against_companies_flag = True,
                allow_in_cell_entry_on_time_sheet = True,
                authentication_service_type = 'AuthAnvil',
                auto_popup_quick_notes_with_stopwatch = True,
                auto_start_stopwatch = True,
                billable_forecast = 1.337,
                calendar = connectwise_psa.models.calendar_reference.CalendarReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                calendar_sync_integration_flag = True,
                client_id = '',
                company_activity_tab_format = 'SummaryList',
                copy_column_layouts_and_filters = True,
                copy_pod_layouts = True,
                copy_shared_default_views = True,
                country = connectwise_psa.models.country_reference.CountryReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
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
                default_email = 'Office',
                default_location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                default_phone = 'Office',
                directional_sync = connectwise_psa.models.directional_sync_reference.DirectionalSyncReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                disable_online_flag = True,
                employee_identifer = '',
                enable_mobile_flag = True,
                enable_mobile_gps_flag = True,
                enter_time_against_company_flag = True,
                expense_approver = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                first_name = '',
                from_member_rec_id = 56,
                global_search_default_sort = 'None',
                global_search_default_ticket_filter = 'OpenRecords',
                hide_member_in_dispatch_portal_flag = True,
                hire_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                home_email = '',
                home_extension = '',
                home_phone = '',
                id = 56,
                identifier = '',
                inactive_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                inactive_flag = True,
                include_in_utilization_reporting_flag = True,
                invoice_screen_default_tab_format = 'ShowInvoicingTab',
                invoice_time_tab_format = 'SummaryList',
                invoicing_display_options = 'RemainOnInvoicingScreen',
                last_login = '',
                last_name = '',
                license_class = 'A',
                mapi_name = '',
                member_personas = [
                    56
                    ],
                middle_initial = '',
                minimum_hours = 1.337,
                mobile_email = '',
                mobile_extension = '',
                mobile_phone = '',
                notes = '',
                office365 = connectwise_psa.models.member_office365.MemberOffice365(
                    id = '', 
                    name = '', ),
                office_email = '',
                office_extension = '',
                office_phone = '',
                partner_portal_flag = True,
                password = '',
                phone_integration_type = 'TAPI',
                phone_source = '',
                photo = connectwise_psa.models.document_reference.DocumentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                primary_email = '',
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
                signature = '',
                sts_user_admin_url = '',
                time_approver = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                time_reminder_email_flag = True,
                time_sheet_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                time_zone = connectwise_psa.models.time_zone_setup_reference.TimeZoneSetupReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                timebased_one_time_password_activated = True,
                title = '',
                toast_notification_flag = True,
                token = '',
                type = connectwise_psa.models.member_type_reference.MemberTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                use_browser_language_flag = True,
                vendor_number = '',
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
            return MyAccount(
                agreement_invoicing_display_options = 'RemainOnInvoicingScreen',
                company_activity_tab_format = 'SummaryList',
                default_email = 'Office',
                default_phone = 'Office',
                first_name = '',
                hire_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                identifier = '',
                invoice_screen_default_tab_format = 'ShowInvoicingTab',
                invoice_time_tab_format = 'SummaryList',
                invoicing_display_options = 'RemainOnInvoicingScreen',
                last_name = '',
                license_class = 'A',
        )
        """

    def testMyAccount(self):
        """Test MyAccount"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
