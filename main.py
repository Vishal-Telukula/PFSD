print("hello")
print("covid is spreading")
# we deal 4 topics in pytest
# 1.test case - one condition and one outcome
# 2.test suite - group of test cases
# 3.Fixtures - condition or method which is executed before or after the test case
# 4.Parameterized testing - test cases with generic variables
# Rules for pytest : 1.dedicated folder should be created for testing
#                          2.the testing file should be names Test_pythonfilename
#                          3. py.test command in our directory
# Keywords for pytest : 1.Assert - notifying
#                       2.Check - check if internet is available or not
#                       3.Yeild - for successful completion of test case yeild is used for notification
#                       4.Mark - used for parameterized testing
# Decorators - annotations(@Fixture)
# smaple program for pytest fixture
balance = 5000


def withdraw(amount):
    global balance
    balance -= amount
    return balance


def deposit(amount):
    global balance
    balance += amount
    return balance
