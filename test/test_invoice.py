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

from connectwise_psa.models.invoice import Invoice

class TestInvoice(unittest.TestCase):
    """Invoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Invoice:
        """Test Invoice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Invoice`
        """
        model = Invoice()
        if include_optional:
            return Invoice(
                info = {
                    'key' : ''
                    },
                account_number = '',
                add_to_batch_email_list = True,
                adjusted_by = '',
                adjustment_reason = '',
                agreement = connectwise_psa.models.agreement_reference.AgreementReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    type = '', ),
                agreement_amount = 1.337,
                apply_to_id = 56,
                apply_to_type = 'All',
                attention = '',
                balance = 1.337,
                bill_to_company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                billing_setup_reference = connectwise_psa.models.billing_setup_reference.BillingSetupReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                billing_site = connectwise_psa.models.site_reference.SiteReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                billing_site_address_line1 = '',
                billing_site_address_line2 = '',
                billing_site_city = '',
                billing_site_country = '',
                billing_site_state = '',
                billing_site_zip = '',
                billing_terms = connectwise_psa.models.billing_terms_reference.BillingTermsReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                bottom_comment = '',
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                credits = 1.337,
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
                customer_po = '',
                var_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                department_id = 56,
                downpayment_applied = 1.337,
                downpayment_previously_taxed_flag = True,
                due_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                email_template_id = 56,
                expense_total = 1.337,
                id = 56,
                internal_notes = '',
                invoice_number = '',
                invoice_template = connectwise_psa.models.invoice_template_detail_reference.InvoiceTemplateDetailReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                location_id = 56,
                override_down_payment_amount_flag = True,
                payments = 1.337,
                phase = connectwise_psa.models.project_phase_reference.ProjectPhaseReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                previous_progress_applied = 1.337,
                product_total = 1.337,
                project = connectwise_psa.models.project_reference.ProjectReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                reference = '',
                remaining_downpayment = 1.337,
                restrict_downpayment_flag = True,
                sales_order = connectwise_psa.models.sales_order_reference.SalesOrderReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', ),
                sales_tax = 1.337,
                service_adjustment_amount = 1.337,
                service_total = 1.337,
                ship_to_attention = '',
                ship_to_company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                shipping_site = connectwise_psa.models.site_reference.SiteReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                shipping_site_address_line1 = '',
                shipping_site_address_line2 = '',
                shipping_site_city = '',
                shipping_site_country = '',
                shipping_site_state = '',
                shipping_site_zip = '',
                special_invoice_flag = True,
                status = connectwise_psa.models.billing_status_reference.BillingStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                subtotal = 1.337,
                tax_code = connectwise_psa.models.tax_code_reference.TaxCodeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                taxable_flag = True,
                template_setup_id = 56,
                territory_id = 56,
                ticket = connectwise_psa.models.ticket_reference.TicketReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    summary = '', ),
                top_comment = '',
                total = 1.337,
                type = 'Agreement'
            )
        else:
            return Invoice(
                type = 'Agreement',
        )
        """

    def testInvoice(self):
        """Test Invoice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
