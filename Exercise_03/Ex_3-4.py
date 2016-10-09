def show_results(self):
        pl.plot(self.t, self.n_uraniumA)
        pl.plot(self.t, self.n_uraniumB)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei')
        pl.show()