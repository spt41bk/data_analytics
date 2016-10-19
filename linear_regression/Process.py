import Read
import Statistics
import RegressionLine

infileName='data/input.txt'
outfileName='data/output.txt'

#read input
x=Read.readVariable(infileName,'x')
y=Read.readVariable(infileName,'y')


#test
#example: http://onlinestatbook.com/2/regression/intro.html
print '---------X------------'
for xi in x:
    print xi
print '---------Y------------'

for yi in y:
    print yi

#mean and sum
#print ('sum x: %.2f'%(Functions.Sum(x)))
#print ('sum y: %.2f'%(Functions.Sum(y)))

print '---------PARAMETERS------------'

mx=Statistics.Mean(x)
my=Statistics.Mean(y)
sx=Statistics.StandardDeviation(x)
sy=Statistics.StandardDeviation(y)
r=Statistics.Correlation(x, y)


print ('mean mx: %.2f'%(mx))
print ('mean my: %.2f'%(my))

#print ('variance x: %.2f'%(Functions.Variance(x)))
print ('standard-deviation sx: %.3f'%(sx))
print ('standard-deviation sy: %.3f'%(sy))
#print ('covariance: %.3f'%(Functions.Covariance(x,y)))
print ('correlation xy: %.3f'%(r))

print '---------REGRESSION------------'
b=RegressionLine.slope(r,sx,sy)#slope
a=RegressionLine.intercept(mx,my,b)#intercept
function=RegressionLine.printRegressionLineFormula(b,a)

print ('slope b: %.3f'%(b))
print ('intercept A: %.3f'%(a))
print ('function: %s'%(function))


print '---------FINISH------------'


fo=open(outfileName,'w')

fo.write('--------statistics--------:\n')
fo.write('mean: mx=%.3f\n'%(mx))
fo.write('mean: my=%.3f\n'%(my))
fo.write('standard deviation: sx=%.3f\n'%(sx))
fo.write('standard deviation: sy=%.3f\n'%(sy))
fo.write('correlation xy: %.3f\n'%(r))

fo.write('\n')
fo.write('--------regression line--------:\n')
fo.write ('slope b: %.3f\n'%(b))
fo.write ('intercept A: %.3f\n'%(a))
fo.write ('function: %s\n'%(function))
fo.write('\n')
fo.write('--------finish!--------:\n')
fo.close()

#error
#y1=Read.readVariable(infileName,'y1')
#print'index \t y \t y1 \t error \t sqr(error)'
#for i in range(0,5):
#    error = y[i]-y1[i]
#    sqrError=math.pow(error,2)
#    print ('i=%d \t %f \t %f \t %f \t %f'%(i,y[i],y1[i],error, sqrError))