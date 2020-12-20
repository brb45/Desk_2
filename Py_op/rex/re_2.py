"""
import re
xx = "guru99,education is fun"
r1 = re.findall(r"\w+",xx)
print(r1)

"""
import re
line = "wifi nup test are prepare testerType wifi nup test prepare testerType"
match_obj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)
if match_obj:
    print("match_obj.group() : ", match_obj.group())
    print("match_obj.group(1) : ", match_obj.group(1))
    print("match_obj.group(2) : ", match_obj.group(2))
    print("match_obj.groups() : ", match_obj.groups())
    #print("match_obj.group(4) : ", match_obj.group(4))

else:
    print("No match")
"""
match_obj.group() :  wifi nup test are prepare testerType
match_obj.group(1) :  wifi nup test
match_obj.group(2) :  prepare
match_obj.groups() :  ('wifi nup test', 'prepare')
"""

s = 'QAtest group id, and Silicon_QAfasttest@litepoint.com is server email.'
domain = re.search("QA\w+", s)
if domain:
    print(domain.groups())
    print(domain.group(0))
    print(domain.group())

s = "tes _tid"
match_obj = re.search("\w+",s)
print(match_obj.groups())
print(match_obj.group(0))
print(match_obj.group(1))
print(match_obj.group())

match_obj = re.findall("\w+", s)
print(match_obj.groups())
print(match_obj.group(0))
print(match_obj.group(1))
print(match_obj.group())
print(match_obj)


