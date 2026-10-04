import unittest
from unittest.mock import patch

from examples.ollama.health_check import check_ollama


class HealthCheckTests(unittest.TestCase):
    @patch('examples.ollama.health_check.urlopen')
    def test_successful_response(self, mock_urlopen):
        response = mock_urlopen.return_value.__enter__.return_value
        response.status = 200
        response.read.return_value = b'{"models": []}'
        self.assertTrue(check_ollama('http://localhost:11434'))

    @patch('examples.ollama.health_check.urlopen', side_effect=OSError)
    def test_unreachable_server(self, mock_urlopen):
        self.assertFalse(check_ollama('http://localhost:11434'))


if __name__ == "__main__":
    unittest.main()