import sys
import math

queue=[]

f = open(sys.argv[1],"r")
process = [x.strip('\n') for x in f.readlines()]


initial_position=process[0]
queue.append(initial_position)
processes=process[1].split(" ")
for p in processes:
	queue.append(p)

total_seek_time=0

for i in xrange(0,len(queue)-1):

	temp=abs(int(queue[i])-int(queue[i+1]));
	total_seek_time+=temp;

print total_seek_time
    
    
    
    

    
	    
	    
		    
	    
		    
	

	    





	
	
