#Program for Searching  for  Word Characters ( Alphabets+Digits) Only
#RegExpr23.py
import re
matdet=re.finditer(r"\w","Ak5Y#GnRp@7W&bP)s6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)