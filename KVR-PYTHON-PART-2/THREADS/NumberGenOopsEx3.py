#Program for generating 1 to N numebrs by using threads
#NumberGenOopsEx3.py
import threading,time # Step-1
class Numbers: #Step-2
	def numbergenerate(self,n): # Step-3
		if(n<=0):
			print("{}--> {} is Invalid Input:".format(threading.current_thread().name))
		else:
			for i in range(1,n+1):
				print("{}-->Value of i={}".format(threading.current_thread().name,i))
				time.sleep(0.25)

#Main Program
threading.Thread(target=Numbers().numbergenerate,args=(int(input("How Many Numbers u want to Generate:")),)).start()
