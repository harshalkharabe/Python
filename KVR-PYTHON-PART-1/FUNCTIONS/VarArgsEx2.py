#Program for Demonstrating the Need of Variable Length Arguments
#This Program will Execute 
#VarArgsEx2.py
def  disp(a,b,c,d,e): # # Function Def-1  with 5 Pos Params
	print(a,b,c,d,e)
disp(10,20,30,40,50) # Function Call-1 with 5 Pos Args
#-----------------------------------------------------------------------------------------------
def  disp(a,b,c,d): # # Function Def-2  with 4 Pos Params
	print(a,b,c,d)
disp(10,20,30,40) # Function Call-2 with 4 Pos Args
#-----------------------------------------------------------------------------------------------
def  disp(a,b,c): # # Function Def-3  with 3 Pos Params
	print(a,b,c)
disp(10,20,30) # Function Call-3 with 3 Pos Args
#-----------------------------------------------------------------------------------------------
def  disp(a,b): # # Function Def-4  with 2 Pos Params
	print(a,b)
disp(10,20) # Function Call-4 with 2 Pos Args
#-----------------------------------------------------------------------------------------------
def  disp(a): # # Function Def-5  with 1Pos Params
	print(a)
disp(10) # Function Call-5 with 1 Pos Args
#-----------------------------------------------------------------------------------------------

# NOTEL: In General If we have n-Function Calls then Python Programmer
# Must Define n-Function Defintions . This is Process is Time consuming Process.

#NOTE: Let Us have n-Function Calls with Variable Length args then by using By using Var Length args concept
#				we define Single Function Definition.


