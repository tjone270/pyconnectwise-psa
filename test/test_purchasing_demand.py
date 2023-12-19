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

from connectwise_psa.models.purchasing_demand import PurchasingDemand

class TestPurchasingDemand(unittest.TestCase):
    """PurchasingDemand unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PurchasingDemand:
        """Test PurchasingDemand
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PurchasingDemand`
        """
        model = PurchasingDemand()
        if include_optional:
            return PurchasingDemand(
                products = [
                    connectwise_psa.models.product_demand.ProductDemand(
                        cost = 1.337, 
                        product_rec_id = 56, 
                        quantity = 56, )
                    ],
                purchase_order = connectwise_psa.models.purchase_order.PurchaseOrder(
                    _info = {
                        'key' : ''
                        }, 
                    business_unit_id = 56, 
                    cancel_reason = '', 
                    closed_by = '', 
                    closed_flag = True, 
                    currency = connectwise_psa.models.currency_reference.CurrencyReference(
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
                    customer_city = '', 
                    customer_company = connectwise_psa.models.company_reference.CompanyReference(
                        id = 56, 
                        identifier = '', 
                        name = '', ), 
                    customer_contact = connectwise_psa.models.contact_reference.ContactReference(
                        id = 56, 
                        name = '', ), 
                    customer_country = connectwise_psa.models.country_reference.CountryReference(
                        id = 56, 
                        identifier = '', 
                        name = '', ), 
                    customer_extension = '', 
                    customer_name = '', 
                    customer_phone = '', 
                    customer_site = connectwise_psa.models.site_reference.SiteReference(
                        id = 56, 
                        name = '', ), 
                    customer_site_name = '', 
                    customer_state = '', 
                    customer_street_line1 = '', 
                    customer_street_line2 = '', 
                    customer_zip = '', 
                    date_closed = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    drop_ship_customer_flag = True, 
                    entered_by = '', 
                    freight_cost = 1.337, 
                    freight_packing_slip = '', 
                    freight_tax_total = 1.337, 
                    id = 56, 
                    internal_notes = '', 
                    location_id = 56, 
                    po_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    po_number = '', 
                    sales_tax = 1.337, 
                    shipment_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    shipment_method = connectwise_psa.models.shipment_method_reference.ShipmentMethodReference(
                        id = 56, 
                        name = '', ), 
                    shipping_instructions = '', 
                    status = connectwise_psa.models.purchase_order_status_reference.PurchaseOrderStatusReference(
                        id = 56, 
                        name = '', ), 
                    sub_total = 1.337, 
                    tax_code = connectwise_psa.models.tax_code_reference.TaxCodeReference(
                        id = 56, 
                        name = '', ), 
                    tax_freight_flag = True, 
                    tax_po_flag = True, 
                    terms = connectwise_psa.models.billing_terms_reference.BillingTermsReference(
                        id = 56, 
                        name = '', ), 
                    total = 1.337, 
                    tracking_number = '', 
                    update_shipment_info = True, 
                    update_vendor_order_number = True, 
                    vendor_company = connectwise_psa.models.company_reference.CompanyReference(
                        id = 56, 
                        identifier = '', 
                        name = '', ), 
                    vendor_contact = connectwise_psa.models.contact_reference.ContactReference(
                        id = 56, 
                        name = '', ), 
                    vendor_invoice_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    vendor_invoice_number = '', 
                    vendor_order_number = '', 
                    vendor_site = connectwise_psa.models.site_reference.SiteReference(
                        id = 56, 
                        name = '', ), 
                    warehouse = connectwise_psa.models.warehouse_reference.WarehouseReference(
                        id = 56, 
                        locked_flag = True, 
                        name = '', ), 
                    warehouse_contact = , ),
                vendor = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                warehouse = connectwise_psa.models.warehouse_reference.WarehouseReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    locked_flag = True, 
                    name = '', )
            )
        else:
            return PurchasingDemand(
        )
        """

    def testPurchasingDemand(self):
        """Test PurchasingDemand"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
