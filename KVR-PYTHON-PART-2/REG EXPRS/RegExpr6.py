#Program for Searching for all  except A or B or C only
#RegExpr6.py
import re
matdet=re.finditer("[^ABC]","Ak5#GnRp@7W&BYPQs6!CMx")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)