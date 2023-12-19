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

from connectwise_psa.models.service_template import ServiceTemplate

class TestServiceTemplate(unittest.TestCase):
    """ServiceTemplate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceTemplate:
        """Test ServiceTemplate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceTemplate`
        """
        model = ServiceTemplate()
        if include_optional:
            return ServiceTemplate(
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
                assigned_by = connectwise_psa.models.member_reference.MemberReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                assigned_notify_flag = True,
                attach_schedule_to_new_service_flag = True,
                bill_complete_flag = True,
                bill_service_separately_flag = True,
                bill_unapproved_time_and_expenses_flag = True,
                billing_amount = 1.337,
                billing_method = 'ActualRates',
                board = connectwise_psa.models.board_reference.BoardReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
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
                department = connectwise_psa.models.system_department_reference.SystemDepartmentReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                email_cc = '',
                email_cc_flag = True,
                email_contact_flag = True,
                email_resource_flag = True,
                expense_billable_flag = True,
                expense_invoice_flag = True,
                hours_budget = 1.337,
                id = 56,
                impact = 'Low',
                internal_analysis = '',
                item = connectwise_psa.models.service_item_reference.ServiceItemReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                name = '',
                override_flag = True,
                priority = connectwise_psa.models.priority_reference.PriorityReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    level = '', 
                    name = '', 
                    sort = 56, ),
                problem = '',
                product_invoice_flag = True,
                purchase_order_number = '',
                reference = '',
                restrict_downpayment_flag = True,
                schedule_days_before = 56,
                service_days_before = 56,
                service_location = connectwise_psa.models.service_location_reference.ServiceLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                severity = 'Low',
                site = connectwise_psa.models.site_reference.SiteReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                source = connectwise_psa.models.service_source_reference.ServiceSourceReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                status = connectwise_psa.models.service_status_reference.ServiceStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    sort = 56, ),
                subtype = connectwise_psa.models.service_sub_type_reference.ServiceSubTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                summary = '',
                team = connectwise_psa.models.service_team_reference.ServiceTeamReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                template_flag = True,
                time_billable_flag = True,
                time_invoice_flag = True,
                type = connectwise_psa.models.service_type_reference.ServiceTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return ServiceTemplate(
        )
        """

    def testServiceTemplate(self):
        """Test ServiceTemplate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()