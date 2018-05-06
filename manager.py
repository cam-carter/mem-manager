from src.job import job
import math

jobs = {}
number_of_jobs = 4
page_size = 512
i = 0
for i in range(number_of_jobs):
    jobs[i] = job()

#this might actually be easier with dynamic input :)
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

frame = [0] * 20 #initially start out with a larger size

for i in range(0, number_of_jobs):
    counter = 0 # used as a counter for the pages
    for k in range (0, number_of_jobs): #checks for deallocs in each job at every step
        if jobs[k].hasDealloc == True:
            if i == jobs[k].deallocTime: #if it's time to deallocate
                jobs[k].hasDealloc = False #set to false
                for n in range(0, 15): #replace all the frames with 0
                    if frame[n] == k+1:
                        frame[n] = 0
    for j in range(len(frame)): # if the spot is open, place page in slot
        if frame[j] == 0:
            if counter < jobs[i].pages_occupied: # page counter
                frame[j] = i+1
                counter += 1

for i in range (len(frame)): # trims the excess list, I could use appends
    if frame[i] == 0:        # but for the sake of this project, keep it simple
        del frame[i:]
        break

for i in range(len(frame)): # print out the frame
    print('| %d ' % frame[i], end="")
print ('|')

frame_byte = 0 # the byte of the frame
inner_frame_byte = 0 # the frame bytes from the start of the pages
page_counter = 0 # the counter of pages

for i in range (0, number_of_jobs):
    #initialize variables
    frame_byte = 0
    inner_frame_byte = 0
    page_counter = 0
    #for each logical address
    for j in range(len(jobs[i].logical_address)):
        #reset these for each logical address because we are going to search
        #the entire array every time
        frame_byte = 0
        inner_frame_byte = 0
        page_counter = 0
        for k in range(len(frame)):
            #if we find the job number...
            if frame[k] == i + 1:
                #if the inner byte is less than the logical address and
                #it's less than the next frame, then append the frame number,
                #the page, and the physical address, ()(frame - page) * 512 ) + logical
                if (inner_frame_byte <= jobs[i].logical_address[j] and
                (inner_frame_byte+512) > jobs[i].logical_address[j]):
                    jobs[i].frame_number.append(k)
                    jobs[i].page_number.append(page_counter)
                    jobs[i].physical_address.append(((k - page_counter) * 512) +
                    (jobs[i].logical_address[j]))
                    break # break so we stop searching for this logical address
                else:
                    #we're still inside the file, so keep going
                    inner_frame_byte += 512 # increase the inner frame byte
                    page_counter += 1 # increase the page counter
            frame_byte += 512 #increment the frame

#if we found there was an error (out of bounds memory location address)
#display that!
for i in range (0, number_of_jobs):
    for j in range (len(jobs[i].logical_address)):
        if jobs[i].pages_occupied * 512 < jobs[i].logical_address[j]:
            jobs[i].frame_number.append('ERROR')
            jobs[i].page_number.append('ERROR')
            jobs[i].physical_address.append('ERROR')

for i in range(0, number_of_jobs):
    print('Job ' + repr(jobs[i].job_number) + ':')
    print('Logical address: ' + repr(jobs[i].logical_address))
    print('Page referenced: ' + repr(jobs[i].page_number))
    print('Frame number: ' + repr(jobs[i].frame_number))
    print('Physical address: ' + repr(jobs[i].physical_address) + '\n')
