import pandas
#import csv
import Statistics
import RegressionLine

infileName='data/input.txt'
outfileName='data/output.txt'

#in out
data=pandas.read_csv('data/input.csv')
x=data["x"].tolist()
y=data["y"].tolist()

print '---------X------------'
print x
print '---------Y------------'
print y

#statistics
print '---------PARAMETERS------------'

mx=Statistics.Mean(x)
my=Statistics.Mean(y)
sx=Statistics.StandardDeviation(x)
sy=Statistics.StandardDeviation(y)
r=Statistics.Correlation(x, y)


print ('mean mx: %.2f'%(mx))
print ('mean my: %.2f'%(my))
print ('standard-deviation sx: %.3f'%(sx))
print ('standard-deviation sy: %.3f'%(sy))
print ('correlation xy: %.3f'%(r))

print '---------REGRESSION------------'
b=RegressionLine.slope(r,sx,sy)#slope
a=RegressionLine.intercept(mx,my,b)#intercept
function=RegressionLine.printRegressionLineFormula(b,a)

print ('slope b: %.3f'%(b))
print ('intercept A: %.3f'%(a))
print ('function: %s'%(function))


print '---------FINISH------------'

data.to_csv("data/output.csv",index=False, cols=['x','y'])
