#!/usr/bin/env python3
"""
Unit tests for client.py
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        mock_get_json.return_value = org_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, org_payload)
        mock_get_json.assert_called_once_with((
            f"https://api.github.com/orgs/{org_name}")
            )

        @patch('client.GithubOrgClient.org', new_callable=Mock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns the correct URL"""
        mock_org.return_value = org_payload
        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, org_payload["repos_url"])

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=Mock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that public_repos returns the correct list of repos"""
        mock_get_json.return_value = repos_payload
        mock_public_repos_url.return_value = "http://fake.url"
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), expected_repos)
        mock_get_json.assert_called_once_with("http://fake.url")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that has_license returns the correct result"""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', (
    'apache2_repos'), [
    )
    (org_payload, repos_payload, expected_repos, apache2_repos)
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test cases for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class method"""
        cls.get_patcher = patch('client.requests.get')
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.get_side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class method"""
        cls.get_patcher.stop()

    @staticmethod
    def get_side_effect(url):
        """Side effect method for requests.get"""
        if url == "https://api.github.com/orgs/google":
            return Mock(json=lambda: org_payload)
        if url == "http://fake.url":
            return Mock(json=lambda: repos_payload)
        return Mock()

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with license argument"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), (
            apache2_repos)
            )


if __name__ == '__main__':
    unittest.main()
