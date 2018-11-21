import numpy as np 
import matplotlib.pyplot as plt 

def function(x):        #define the function to integrate
    return np.cos(x)

def integration(f,a,b,n):
    #f = the function to integrate
    #a = lower bound in x
    #b = upper bound in x
    #n = the number of random points to generate

    #create x and y arrays along the function in order to find the upper and lower bounds in y
    x = np.linspace(a,b,n)
    y = f(x)
    c = np.amin(y)   #lower bound in y
    d = np.amax(y)   #upper bound in y

    if(np.sign(c)==np.sign(d)):     #if the entire range of the function is above or below y=0,
            if(c<0):                # make sure that the area between the lower/upper bound and
                d = 0               # the x-axis is counted by setting that bound = 0
            elif(c>0):
                c = 0

    #create x and y arrays of random points
    xr = np.zeros(n)
    yr = np.zeros(n)
    for i in range(n):
        xr[i] = np.random.random()*(b-a)    #spread the random points over the area
        yr[i] = np.random.random()*(d-c)    # of the function
        if(c<0):                #if the lower bound is negative, shift the area down so that
            yr[i] += c          # some points are negative
        

    pos_area_pts = 0.0      #positive points - points above y=0
    neg_area_pts = 0.0      #negative points - points below y=0
    for i in range(n):
        if((yr[i]>=0 and f(xr[i])>=0) and np.fabs(yr[i])<=np.fabs(f(xr[i]))):   #for each random point:
            pos_area_pts += 1.0                                                 # •if it is positive & under the curve,
            #print("Positive point found: (%s, %s)"%(xr[i],yr[i]))              #   count in positive pts
        elif((yr[i]<0 and f(xr[i])<0) and np.fabs(yr[i])<=np.fabs(f(xr[i]))):   # •if it is negative & over the curve,
            neg_area_pts += 1.0                                                 #   count in negative pts
            #print("Negative point found: (%s, %s)"%(xr[i],yr[i]))

    area_pts = pos_area_pts - neg_area_pts      #subtract negative area from positive area
    ratio = area_pts/n                      #calculate the ratio of points under the curve to total points
    area = ratio*(b-a)*(d-c)            #apply the ratio to the total area within the bounds

    return area 

a = 0.0
b = 1.75
npoints = 1000

answer = np.sin(1.75)       #calculate the true answer for this specific function
mcintegral = 0.0            #calculate the monte carlo integral
for i in range(1000):                                   #I average the result of 1000 calculations in order
    mcintegral += integration(function,a,b,npoints)     # to obtain better accuracy - functionally, I am
mcintegral /= 1000                                      # generating 1 million points.
print("Answer = "+str(answer))              #print the true answer and the monte carlo result
print("Monte Carlo = "+str(mcintegral))     # and compare