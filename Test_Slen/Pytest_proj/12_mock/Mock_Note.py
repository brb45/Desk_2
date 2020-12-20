# pytest-mock 3.3.1
# pip install pytest-mockCopy PIP instructions
#

# Mock is defined as
# The replacement of one or more function calls or objects with mock calls or objects
# A mock function call returns a predefined value immediately, without doing any work.
# A mock object's attributes and methods are similarly defined entirely in the test,
# without creating the real object or doing any work. The fact that the writer of the test
# can define the return values of each function call gives him or her a tremendous amount
# of power when testing, but it also means that s/he needs to do some foundational
# work to get everything set up properly.

# In Python, mocking is accomplished through the unittest.mock module.
# The module contains a number of useful classes and functions, the most important of which
# are the patch function (as decorator and context manager) and the MagicMock class.
# Mocking in Python is largely accomplished through the use of these two powerful components.

# The overall procedure is as follows:
#
# Write the test as if you were using real external APIs.
# In the function under test, determine which API calls need to be mocked out; this should be a small number.
# In the test function, patch the API calls.
# Set up the MagicMock object responses.
# Run your test.

# If your test passes, you're done. If not, you might have an error in the function under test,
# or you might have set up your MagicMock response incorrectly.

# But when and why should we mock?
# When we write software, we will often need to make calls to functions that are external to our code:
# for example calls to the operating system, HTTP requests to external APIs,
# calls to functions we don’t control directly but which our software depends on.
#
# Well, for each of these cases (and not only) it is necessary to simulate the output of external
# functions in order to carry out consistent software tests.

# unittest.mock
# pytest-mock
# Monkeypatching



















# Mocks are always white-box tests. You can’t use them without peeking into the code, so they are most useful
# for developers and not so much for testing specifications. It is a tradeoff that the developer has to accept.

# API mock test in general is part of white box unit test for developers.
# For testers, it is useful for mock during API flow testing.

# when to use mock for QA test, besides unit test from developer's view
# 1. If API under test has dependencies from other API calls, which can be mocked
# 2. Test API standalone, when the api is part of a API flow. APIs on
# the upper end will be mocked.

# Think which mock method I should use
# So far
# 1. using reponses
