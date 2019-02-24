import matplotlib.pyplot as plt

#Define Some Constants
T=1/512
N=30
f=open("Data2.txt","r")

#0) taking input from Data1.txt
input = f.read()       #read input
lines = list()         #empty list
diff=list()            #empty list
square=list()          #empty list
smooth=list()          #empty list
autocorrelation=list() #empty list
lines_int = input.split()
for k in lines_int:
    lines.append(float(k))

print(lines)

#1) perform diff equation
for i in range(2,len(lines)-2):
    diff.append(1/(8*T)*((-1*lines[i-2])+(-2*lines[i-1])+(2*lines[i+1])+(1*lines[i+2])))
print("diff =" , diff)

#2) perform square equation
for i in range(0,len(diff)):
    square.append(diff[i]*diff[i])
print("square =" , square)
print()

#3) perform smoooth equation

for i in range(1,4000):
    sum = 0
    if(i<30):
        k=0
    else:
        k=i-30
    for j in range(k,i):
        #print(i,count)
        sum += square[j]
    smooth.append(1/N*sum)
print("smooth =" , smooth)
print(len(smooth))



#4) copmpute autocorrelation
for m in range(0,800):
    sum = 0
    for j in range(0,2000):
        sum += smooth[j]*smooth[j+m]

    autocorrelation.append(sum)

print("autocorrelation =",autocorrelation)
# plot all
#plt.plot(lines)
#plt.show()
#plt.plot(diff)
#plt.show()
#plt.plot(square)
#plt.show()
#plt.plot(smooth)
#plt.show()
plt.plot(autocorrelation)
plt.show()


# measure i can suggest
second_Max = 0

for i in range(50,600):
    if(second_Max < autocorrelation[i]):
        second_Max = autocorrelation[i]
        Required_Lag = i

#print(Required_Lag)
Heart_Rate = 60 / (Required_Lag / 512)
print("Heart_Rate = ",Heart_Rate,"bpm")

AF_measure = Heart_Rate -100
print("AF_measure = ",AF_measure)kj