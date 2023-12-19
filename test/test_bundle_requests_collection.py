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

from connectwise_psa.models.bundle_requests_collection import BundleRequestsCollection

class TestBundleRequestsCollection(unittest.TestCase):
    """BundleRequestsCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BundleRequestsCollection:
        """Test BundleRequestsCollection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BundleRequestsCollection`
        """
        model = BundleRequestsCollection()
        if include_optional:
            return BundleRequestsCollection(
                requests = [
                    connectwise_psa.models.bundle_request.BundleRequest(
                        api_request = connectwise_psa.models.api_request.ApiRequest(
                            entity = connectwise_psa.models.i_rest_identified_item.IRestIdentifiedItem(
                                id = 56, ), 
                            external_id = '', 
                            fields = '', 
                            filters = connectwise_psa.models.filter_values.FilterValues(
                                childconditions = '', 
                                conditions = '', 
                                customfieldconditions = '', 
                                order_by = '', ), 
                            format = '', 
                            grand_parent_id = 56, 
                            id = 56, 
                            member_context = '', 
                            misc_properties = {
                                'key' : None
                                }, 
                            page = connectwise_psa.models.page_values.PageValues(
                                page_id = 56, 
                                page_size = 56, ), 
                            parent_id = 56, 
                            update_only_ces_properties = True, ), 
                        resource_type = '', 
                        sequence_number = 56, 
                        version = '', )
                    ]
            )
        else:
            return BundleRequestsCollection(
                requests = [
                    connectwise_psa.models.bundle_request.BundleRequest(
                        api_request = connectwise_psa.models.api_request.ApiRequest(
                            entity = connectwise_psa.models.i_rest_identified_item.IRestIdentifiedItem(
                                id = 56, ), 
                            external_id = '', 
                            fields = '', 
                            filters = connectwise_psa.models.filter_values.FilterValues(
                                childconditions = '', 
                                conditions = '', 
                                customfieldconditions = '', 
                                order_by = '', ), 
                            format = '', 
                            grand_parent_id = 56, 
                            id = 56, 
                            member_context = '', 
                            misc_properties = {
                                'key' : None
                                }, 
                            page = connectwise_psa.models.page_values.PageValues(
                                page_id = 56, 
                                page_size = 56, ), 
                            parent_id = 56, 
                            update_only_ces_properties = True, ), 
                        resource_type = '', 
                        sequence_number = 56, 
                        version = '', )
                    ],
        )
        """

    def testBundleRequestsCollection(self):
        """Test BundleRequestsCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
