#Program for Searching for all Upper Case Alphabets
#RegExpr7.py
import re
matdet=re.finditer("[A-Z]","Ak5Y#GnRp@7W&bPQs6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)