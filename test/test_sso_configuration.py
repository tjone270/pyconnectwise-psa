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

from connectwise_psa.models.sso_configuration import SsoConfiguration

class TestSsoConfiguration(unittest.TestCase):
    """SsoConfiguration unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SsoConfiguration:
        """Test SsoConfiguration
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SsoConfiguration`
        """
        model = SsoConfiguration()
        if include_optional:
            return SsoConfiguration(
                info = {
                    'key' : ''
                    },
                all_members_submitted = True,
                client_id = '',
                id = 56,
                inactive_flag = True,
                is_sso_on_by_default = True,
                location_ids = [
                    56
                    ],
                name = '',
                saml_certificate_issued_to = '',
                saml_certificate_name = '',
                saml_certificate_thumbprint = '',
                saml_certificate_valid_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                saml_certificate_valid_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                saml_entity_id = '',
                saml_idp_certificate = '',
                saml_sign_in_url = '',
                sso_type = 'CWSSO',
                sts_base_url = '',
                sts_user_admin_url = '',
                submitted_member_count = 56,
                token = ''
            )
        else:
            return SsoConfiguration(
                location_ids = [
                    56
                    ],
                name = '',
                sso_type = 'CWSSO',
        )
        """

    def testSsoConfiguration(self):
        """Test SsoConfiguration"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
