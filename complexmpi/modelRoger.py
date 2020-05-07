import numpy as np


class ModelRoger(object):
        '''Toy class which simulates some data for testing astroABC sampler'''
        def __init__(self,name,num):
                self.name=name
                self.num=num

        def make_mock(self, paramet):
                '''
                Input:
                        param: variable to generate either exponential data or Normal data with variance = var
                '''
                
                var1=np.array(paramet[1])
                #print(type(var1))
                param1=paramet[0]
                #print(type(param1))
                if self.name == "exp":
                        b = 1/param1
                        return np.random.exponential(b,self.num)
                if self.name == "normal":
                        if isinstance(var1,float):
                                sigm = np.diag(np.ones(len(param1))*var)
                        elif len(var1)==len(param1):
                                sigm = np.diag(var1)
                        else:
                                sigm = var1.reshape(len(param1),len(param1)) #covariance matrix
                        return np.random.multivariate_normal(param1,sigm,self.num)

