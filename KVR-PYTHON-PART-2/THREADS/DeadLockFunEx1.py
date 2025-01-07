#Program for Demonstrating the Occurence of Dead Lock 
#DeadLockFunEx1.py
import threading,time
def MulTable(n):
	if(n<=0):
		print("{}--> {} is Invalid Input".format(n))
	else:
		for i in range(1,11):
			print("\t{}---->{} x {}={}".format(threading.current_thread().name,n,i,n*i))
			time.sleep(1)
		print("-------------------------------------------------------------")

#Main Program
#Create sub threads
t1=threading.Thread(target=MulTable,args=(19,))
t2=threading.Thread(target=MulTable,args=(17,))
t3=threading.Thread(target=MulTable,args=(9,))
t4=threading.Thread(target=MulTable,args=(14,))
#dispatch the sub threads
t1.start()
t2.start()
t3.start()
t4.start()