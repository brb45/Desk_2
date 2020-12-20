from learning_german import send_message

# No mocking
# Yay! Our first test just ran. But it has a few problems:
#
# Every time you run it, it will send real SMSs - we don’t want this
# Every time it sends a real SMS, Twilio charges you money
# You need real phone numbers to test your code
# It is slow
def test_send_a_common_word():
    message = "Hi there"
    to = "<your-personal-number>"
    from_ = "<your-twilio-number>"
    assert send_message(to, from_, message) is not None


# Mocking parts of your code
from learning_german import send_message
from unittest import mock


@mock.patch('learning_german.client.messages.create')
def test_send_a_common_word(create_message_mock):
    message = "Hi there"
    expected_sid = 'SM87105da94bff44b999e4e6eb90d8eb6a'
    create_message_mock.return_value.sid = expected_sid

    to = "<your-personal-number>"
    from_ = "<your-twilio-number>"
    sid = send_message(to, from_, message)

    assert create_message_mock.called is True
    assert sid == expected_sid