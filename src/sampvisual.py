# -*- coding: utf-8 -*-
"""
Created on Tue May 12 10:46:08 2020

@author: siavash tabrizian stabrizian@smu.edu
"""
import os
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

        
'''
   This class contains the subroutine for visualization using the sampling 
   and resampling classes.
   
   resampling input is an instance of resampling class from the resampling module
'''
class visualsamp():
    def __init__(self, resampling, loc):
        self.resample = resampling
        self.loc = loc
        if not os.path.exists(self.loc):
            os.makedirs(self.loc)
        self.figcount = 0
    
    #Visualization on law of large numbers 
    def lawlargevs(self, minssize = 10, maxssize = 100, \
                   increment = 10, samptype = ['SRS'], separate = False,\
                   title = 'Law of Large Numbers'):
        truemean = self.resample.sampling.dist.getmu()
        if separate == False:
            fig = plt.figure(num = self.figcount)
        for st in samptype:
            self.resample.samptype = samptype
            mean = []
            expnum = 0
            confupp = []
            confdwn = []
            x = []
            for sz in range(minssize,maxssize,increment):
                x.append(sz)
                self.resample.rssize = sz
                [o1,o2] = self.resample.monte_carlo()
                mean.append(o1)
                mu.append(truemean)
                [o1, o2] = self.resample.getCI(o1,o2)
                confupp.append(o1)
                confdwn.append(o2)
                expnum += 1
            if separate == True:
                self.figcount += 1
                fig = plt.figure()
                plt.plot(np.array(x),np.array(mean))
                plt.plot(np.array(x),np.array(mu))
                plt.fill_between(np.array(x),np.array(confupp),np.array(confdwn), alpha = 0.3)
                plt.xlabel('Number of observations --->')
                plt.ylabel('Estimation value --->')
                plt.title(title)
                plt.grid(True)
                plt.savefig(self.loc + '/lawlarge' + samptype)
                plt.show()
            else:
                plt.plot(np.array(x),np.array(mean))           
        plt.plot(np.array(x),np.array(mu))
        plt.xlabel('Number of observations --->')
        plt.ylabel('Estimation value --->')
        plt.title(title)
        plt.grid(True)
        plt.savefig(self.loc + '/lawlarge')
        plt.show()
    
    #Histogram representation of the sampling method comparing to normal dist
    #This is experimenting the central limit theorem
    def centlimit(self, ssize = 100, \
                   samptype = 'SRS', separate = False,\
                   num_bins =20, title = 'Central limit theorem'):
        truemean = self.resample.sampling.dist.getmu()
        self.resample.samptype = samptype
        self.resample.rssize = ssize
        [o1,o2] = self.resample.monte_carlo()
        meanlist = []
        std = self.resample.std
        for m in o2:
            meanlist.append((m-truemean)/(std/np.sqrt(len(o2))))
        n, bins, patches = plt.hist(np.array(meanlist), num_bins, normed = 1, \
                                    facecolor = 'blue', alpha = 0.5) 
        y = mlab.normpdf(bins,0.0,1.0)
        plt.plot(bins,y,'r--')
        plt.xlabel('mean estimates')
        plt.ylabel('probabilities')
        plt.title(title)
        plt.show
        plt.savefig(self.loc + '/central')