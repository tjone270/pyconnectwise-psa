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

from connectwise_psa.models.forecast import Forecast

class TestForecast(unittest.TestCase):
    """Forecast unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Forecast:
        """Test Forecast
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Forecast`
        """
        model = Forecast()
        if include_optional:
            return Forecast(
                info = {
                    'key' : ''
                    },
                agreement_revenue = connectwise_psa.models.agreement_revenue_reference.AgreementRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                billing_terms = connectwise_psa.models.billing_terms_reference.BillingTermsReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
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
                expected_probability = 56,
                expense_revenue = connectwise_psa.models.expense_revenue_reference.ExpenseRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                forecast_items = [
                    connectwise_psa.models.forecast_item.ForecastItem(
                        _info = {
                            'key' : ''
                            }, 
                        bill_cycle = connectwise_psa.models.billing_cycle_reference.BillingCycleReference(
                            id = 56, 
                            name = '', ), 
                        catalog_item = connectwise_psa.models.iv_item_reference.IvItemReference(
                            id = 56, 
                            identifier = '', 
                            serialized_flag = True, ), 
                        cost = 1.337, 
                        cycle_basis = '', 
                        cycles = 56, 
                        forecast_description = '', 
                        forecast_type = 'Other1', 
                        id = 56, 
                        include_flag = True, 
                        link_flag = True, 
                        margin = 1.337, 
                        opportunity = connectwise_psa.models.opportunity_reference.OpportunityReference(
                            id = 56, 
                            name = '', ), 
                        percentage = 56, 
                        product_class = '', 
                        product_description = '', 
                        quantity = 1.337, 
                        quote_werks_doc_name = '', 
                        quote_werks_doc_no = '', 
                        quote_werks_quantity = 56, 
                        recurring_cost = 1.337, 
                        recurring_date_end = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        recurring_date_start = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        recurring_flag = True, 
                        recurring_revenue = 1.337, 
                        revenue = 1.337, 
                        sequence_number = 1.337, 
                        status = connectwise_psa.models.opportunity_status_reference.OpportunityStatusReference(
                            id = 56, 
                            name = '', ), 
                        sub_number = 56, 
                        taxable_flag = True, )
                    ],
                forecast_revenue_totals = connectwise_psa.models.forecast_revenue_reference.ForecastRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                forecast_total_with_taxes = 1.337,
                id = 56,
                inclusive_revenue_totals = connectwise_psa.models.inclusive_revenue_reference.InclusiveRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                lost_revenue = connectwise_psa.models.lost_revenue_reference.LostRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                open_revenue = connectwise_psa.models.open_revenue_reference.OpenRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                other_revenue1 = connectwise_psa.models.other1_revenue_reference.Other1RevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                other_revenue2 = connectwise_psa.models.other2_revenue_reference.Other2RevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                product_revenue = connectwise_psa.models.product_revenue_reference.ProductRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                recurring_total = 1.337,
                sales_tax_revenue = 1.337,
                service_revenue = connectwise_psa.models.service_revenue_reference.ServiceRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                tax_code = connectwise_psa.models.tax_code_reference.TaxCodeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                time_revenue = connectwise_psa.models.time_revenue_reference.TimeRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, ),
                won_revenue = connectwise_psa.models.won_revenue_reference.WonRevenueReference(
                    _info = {
                        'key' : ''
                        }, 
                    cost = 1.337, 
                    id = 56, 
                    margin = 1.337, 
                    percentage = 1.337, 
                    revenue = 1.337, )
            )
        else:
            return Forecast(
        )
        """

    def testForecast(self):
        """Test Forecast"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
