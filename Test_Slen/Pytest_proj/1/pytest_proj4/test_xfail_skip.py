import pytest
@pytest.mark.skip
def testadd_1():
	assert 100+200 == 400,"failed"

@pytest.mark.skip
def testadd_2():
	assert 100+200 == 300,"failed"

@pytest.mark.xfail
def testadd_3():
	assert 15+13 == 28,"failed"

@pytest.mark.xfail
def testadd_4():
	assert 15+13 == 100,"failed"

def testadd_5():
	assert 3+2 == 5,"failed"

def testadd_6():
	assert 3+2 == 6,"failed"

import os
print(os.getcwd())
print("import pytest_proj4.test_xfail_skip.py")


