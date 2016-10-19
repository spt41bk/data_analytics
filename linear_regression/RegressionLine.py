
def slope(r,sx,sy):
    return r*(sy/sx)

def intercept(mx,my,b):
    return my-b*mx

def printRegressionLineFormula(b,a):
    function=('Y\' = %.3fX + %.3f' %(b,a))
    return function