from src.job import job
import math

jobs = {}
number_of_jobs = 4
page_size = 512
i = 0
for i in range(number_of_jobs):
    jobs[i] = job()

jobs[0].job_number = 1
jobs[0].memory_requested = 4096
jobs[0].hasDealloc = True
jobs[0].deallocTime = 2 # deallocates after 2 has been allocated

jobs[1].job_number = 2
jobs[1].memory_requested = 2000

jobs[2].job_number = 3
jobs[2].memory_requested = 3088

jobs[3].job_number = 4
jobs[3].memory_requested = 688

jobs[1].logical_address.append(1096)
jobs[1].logical_address.append(3)

jobs[2].logical_address.append(2000)
jobs[2].logical_address.append(5200)

jobs[3].logical_address.append(0)

for i in range (0, number_of_jobs):
    jobs[i].pages_occupied = math.ceil(jobs[i].memory_requested / 512)

frame = [0] * 20
frame_counter = 0
page_size = 512

for i in range(0, number_of_jobs):
    counter = 0
    for k in range (0, number_of_jobs): #checks for deallocs in each job at every step
        if jobs[k].hasDealloc == True:
            if i == jobs[k].deallocTime: #if it's time to deallocate
                jobs[k].hasDealloc = False #set to false
                for n in range(0, 15): #replace all the frames with 0
                    if frame[n] == k+1:
                        frame[n] = 0
    for j in range(0, 15):
        if frame[j] == 0:
            if counter < jobs[i].pages_occupied:
                frame[j] = i+1
                counter += 1
for x in range(0, 15):
    print('%d | ' % frame[x], end="")
print ("")
frame_byte = 0
inner_frame_byte = 0
page_counter = 0

for r in range (1, number_of_jobs):
    frame_byte = 0
    inner_frame_byte = 0
    page_counter = 0
    for u in range(len(jobs[r].logical_address)):
        frame_byte = 0
        inner_frame_byte = 0
        page_counter = 0
        for w in range(0, 15):
            if frame[w] == r + 1:
                if (inner_frame_byte < jobs[r].logical_address[u] and
                (inner_frame_byte+512) > jobs[r].logical_address[u]):
                    jobs[r].frame_number.append(w)
                    jobs[r].page_number.append(page_counter)
                    jobs[r].physical_address.append((w * 512) +
                    jobs[r].logical_address[u])
                    break
                elif jobs[r].logical_address[u] == 0:
                    jobs[r].frame_number.append(w)
                    jobs[r].page_number.append(page_counter)
                    jobs[r].physical_address.append(frame_byte)
                    break
                else:
                    inner_frame_byte += 512
                    page_counter += 1

            frame_byte += 512

for i in range(1, number_of_jobs):
    print('Job ' + repr(jobs[i].job_number) + ':')
    print('Logical address: ' + repr(jobs[i].logical_address))
    print('Page referenced: ' + repr(jobs[i].page_number))
    print('Physical address: ' + repr(jobs[i].physical_address))
    print('Frame number: ' + repr(jobs[i].frame_number) + '\n')
