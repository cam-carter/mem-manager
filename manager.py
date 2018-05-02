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

frame_counter = 0
page_size = 512

i = 0
while True:
    jobs[i].pages_occupied = math.ceil(jobs[i].memory_requested / 512)
    if jobs[i].memory_requested <= page_size:
        jobs[i].frame_number = frame_counter
    i += 1
    frame_counter += 1
    page_size += 512
    if i == number_of_jobs:
        break

for i in range(1, number_of_jobs):
    print('Job ' + repr(jobs[i].job_number) + ':')
    print('Physical address: ' + repr(jobs[i].memory_requested))
    if jobs[i].logical_address:
        for j in range(len(jobs[i].logical_address)):
            print('Logical address: ' + repr(jobs[i].logical_address[j]))
            print('Page referenced: ' + repr(math.ceil(jobs[i].logical_address[j] / 512)))
    print('Pages occupied: ' + repr(jobs[i].pages_occupied))
    print('Frame number: ' + repr(jobs[i].frame_number) + '\n')
    

