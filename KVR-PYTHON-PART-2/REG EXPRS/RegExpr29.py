#Program for Searching  Zero K or One K OR More K's
#RegExpr29.py
import re
matdet=re.finditer("K*","KVKKVKKKVKV")
print("-"*50)
for mat in matdet:
	print("Start Index:{}  End Index:{}  Value:{}".format(mat.start(),mat.end(), mat.group()))
print("-"*50)