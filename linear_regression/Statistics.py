import math

def size(x):
    return x.__len__()

def Sum(x):
    sum=0
    for xi in x:
        sum=sum+float(xi)
    return sum

def sumSquares(x):
    sumsquare=0
    for xi in x:
        sumsquare=sumsquare+math.pow(xi,2)
    return sumsquare

def sumXY(x,y):
    sum=0
    for i in range(0,x.__len__()):
        sum=sum+x[i]*y[i]
    return sum

def Mean(x):
    len=x.__len__()
    sum=Sum(x)
    mean=sum/len
    return mean

def Variance(x):
    len = x.__len__()
    mean=Mean(x)
    sum=0
    for xi in x:
        sum=sum+math.pow(xi-mean,2)
    variance = sum/(len-1)
    return variance

def StandardDeviation(x):
    return math.sqrt(Variance(x))


def Covariance(x,y):
    meanx=Mean(x)
    meany=Mean(y)
    len = x.__len__()
    sum=0
    for i in range(0, x.__len__()):
        sum=sum+(x[i]-meanx)*(y[i]-meany)
    covariance=sum/(len-1)
    return covariance

def Correlation(x,y):
    correlation=Covariance(x,y)/math.sqrt(Variance(x)*Variance(y))
    return correlation

def Correlation2(x,y):
    #sum xy
    sumxy=0
    sumx2=0
    sumy2=0
    for i in range(0,x.__len__()):
        sumxy=sumxy+x[i]*y[i]
        sumx2=sumx2+math.pow(x[i],2)
        sumy2=sumy2+math.pow(y[i],2)


    correlation=sumxy/math.sqrt(sumx2*sumy2)
    return correlation

#standard deviation: is the square root of variance
#variance: variance^2= [sum (x-mean)^2]/n
