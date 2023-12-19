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

from connectwise_psa.models.project_ticket import ProjectTicket

class TestProjectTicket(unittest.TestCase):
    """ProjectTicket unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProjectTicket:
        """Test ProjectTicket
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProjectTicket`
        """
        model = ProjectTicket()
        if include_optional:
            return ProjectTicket(
                info = {
                    'key' : ''
                    },
                actual_hours = 1.337,
                address_line1 = '',
                address_line2 = '',
                agreement = connectwise_psa.models.agreement_reference.AgreementReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    type = '', ),
                allow_all_clients_portal_view = True,
                approved = True,
                automatic_email_cc = '',
                automatic_email_cc_flag = True,
                automatic_email_contact_flag = True,
                automatic_email_resource_flag = True,
                bill_expenses = 'Billable',
                bill_products = 'Billable',
                bill_time = 'Billable',
                board = connectwise_psa.models.board_reference.BoardReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                budget_hours = 1.337,
                city = '',
                closed_by = '',
                closed_date = '',
                closed_flag = True,
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                contact = connectwise_psa.models.contact_reference.ContactReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                contact_email_address = '',
                contact_email_lookup = '',
                contact_name = '',
                contact_phone_extension = '',
                contact_phone_number = '',
                country = connectwise_psa.models.country_reference.CountryReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                currency = connectwise_psa.models.currency_reference.CurrencyReference(
                    _info = {
                        'key' : ''
                        }, 
                    currency_code = '', 
                    currency_identifier = '', 
                    decimal_separator = '', 
                    display_id_flag = True, 
                    display_symbol_flag = True, 
                    id = 56, 
                    name = '', 
                    negative_parentheses_flag = True, 
                    number_of_decimals = 56, 
                    right_align = True, 
                    symbol = '', 
                    thousands_separator = '', ),
                custom_fields = [
                    connectwise_psa.models.custom_field_value.CustomFieldValue(
                        caption = '', 
                        entry_method = 'Date', 
                        id = 56, 
                        number_of_decimals = 56, 
                        type = 'TextArea', 
                        value = connectwise_psa.models.value.value(), )
                    ],
                customer_updated_flag = True,
                department = connectwise_psa.models.system_department_reference.SystemDepartmentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                duration = 56,
                estimated_start_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 56,
                initial_description = '',
                initial_internal_analysis = '',
                initial_resolution = '',
                is_issue_flag = True,
                item = connectwise_psa.models.service_item_reference.ServiceItemReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                knowledge_base_category_id = 56,
                knowledge_base_link_id = 56,
                knowledge_base_link_type = 'Activity',
                knowledge_base_sub_category_id = 56,
                lag_days = 56,
                lag_nonworking_days_flag = True,
                location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                mobile_guid = '',
                opportunity = connectwise_psa.models.opportunity_reference.OpportunityReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                owner = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                phase = connectwise_psa.models.project_phase_reference.ProjectPhaseReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                predecessor_closed_flag = True,
                predecessor_id = 56,
                predecessor_type = 'Ticket',
                priority = connectwise_psa.models.priority_reference.PriorityReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    level = '', 
                    name = '', 
                    sort = 56, ),
                process_notifications = True,
                project = connectwise_psa.models.project_reference.ProjectReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                required_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                resources = '',
                service_location = connectwise_psa.models.service_location_reference.ServiceLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                site = connectwise_psa.models.site_reference.SiteReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                site_name = '',
                skip_callback = True,
                source = connectwise_psa.models.service_source_reference.ServiceSourceReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                state_identifier = '',
                status = connectwise_psa.models.service_status_reference.ServiceStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    sort = 56, ),
                sub_billing_amount = 1.337,
                sub_billing_method = 'ActualRates',
                sub_date_accepted = '',
                sub_type = connectwise_psa.models.service_sub_type_reference.ServiceSubTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                summary = '',
                tasks = [
                    connectwise_psa.models.ticket_task.TicketTask(
                        _info = {
                            'key' : ''
                            }, 
                        child_schedule_action = 'Transfer', 
                        child_ticket_id = 56, 
                        closed_flag = True, 
                        code = connectwise_psa.models.service_code_reference.ServiceCodeReference(
                            id = 56, 
                            name = '', ), 
                        id = 56, 
                        notes = '', 
                        priority = 56, 
                        resolution = '', 
                        schedule = connectwise_psa.models.schedule_entry_reference.ScheduleEntryReference(
                            description = '', 
                            id = 56, ), 
                        summary = '', 
                        ticket_id = 56, )
                    ],
                type = connectwise_psa.models.service_type_reference.ServiceTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                wbs_code = '',
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
                    name = '', ),
                zip = ''
            )
        else:
            return ProjectTicket(
                summary = '',
        )
        """

    def testProjectTicket(self):
        """Test ProjectTicket"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()