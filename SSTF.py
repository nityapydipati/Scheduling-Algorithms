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
contents = [x.strip('\n') for x in f.readlines()]


initial_position=int(contents[0])
processes=contents[1].split(" ")
for p in processes:
	queue.append(int(p))
final_queue.append(initial_position)



for i in range(0,len(queue)):
	min_q=1000000000000
	for j in range(0,(len(queue))):
		
		
		
		if(queue[j] in final_queue):
			
			
			continue;
		a=abs(queue[j]-initial_position)
		
		


		if(min_q>a):

			min_q=a;

			pos=j;
			
		
	
	
	initial_position=queue[pos]


	
	final_queue.append(initial_position)		
	

for i in range(0,len(final_queue)-1):
	total_seek_time+=abs(final_queue[i]-final_queue[i+1])

print total_seek_time





	
	

	
	
	
	







	
