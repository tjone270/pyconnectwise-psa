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

from connectwise_psa.models.agreement_application_parameters import AgreementApplicationParameters

class TestAgreementApplicationParameters(unittest.TestCase):
    """AgreementApplicationParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AgreementApplicationParameters:
        """Test AgreementApplicationParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AgreementApplicationParameters`
        """
        model = AgreementApplicationParameters()
        if include_optional:
            return AgreementApplicationParameters(
                agr_billing_cycle = connectwise_psa.models.agreement_application_billing_cycle.AgreementApplicationBillingCycle(
                    id = 56, 
                    name = '', 
                    tag = '', ),
                agreement_expires_flag = True,
                allow_overruns_flag = True,
                application_limit = connectwise_psa.models.agreement_application_limit.AgreementApplicationLimit(
                    id = 56, 
                    name = '', 
                    tag = '', ),
                application_limit_amount = 1.337,
                application_unit = connectwise_psa.models.agreement_application_unit.AgreementApplicationUnit(
                    id = 56, 
                    name = '', 
                    tag = '', ),
                available_per = connectwise_psa.models.agreement_application_aviable_per.AgreementApplicationAviablePer(
                    id = 56, 
                    name = '', 
                    tag = '', ),
                carry_over_days = 56,
                carryover_unused_flag = True,
                charge_adjustments_flag = True,
                covers_expenses_flag = True,
                covers_products_flag = True,
                covers_tax_flag = True,
                covers_time_flag = True,
                overrun_limit = 56,
                prepay_flag = True,
                user_defined_field_values = [
                    connectwise_psa.models.user_defined_field_value_model.UserDefinedFieldValueModel(
                        filtered = True, 
                        row_num = 56, 
                        skip_location_and_billing_unit = True, 
                        user_defined_field_rec_id = 56, 
                        value = '', )
                    ]
            )
        else:
            return AgreementApplicationParameters(
        )
        """

    def testAgreementApplicationParameters(self):
        """Test AgreementApplicationParameters"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
