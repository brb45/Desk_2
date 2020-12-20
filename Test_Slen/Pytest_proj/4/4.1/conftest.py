import json
import pytest
from pprint import pprint

# TEST_BUCKET_NAME= "bucket_2"
@pytest.fixture
def sqs_event_payload():
    def _payload(id, BUCKET_NAME):
        res = (id, BUCKET_NAME)
        print("executing _payload")
        return res
    print("before calling _payload")
    return _payload


@pytest.fixture(autouse=True)
def just_print():
    print("\nauto-fixture is run")
    yield
    print("\nAll test is done")

# Error
# @pytest.fixture
# def sqs_event_payload_1(id, TEST_BUCKET_NAME):
#     def _payload(id, TEST_BUCKET_NAME):
#         s3_key = f'{id}/{id}.pdf'
#         msg = {
#             'Records': [
#                 {
#                     's3': {
#                         'bucket': {'name': TEST_BUCKET_NAME},
#                         'object': {'key': s3_key},
#                     }
#                 }
#             ]
#         }
#         print(f"\ns3_key is {s3_key}")
#
#         body = {'Message': json.dumps(msg)}
#         res = {'Records': [{'body': json.dumps(body)}]}
#
#         print("\n")
#         pprint(res)
#         return res
#
#     return _payload
    # E
    # fixture 'id' not found
    # > available fixtures: cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, extra, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, sqs_event_payload, sqs_event_payload_1, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
    # > use
    # 'pytest --fixtures [testpath]'
    # for help on them.