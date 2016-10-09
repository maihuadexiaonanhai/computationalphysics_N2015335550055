def store_results(self):
        myfile = open('nuclei_decay_data.txt', 'w')
        for i in range(len(self.t)):
            print(self.t[i], self.n_uraniumA[i], self.n_uraniumB[i], file = myfile)
        myfile.close()