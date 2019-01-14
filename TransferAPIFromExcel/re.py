# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"[0-9]{3,7}"

test_str = ("\"statuscode\": 2020000,,\n\n"
	"response body: \n"
	"{\n"
	"                        }")

m = re.search(regex, test_str)
print(m)

# You can manually specify the number of replacements by changing the 4th argument
# result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

# if result:
#     print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.