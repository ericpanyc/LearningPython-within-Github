#!/usr/bin/python
import re
phone = "602-343-8747"
area_code = re.search(r'^\d*', phone)
print ('The area code is: ' + area_code.group())
