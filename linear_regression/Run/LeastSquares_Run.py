import pandas
import LeastSquares
import Statistics
import RegressionLine

#in out
data=pandas.read_csv('../data/input-least-squares.csv')
x=data["x"].tolist()
y=data["y"].tolist()

print '---------X------------'
print x
print '---------Y------------'
print y

print '---------LEAST SQUARES------------'
mx=Statistics.Mean(x)
my=Statistics.Mean(y)
sxx=LeastSquares.totalVariability(x)
syy=LeastSquares.totalVariability(y)
sxy=LeastSquares.variability(x,y)
b1=LeastSquares.intercept(sxy,sxx)
b0=LeastSquares.slope(my,b1,mx)
function=RegressionLine.printRegressionLineFormula(b1,b0)
sse=LeastSquares.sumSquaresError(syy,sxy,sxx)
r2=LeastSquares.errorSquare(sxy,sxx,syy)


print ('mean:')
print ('mx: %.3f'%(mx))
print ('my: %.3f'%(my))

print('total variability:')
print ('sxx: %.3f'%(sxx))
print ('syy: %.3f'%(syy))
print ('sxy: %.3f'%(sxy))

print ('parameters:')
print ('intercept b1: %.3f'%(b1))
print ('slope b0: %.3f'%(b0))
print ('function: %s'%(function))


print ('error:')
print ('error sse: %.3f'%(sse))
print ('error r2: %.3f'%(r2))
print ('%.0f %% of the variability in y is explained by linear regression'%(r2*100))

