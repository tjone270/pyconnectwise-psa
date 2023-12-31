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

from connectwise_psa.models.link_clicked import LinkClicked

class TestLinkClicked(unittest.TestCase):
    """LinkClicked unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LinkClicked:
        """Test LinkClicked
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LinkClicked`
        """
        model = LinkClicked()
        if include_optional:
            return LinkClicked(
                campaign_id = 56,
                contact_id = 56,
                date_clicked = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = 56,
                query_string = '',
                url = ''
            )
        else:
            return LinkClicked(
                contact_id = 56,
                url = '',
        )
        """

    def testLinkClicked(self):
        """Test LinkClicked"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
