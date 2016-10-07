import sys
import math

queue=[]
start=0
end=199
first_pass=[]
second_pass=[]
total_seek_time1=0
total_seek_time2=0

f = open(sys.argv[1],"r")
process = [x.strip('\n') for x in f.readlines()]


initial_position=int(process[0])
queue.append(initial_position)
processes=process[1].split(" ")
for p in processes:
	queue.append(p)

queue= sorted(map(int, queue))

for q in queue:
	if q<=initial_position:
		first_pass.append(q)
	else:
		second_pass.append(q)

second_pass=sorted(second_pass, reverse=True)


for i in xrange(0,len(first_pass)-1):

	temp=abs(int(first_pass[i])-int(first_pass[i+1]));
	total_seek_time1+=temp;


for i in xrange(0,len(second_pass)-1):
	temp1=abs(int(second_pass[i])-int(second_pass[i+1]));
	total_seek_time2+=temp1;
    
print total_seek_time1+total_seek_time2
















