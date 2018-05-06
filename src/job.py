class job():
    def __init__(self):
        self.job_number = 0
        self.memory_requested = 0
        self.logical_address = []
        self.pages_occupied = 0
        self.frame_number = []
        self.page_number = []
        self.physical_address = []
        self.hasDealloc = False
        self.deallocTime = 999
