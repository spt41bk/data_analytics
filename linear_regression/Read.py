

def readVariable(fileName,variableName):
    x=[]
    fi=open(fileName,'r')
    for line in fi:
        if(line.__contains__(variableName)):
            xline=line.split()
            for xi in xline:
                if not xi.__contains__(variableName):
                    x.append(float(xi))
    fi.close()
    return x

#fi=open('data/input.txt','r')
#fo=open('data/output.txt','w')

#x=[]
#y=[]
#for line in fi:
 #   print line
  #  if line.__contains__('x'):
   #     xline=line.split()
    #    for xi in xline:
     #       if not xi.__contains__('x'):
                #print xi
      #          x.append(xi)
   # if line.__contains__('y'):
    #    yline=line.split()
     #   for yi in yline:
      #      if not yi.__contains__('y'):
       #         y.append(yi)

#print x.__len__()
#for xi in x:
 #   print xi

#for yi in y:
 #   print yi

#fi.close()
#fo.close()

