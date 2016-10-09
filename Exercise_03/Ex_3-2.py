def __init__(self, number_of_nucleiA = 100,number_of_nucleiB = 0, time_constant = 1, time_of_duration = 5, time_step = 0.05):
        # unit of time is second
        self.n_uraniumA = [number_of_nucleiA]
        self.n_uraniumB = [number_of_nucleiB]        
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.time = time_of_duration
        self.nsteps = int(time_of_duration // time_step + 1)
        print("Initial number of nucleiA ->", number_of_nucleiA)
        print("Initial number of nucleiB ->", number_of_nucleiB)
        print("Time constant ->", time_constant)
        print("time step -> ", time_step)
        print("total time -> ", time_of_duration)