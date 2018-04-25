# to find job page
page_size = 512 # byte counter for pages, starts at 512 bytes
page_counter = 1 # page counter, starts at first page
i = 0 # index for job number
for i in range(number_of_jobs):
    # if the memory request for the current job is less than the size of the page,
    # then the current jobs page number is set equal to the page counter
    # if the memory request for the current job is greater than the size of the page,
    # then the page counter and page size is iterated
    if jobs[i].memory_requested <= page_size:
        jobs[i].page_number = page_counter # sets page number of job to current page counter
        i += 1 # iterates to next job
        page_size = 512 # resets page_size
        page_counter = 1 # resets page_counter
    else:
        page_size += 512 # iterates page_size
        page_counter += 1 # iterates page_counter

# create jobs from file
for i in range(number_of_jobs):
    jobs[i] = Job()
    jobs[i].create('input/inputfilewhatever.text')
