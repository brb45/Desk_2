import pytest

class Test:
    def test_a(self, sqs_event_payload):
        id = '10001'
        TEST_BUCKET_NAME = "bucket_2"
        payload = sqs_event_payload(id, TEST_BUCKET_NAME)

        # Send the payload to a function we want to test.
        # For example, a Lambda handler function
        # r = handler(event=payload, context=None)

        # Assert something here...

    def test_b(self):
        print("\nthis is test_b")


