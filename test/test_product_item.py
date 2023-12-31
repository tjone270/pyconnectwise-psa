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

from connectwise_psa.models.product_item import ProductItem

class TestProductItem(unittest.TestCase):
    """ProductItem unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductItem:
        """Test ProductItem
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductItem`
        """
        model = ProductItem()
        if include_optional:
            return ProductItem(
                info = {
                    'key' : ''
                    },
                add_components_flag = True,
                agreement = connectwise_psa.models.agreement_reference.AgreementReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', 
                    type = '', ),
                agreement_amount = 1.337,
                billable_option = 'Billable',
                business_unit = connectwise_psa.models.billing_unit_reference.BillingUnitReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                business_unit_id = 56,
                bypass_forecast_update = True,
                calculated_cost = 1.337,
                calculated_cost_flag = True,
                calculated_price = 1.337,
                calculated_price_flag = True,
                cancelled_by = 56,
                cancelled_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                cancelled_flag = True,
                cancelled_reason = '',
                catalog_item = connectwise_psa.models.catalog_item_reference.CatalogItemReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                cost = 1.337,
                custom_fields = [
                    connectwise_psa.models.custom_field_value.CustomFieldValue(
                        caption = '', 
                        entry_method = 'Date', 
                        id = 56, 
                        number_of_decimals = 56, 
                        type = 'TextArea', 
                        value = connectwise_psa.models.value.value(), )
                    ],
                customer_description = '',
                description = '',
                discount = 1.337,
                dropship_flag = True,
                entity_type = connectwise_psa.models.entity_type_reference.EntityTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                forecast_detail_id = 56,
                forecast_status = connectwise_psa.models.opportunity_status_reference.OpportunityStatusReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                id = 56,
                ignore_pricing_schedules_flag = True,
                integration_x_ref = '',
                internal_notes = '',
                invoice = connectwise_psa.models.invoice_reference.InvoiceReference(
                    _info = {
                        'key' : ''
                        }, 
                    apply_to_type = '', 
                    billing_type = '', 
                    id = 56, 
                    identifier = '', ),
                invoice_grouping = connectwise_psa.models.invoice_grouping_reference.InvoiceGroupingReference(
                    _info = {
                        'key' : ''
                        }, 
                    description = '', 
                    group_parent_child_additions_flag = True, 
                    id = 56, 
                    name = '', 
                    show_price_flag = True, 
                    show_sub_items_flag = True, ),
                list_price = 1.337,
                location = connectwise_psa.models.system_location_reference.SystemLocationReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                location_id = 56,
                minimum_stock_flag = True,
                need_to_order_quantity = 56,
                need_to_purchase_flag = True,
                opportunity = connectwise_psa.models.opportunity_reference.OpportunityReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                phase = connectwise_psa.models.project_phase_reference.ProjectPhaseReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                phase_product_flag = True,
                po_approved_flag = True,
                price = 1.337,
                price_method = 'FlatRateForRange',
                product_class = 'Agreement',
                product_supplied_flag = True,
                project = connectwise_psa.models.project_reference.ProjectReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                purchase_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                quantity = 1.337,
                quantity_cancelled = 1.337,
                recurring = connectwise_psa.models.product_recurring.ProductRecurring(
                    bill_cycle_id = 56, 
                    cycle_type = 'ContractYear', 
                    cycles = 56, 
                    end_date = '', 
                    recurring_cost = 1.337, 
                    recurring_revenue = 1.337, 
                    start_date = '', ),
                sales_order = connectwise_psa.models.sales_order_reference.SalesOrderReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', ),
                sequence_number = 1.337,
                serial_number_ids = [
                    56
                    ],
                serial_numbers = [
                    ''
                    ],
                ship_set = '',
                sla = connectwise_psa.models.sla_reference.SLAReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                special_order_flag = True,
                sub_contractor_amount_limit = 1.337,
                sub_contractor_ship_to_id = 56,
                taxable_flag = True,
                ticket = connectwise_psa.models.ticket_reference.TicketReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    summary = '', ),
                vendor = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                vendor_sku = '',
                warehouse = '',
                warehouse_bin = '',
                warehouse_bin_id = 56,
                warehouse_bin_id_object = connectwise_psa.models.warehouse_bin_reference.WarehouseBinReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                warehouse_id = 56,
                warehouse_id_object = connectwise_psa.models.warehouse_reference.WarehouseReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    locked_flag = True, 
                    name = '', )
            )
        else:
            return ProductItem(
                billable_option = 'Billable',
        )
        """

    def testProductItem(self):
        """Test ProductItem"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
