import sys
import types
import unittest
from unittest.mock import MagicMock, patch

from src import chatbot


class TestChatbot(unittest.TestCase):
    def test_handle_question(self):
        fake_records = [{"name": "Alice"}, {"name": "Bob"}]
        fake_response = {"choices": [{"message": {"content": "Hi"}}]}

        fake_openai = types.SimpleNamespace(
            ChatCompletion=types.SimpleNamespace(create=MagicMock(return_value=fake_response)),
            api_key=None,
        )

        with patch("src.chatbot.fetch_records", return_value=fake_records):
            sys.modules["openai"] = fake_openai
            answer = chatbot.handle_question("Who is here?", "SELECT * FROM people")
            self.assertEqual(answer, "Hi")
            del sys.modules["openai"]


if __name__ == "__main__":
    unittest.main()
