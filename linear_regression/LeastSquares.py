import Statistics
import math

def totalVariability(x):

    size=Statistics.size(x)
    sumsquare=Statistics.sumSquares(x)
    sumx=Statistics.Sum(x)

    totalvariability=sumsquare-(math.pow(sumx,2)/size)

    return totalvariability

def variability(x,y):
    sumxy=Statistics.sumXY(x,y)
    sumx=Statistics.Sum(x)
    sumy=Statistics.Sum(y)
    size=Statistics.size(x)

    sxy=sumxy-(sumx*sumy)/size

    return sxy

def intercept(sxy,sxx):
    return sxy/sxx

def slope(my,b1,mx):
    return my-b1*mx

def sumSquaresError(syy,sxy,sxx,):
    return syy-math.pow(sxy,2)/sxx

def errorSquare(sxy,sxx,syy):
    return math.pow(sxy,2)/(sxx*syy)
