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

from connectwise_psa.models.gl_export_customer import GLExportCustomer

class TestGLExportCustomer(unittest.TestCase):
    """GLExportCustomer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GLExportCustomer:
        """Test GLExportCustomer
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GLExportCustomer`
        """
        model = GLExportCustomer()
        if include_optional:
            return GLExportCustomer(
                account_number = '',
                billing_terms = connectwise_psa.models.billing_terms_reference.BillingTermsReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                billing_terms_xref = '',
                city_tax_agency_xref = '',
                city_tax_rate = 1.337,
                city_tax_xref = '',
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                company_type = connectwise_psa.models.company_type_reference.CompanyTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                composite_tax_agency_xref = '',
                composite_tax_rate = 1.337,
                composite_tax_xref = '',
                contact = connectwise_psa.models.contact_reference.ContactReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                country_tax_agency_xref = '',
                country_tax_rate = 1.337,
                country_tax_xref = '',
                county_tax_agency_xref = '',
                county_tax_rate = 1.337,
                county_tax_xref = '',
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
                due_days = 56,
                site = connectwise_psa.models.site_reference.SiteReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                state_tax_agency_xref = '',
                state_tax_rate = 1.337,
                state_tax_xref = '',
                tax_agency_xref = '',
                tax_code = connectwise_psa.models.tax_code_reference.TaxCodeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                tax_group_rate = 1.337,
                tax_levels = [
                    connectwise_psa.models.gl_export_customer_tax_level.GLExportCustomerTaxLevel(
                        agency_xref = '', 
                        tax_code_xref = '', 
                        tax_level = 56, 
                        tax_rate = 1.337, )
                    ],
                taxable = True
            )
        else:
            return GLExportCustomer(
        )
        """

    def testGLExportCustomer(self):
        """Test GLExportCustomer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
