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

from connectwise_psa.models.file_upload_setting import FileUploadSetting

class TestFileUploadSetting(unittest.TestCase):
    """FileUploadSetting unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> FileUploadSetting:
        """Test FileUploadSetting
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `FileUploadSetting`
        """
        model = FileUploadSetting()
        if include_optional:
            return FileUploadSetting(
                info = {
                    'key' : ''
                    },
                global_file_size_limit = 56,
                id = 56,
                restrict_file_types_flag = True
            )
        else:
            return FileUploadSetting(
                restrict_file_types_flag = True,
        )
        """

    def testFileUploadSetting(self):
        """Test FileUploadSetting"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()