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

from connectwise_psa.models.company_company_type_association_company_type_association import CompanyCompanyTypeAssociationCompanyTypeAssociation

class TestCompanyCompanyTypeAssociationCompanyTypeAssociation(unittest.TestCase):
    """CompanyCompanyTypeAssociationCompanyTypeAssociation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompanyCompanyTypeAssociationCompanyTypeAssociation:
        """Test CompanyCompanyTypeAssociationCompanyTypeAssociation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompanyCompanyTypeAssociationCompanyTypeAssociation`
        """
        model = CompanyCompanyTypeAssociationCompanyTypeAssociation()
        if include_optional:
            return CompanyCompanyTypeAssociationCompanyTypeAssociation(
                info = {
                    'key' : ''
                    },
                company = connectwise_psa.models.company_reference.CompanyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    identifier = '', 
                    name = '', ),
                id = 56,
                type = connectwise_psa.models.company_type_reference.CompanyTypeReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', )
            )
        else:
            return CompanyCompanyTypeAssociationCompanyTypeAssociation(
        )
        """

    def testCompanyCompanyTypeAssociationCompanyTypeAssociation(self):
        """Test CompanyCompanyTypeAssociationCompanyTypeAssociation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()