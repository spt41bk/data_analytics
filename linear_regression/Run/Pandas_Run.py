import pandas

data=pandas.read_csv('../data/input.csv')
x=data["x"].tolist()
z=[]
data = data.reindex( data.columns.values + ['z'])

print data
#z=[]
#z[0]='z0'

#data.to_csv("../data/output-pandas.csv",index=False, cols=['x','y','z'])


print x