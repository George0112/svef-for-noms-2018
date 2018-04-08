import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
#import seaborn as sns
np.set_printoptions(threshold=np.inf)
mpl.rcParams['lines.markersize'] = 10

arr = np.zeros((5, 310), dtype=int)
#for i in range(4):
#	arr[0][i] = 'layer%d' %i

for line in open('receivedtrace.txt'):
	if(int(line.split()[1]) <= 10):
		arr[0][int(line.split()[8])] = 1
	else:
		arr[int(line.split()[4])+1][int(line.split()[8])] = 1
	print(line.split()[4], line.split()[8])
#for i in range(150):
#    arr[0][2*i] = 1

print (arr)
labels = ['header', 'layer0', 'layer1', 'layer2', 'layer3']

plt.imshow(arr, interpolation='nearest', cmap=plt.cm.Reds, aspect='auto')
plt.yticks(range(arr.shape[0]), labels)
#plt.plot(x,y,'rs')
plt.axis([-1,310,-1,6])
#ax = plt.subplots()
#heatmap = plt.pcolor(x,y)
plt.show()
