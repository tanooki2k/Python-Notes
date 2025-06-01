from unittest import TestCase
from unittest.mock import patch
from page import PageRequester


# Unit tests for the PageRequester class.
class TestPageRequester(TestCase):

    # Sets up a PageRequester instance for testing with a specific URL.
    def setUp(self):
        self.page = PageRequester("https://www.google.com")

    # Tests if the get() method makes an HTTP GET request.
    def test_make_request(self):
        with patch("requests.get") as mock_get:
            self.page.get()
            mock_get.assert_called()

    # Tests if the get() method correctly returns the content from the HTTP response.
    def test_content_returned(self):
        fake_content = "Hello"

        # Simulates a mocked HTTP response with predefined content.
        class FakeResponse:
            def __init__(self):
                self.content = fake_content

        with patch("requests.get", return_value=FakeResponse()):
            result = self.page.get()
            self.assertEqual(result, fake_content)
