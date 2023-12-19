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

from connectwise_psa.models.unposted_invoice import UnpostedInvoice

class TestUnpostedInvoice(unittest.TestCase):
    """UnpostedInvoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnpostedInvoice:
        """Test UnpostedInvoice
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnpostedInvoice`
        """
        model = UnpostedInvoice()
        if include_optional:
            return UnpostedInvoice(
                info = {
                    'key' : ''
                    },
                account_number = '',
                avalara_tax_flag = True,
                bill_to_company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                bill_to_site = connectwise_psa.models.site_reference.SiteReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                billing_log_id = 56,
                billing_terms = connectwise_psa.models.billing_terms_reference.BillingTermsReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                city_tax_amount = 1.337,
                city_tax_flag = True,
                city_tax_xref = '',
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                composite_tax_amount = 1.337,
                composite_tax_flag = True,
                composite_tax_xref = '',
                country_tax_amount = 1.337,
                country_tax_flag = True,
                country_tax_xref = '',
                county_tax_amount = 1.337,
                county_tax_flag = True,
                county_tax_xref = '',
                created_by = '',
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
                date_closed = '',
                department_id = 56,
                description = '',
                due_date = '',
                due_days = '',
                id = 56,
                invoice_date = '',
                invoice_number = '',
                invoice_taxable_flag = True,
                invoice_type = 'Agreement',
                item_taxable_flag = True,
                level_six_tax_amount = 1.337,
                level_six_tax_flag = True,
                level_six_tax_xref = '',
                location_id = 56,
                sales_tax_amount = 1.337,
                ship_to_company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                ship_to_site = connectwise_psa.models.site_reference.SiteReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                state_tax_amount = 1.337,
                state_tax_flag = True,
                state_tax_xref = '',
                sub_total = 1.337,
                tax_code = connectwise_psa.models.tax_code_reference.TaxCodeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                total = 1.337
            )
        else:
            return UnpostedInvoice(
        )
        """

    def testUnpostedInvoice(self):
        """Test UnpostedInvoice"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()