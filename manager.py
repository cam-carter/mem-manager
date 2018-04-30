from src import job

jobs = {}
number_of_jobs = 4
i = 0
for i in range(number_of_jobs):
    jobs[i] = job()

jobs[0].request = A
jobs[0].job_number = 1
jobs[0].memory_requested = 4096

jobs[1].request = A
jobs[1].job_number = 2
jobs[1].memory_requested = 2000

jobs[2].request = A
jobs[2].job_number = 3
jobs[2].memory_requested = 3088

jobs[3].request = A
jobs[3].job_number = 4
jobs[3].memory_requested = 688

jobs[1].logical_address.append(1096)
jobs[1].logical_address.append(3)

jobs[2].logical_address.append(2000)
jobs[2].logical_address.append(5200)

jobs[3].logical_address.append(0)

