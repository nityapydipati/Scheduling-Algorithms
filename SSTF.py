import sys
import math

queue=[]
start=0
end=199
total_seek_time=0
final_queue=[]
initial_position=0
pos=0

f = open(sys.argv[1],"r")
process = [x.strip('\n') for x in f.readlines()]


initial_position=int(process[0])
processes=process[1].split(" ")
for p in processes:
	queue.append(int(p))
final_queue.append(initial_position)
k=0
for i in range(0,len(queue)):
	min_q=1000000000000
	
	for j in range(0,(len(queue))):
		
		
		if(queue[j] in final_queue):
			
			continue;
		a=abs(queue[j]-initial_position)

		if(min_q>=a):
			#determining if first step or not
			if(min_q==a and k==0):
				if(abs(initial_position-start)<abs(initial_position-end)):
					if(start<queue[pos]<initial_position):
						min_q=a;
						pos=pos;
					elif(start<queue[j]<initial_position):
						min_q=a;
						pos=j;
				else:
					if(initial_position<queue[pos]<end):
						min_q=a;
						pos=pos;
					elif(initial_position<queue[j]<end):
						min_q=a;
						pos=j;
			elif(min_q==a and k!=0):
				if(abs(queue[j-1])<abs(queue[j])):
					min_q=a;
					if(queue[pos]>queue[j]):
						pos=pos
					else:
						pos=j
					
				else:
					min_q=a;
					if(queue[pos]>queue[j]):
						pos=j
					else:
						pos=pos


			else:
				min_q=a;
				pos=j;
	
	k=k+1

	
	initial_position=queue[pos]
	final_queue.append(initial_position)		
	

for i in range(0,len(final_queue)-1):
	total_seek_time+=abs(final_queue[i]-final_queue[i+1])

print total_seek_time





	
	

	
	
	
	







	
