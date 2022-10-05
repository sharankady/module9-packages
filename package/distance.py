class distance:
    
    def miles_to_kilometers(self,M):          
            self.M=M
            K=M/1.60934
            print(format(self.M),"Miles equal to ",K, "kms")

    def Kilometers_to_miles(self,K):
            self.K=K
            M=1.60934*K
            print(format(self.K),"kms equal to ",M, "miles")

d=distance()
d.miles_to_kilometers(12)
d.Kilometers_to_miles(14)