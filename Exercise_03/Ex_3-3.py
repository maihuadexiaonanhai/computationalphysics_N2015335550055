def calculate(self):
        for i in range(self.nsteps):
            tmpA = self.n_uraniumA[i] + self.n_uraniumB[i] / self.tau * self.dt - self.n_uraniumA[i] / self.tau * self.dt
            tmpB = self.n_uraniumB[i] + self.n_uraniumA[i] / self.tau * self.dt - self.n_uraniumB[i] / self.tau * self.dt         
            self.n_uraniumA.append(tmpA)
            self.n_uraniumB.append(tmpB)            
            self.t.append(self.t[i] + self.dt)