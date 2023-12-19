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

from connectwise_psa.models.survey_question_value import SurveyQuestionValue

class TestSurveyQuestionValue(unittest.TestCase):
    """SurveyQuestionValue unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SurveyQuestionValue:
        """Test SurveyQuestionValue
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SurveyQuestionValue`
        """
        model = SurveyQuestionValue()
        if include_optional:
            return SurveyQuestionValue(
                info = {
                    'key' : ''
                    },
                default_flag = True,
                id = 56,
                inactive_flag = True,
                point_value = 56,
                question = connectwise_psa.models.survey_question_reference.SurveyQuestionReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    question = '', ),
                survey = connectwise_psa.models.survey_reference.SurveyReference(
                    _info = {
                        'key' : ''
                        }, 
                    id = 56, 
                    name = '', ),
                value = ''
            )
        else:
            return SurveyQuestionValue(
                value = '',
        )
        """

    def testSurveyQuestionValue(self):
        """Test SurveyQuestionValue"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
