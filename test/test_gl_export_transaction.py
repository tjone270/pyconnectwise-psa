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

from connectwise_psa.models.gl_export_transaction import GLExportTransaction

class TestGLExportTransaction(unittest.TestCase):
    """GLExportTransaction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GLExportTransaction:
        """Test GLExportTransaction
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GLExportTransaction`
        """
        model = GLExportTransaction()
        if include_optional:
            return GLExportTransaction(
                account_number = '',
                agreement_pre_payment_flag = True,
                attention = '',
                billing_terms = connectwise_psa.models.billing_terms_reference.BillingTermsReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                billing_terms_xref = '',
                billing_type = '',
                city_tax = 1.337,
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                company_account_number = '',
                company_type = connectwise_psa.models.company_type_reference.CompanyTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                county_tax = 1.337,
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
                description = '',
                detail = [
                    connectwise_psa.models.gl_export_transaction_detail.GLExportTransactionDetail(
                        account_number = '', 
                        cogs_xref = '', 
                        cost = 1.337, 
                        cost_account_number = '', 
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
                        description = '', 
                        document_date = '', 
                        document_type = '', 
                        drop_shipped_flag = True, 
                        gl_class = '', 
                        gl_item_id = '', 
                        gl_type_id = '', 
                        id = 56, 
                        inventory_account_number = '', 
                        inventory_xref = '', 
                        invoice_summary_option = '', 
                        item = connectwise_psa.models.iv_item_reference.IvItemReference(
                            id = 56, 
                            identifier = '', 
                            serialized_flag = True, ), 
                        item_cost = 1.337, 
                        item_description = '', 
                        item_price = 1.337, 
                        item_taxable_flag = True, 
                        item_type_xref = '', 
                        location_xref = '', 
                        memo = '', 
                        price_level_xref = '', 
                        product = connectwise_psa.models.product_reference.ProductReference(
                            description = '', 
                            id = 56, ), 
                        product_account_number = '', 
                        quantity = 1.337, 
                        sales_code = '', 
                        sales_description = '', 
                        serial_numbers = '', 
                        serialized_flag = True, 
                        shipment_method = connectwise_psa.models.shipment_method_reference.ShipmentMethodReference(
                            id = 56, 
                            name = '', ), 
                        sub_category = connectwise_psa.models.product_sub_category_reference.ProductSubCategoryReference(
                            id = 56, 
                            name = '', ), 
                        tax_agency_xref = '', 
                        tax_code = connectwise_psa.models.tax_code_reference.TaxCodeReference(
                            id = 56, 
                            name = '', ), 
                        tax_code_xref = '', 
                        tax_levels = [
                            connectwise_psa.models.gl_export_transaction_detail_tax_level.GLExportTransactionDetailTaxLevel(
                                tax_level = 56, 
                                taxable_flag = True, )
                            ], 
                        tax_note = '', 
                        tax_rate = 1.337, 
                        tax_rate_percent = 1.337, 
                        taxable2_flag = True, 
                        taxable3_flag = True, 
                        taxable4_flag = True, 
                        taxable5_flag = True, 
                        taxable_flag = True, 
                        time_entry = connectwise_psa.models.time_entry_reference.TimeEntryReference(
                            id = 56, ), 
                        total = 1.337, 
                        unit_of_measure = connectwise_psa.models.unit_of_measure_reference.UnitOfMeasureReference(
                            id = 56, 
                            name = '', ), 
                        uom_schedule_xref = '', 
                        warehouse_bin = connectwise_psa.models.warehouse_bin_reference.WarehouseBinReference(
                            id = 56, 
                            name = '', ), 
                        warehouse_site = connectwise_psa.models.site_reference.SiteReference(
                            id = 56, 
                            name = '', ), )
                    ],
                document_date = '',
                document_number = '',
                document_type = '',
                due_date = '',
                due_days = 56,
                email_delivery_flag = True,
                gl_class = '',
                gl_entry_ids = '',
                gl_type_id = '',
                id = 56,
                memo = '',
                piggy_back_flag = True,
                print_delivery_flag = True,
                project = connectwise_psa.models.project_reference.ProjectReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                purchase_order = connectwise_psa.models.purchase_order_reference.PurchaseOrderReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                sales_rep_id = '',
                sales_rep_name = '',
                sales_tax = 1.337,
                sales_territory = '',
                send_avalara_tax_flag = True,
                ship_contact = '',
                ship_site = connectwise_psa.models.site_reference.SiteReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                ship_to_company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                ship_to_company_account_number = '',
                ship_to_company_type = connectwise_psa.models.company_type_reference.CompanyTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                ship_to_tax_id = '',
                site = connectwise_psa.models.site_reference.SiteReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                state_tax = 1.337,
                state_tax_xref = '',
                tax_account_number = '',
                tax_agency_xref = '',
                tax_code = connectwise_psa.models.tax_code_reference.TaxCodeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                tax_dp_applied_flag = True,
                tax_group_rate = 1.337,
                tax_id = '',
                tax_levels = [
                    connectwise_psa.models.gl_export_transaction_tax_level.GLExportTransactionTaxLevel(
                        tax_amount = 1.337, 
                        tax_code_xref = '', 
                        tax_level = 56, 
                        taxable_amount = 1.337, )
                    ],
                taxable = True,
                taxable_amount1 = 1.337,
                taxable_amount2 = 1.337,
                taxable_amount3 = 1.337,
                taxable_amount4 = 1.337,
                taxable_amount5 = 1.337,
                taxable_total = 1.337,
                total = 1.337,
                use_avalara_flag = True
            )
        else:
            return GLExportTransaction(
        )
        """

    def testGLExportTransaction(self):
        """Test GLExportTransaction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
