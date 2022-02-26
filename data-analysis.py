import math
data = [9,10,8,6,8,5,5,3,9,2,8,4,10,9,2,5,7,2,4,6,7,4,2,8,8,5]
mean = None
total = 0
total2 = 0
σ = None
data = sorted(data)
print(data)
#Standard dev
for i in data:
  total+=i
  total2 += i**2
mean = total/len(data)
sd1 = (total2)/len(data)
sd2 = mean**2
σ = math.sqrt(sd1 - sd2)
print("stdev =",σ)
print("mean = ",mean)
#median
if len(data)%2 == 1:
  median = data[int((len(data)+1)/2)-1]
else:
  m1 = data[int(len(data)/2)]
  m2 = data[int((len(data)/2)-1)]
  median = (m1+m2)/2
print("median =",median)
#IQR
if len(data)%4==0:
  Q1 = data[int((len(data)/4)-1)]
else:
  Q1U = data[int(math.ceil(len(data)/4))-1]
  Q1L = data[int(math.floor(len(data)/4))-1]
  Q1 = (Q1U+Q1L)/2
if len(data)%4==0:
  Q3 = data[int((len(data)*3/4)-1)]
else:
  Q3U = data[int(math.ceil(len(data)*3/4))-1]
  Q3L = data[int(math.floor(len(data)*3/4))-1]
  Q3 = (Q3U+Q3L)/2
IQR = Q3-Q1
print("IQR =",IQR)
#Skewness
skew =  3*(mean-median)/σ
print("skew =",skew)
