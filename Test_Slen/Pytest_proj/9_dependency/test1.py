import random
import pytest


class TestAWS:

    @pytest.mark.dependency
    def test_instance_start(self):
        assert random.choice((True, False))

    @pytest.mark.dependency(depends=['TestAWS::test_instance_start'])
    def test_instance_stop(self):
        assert random.choice((True, False))

    @pytest.mark.dependency(depends=['TestAWS::test_instance_start'])
    def test_instance_delete(self):
        assert random.choice((True, False))


