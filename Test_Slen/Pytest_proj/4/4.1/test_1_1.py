import pytest

class Test:
    def test_a(self, sqs_event_payload):
        id = '10001'
        TEST_BUCKET_NAME = "bucket_2"
        payload = sqs_event_payload(id, TEST_BUCKET_NAME)

        assert payload == (id, TEST_BUCKET_NAME)

        # Send the payload to a function we want to test.
        # For example, a Lambda handler function
        # r = handler(event=payload, context=None)

        # Assert something here...

    def test_b(self):
        print("\nthis is test_b")

# @pytest.fixture
# def sqs_event_payload1():
#     def _payload(id, BUCKET_NAME):
#         res = (id, BUCKET_NAME)
#         return res
#
#     return _payload
#
#
# @pytest.fixture(autouse=True)
# def just_print2():
#     print("\nauto-fixture is run")
#     yield
#     print("\nAll test is done")
