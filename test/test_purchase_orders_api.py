# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.purchase_orders_api import PurchaseOrdersApi


class TestPurchaseOrdersApi(unittest.TestCase):
    """PurchaseOrdersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PurchaseOrdersApi()

    def tearDown(self) -> None:
        pass

    def test_delete_procurement_purchaseorders_by_id(self) -> None:
        """Test case for delete_procurement_purchaseorders_by_id

        Delete PurchaseOrder
        """
        pass

    def test_get_procurement_purchaseorders(self) -> None:
        """Test case for get_procurement_purchaseorders

        Get List of PurchaseOrder
        """
        pass

    def test_get_procurement_purchaseorders_by_id(self) -> None:
        """Test case for get_procurement_purchaseorders_by_id

        Get PurchaseOrder
        """
        pass

    def test_get_procurement_purchaseorders_count(self) -> None:
        """Test case for get_procurement_purchaseorders_count

        Get Count of PurchaseOrder
        """
        pass

    def test_patch_procurement_purchaseorders_by_id(self) -> None:
        """Test case for patch_procurement_purchaseorders_by_id

        Patch PurchaseOrder
        """
        pass

    def test_post_procurement_purchaseorders(self) -> None:
        """Test case for post_procurement_purchaseorders

        Post PurchaseOrder
        """
        pass

    def test_post_procurement_purchaseorders_by_id_rebatch(self) -> None:
        """Test case for post_procurement_purchaseorders_by_id_rebatch

        Post RebatchPurchaseOrder
        """
        pass

    def test_post_procurement_purchaseorders_by_id_unbatch(self) -> None:
        """Test case for post_procurement_purchaseorders_by_id_unbatch

        Post UnbatchPurchaseOrder
        """
        pass

    def test_put_procurement_purchaseorders_by_id(self) -> None:
        """Test case for put_procurement_purchaseorders_by_id

        Put PurchaseOrder
        """
        pass


if __name__ == '__main__':
    unittest.main()
