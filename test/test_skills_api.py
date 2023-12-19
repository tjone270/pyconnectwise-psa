# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from connectwise_psa.api.skills_api import SkillsApi


class TestSkillsApi(unittest.TestCase):
    """SkillsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SkillsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_system_skills_by_id(self) -> None:
        """Test case for delete_system_skills_by_id

        Delete Skill
        """
        pass

    def test_get_system_skills(self) -> None:
        """Test case for get_system_skills

        Get List of Skill
        """
        pass

    def test_get_system_skills_by_id(self) -> None:
        """Test case for get_system_skills_by_id

        Get Skill
        """
        pass

    def test_get_system_skills_count(self) -> None:
        """Test case for get_system_skills_count

        Get Count of Skill
        """
        pass

    def test_patch_system_skills_by_id(self) -> None:
        """Test case for patch_system_skills_by_id

        Patch Skill
        """
        pass

    def test_post_system_skills(self) -> None:
        """Test case for post_system_skills

        Post Skill
        """
        pass

    def test_put_system_skills_by_id(self) -> None:
        """Test case for put_system_skills_by_id

        Put Skill
        """
        pass


if __name__ == '__main__':
    unittest.main()
