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

from connectwise_psa.models.bundle_results_collection import BundleResultsCollection

class TestBundleResultsCollection(unittest.TestCase):
    """BundleResultsCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BundleResultsCollection:
        """Test BundleResultsCollection
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BundleResultsCollection`
        """
        model = BundleResultsCollection()
        if include_optional:
            return BundleResultsCollection(
                info = {
                    'key' : ''
                    },
                results = [
                    connectwise_psa.models.bundle_result.BundleResult(
                        count = 56, 
                        entities = [
                            connectwise_psa.models.i_rest_identified_item.IRestIdentifiedItem(
                                id = 56, )
                            ], 
                        error = connectwise_psa.models.error_response_message.ErrorResponseMessage(
                            code = '', 
                            errors = [
                                connectwise_psa.models.validation_error.ValidationError(
                                    code = '', 
                                    details = '', 
                                    field = '', 
                                    message = '', 
                                    resource = '', )
                                ], 
                            message = '', ), 
                        resource_type = '', 
                        sequence_number = 56, 
                        status_code = 56, 
                        success = True, 
                        version = '', )
                    ]
            )
        else:
            return BundleResultsCollection(
        )
        """

    def testBundleResultsCollection(self):
        """Test BundleResultsCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
