import subprocess
from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import pickle

savePath = './pickle/'

# Matrix sizes used
sizes = []  # x axis for ex 1 and 2
sizes2 = []  # x axis for ex 2.2 and 3
# Exercise 1 results
cTimes1 = []
cTimes1Misses = []
javaTimes1 = []
javaTimes1Misses = []
# Exercise 2 results
cTimes2 = []
cTimes2Misses = []
javaTimes2 = []
javaTimes2Misses = []
# Exercise 2.2 results
cTimes22 = []
cTimes22Misses = []
# Exercise 3 (Dictionary that holds results from diferent block sizes)
cTimes3 = {}  # Has block sizes as keys and data as values
cTimes3 = {} 
cTimes3Misses = {} 

# start = 100
# end = 400+1
# step = 50

start = 600
end = 3000+1
step = 400


for i in range(start, end, step):
    sizes.append(int(i))

with open(savePath + 'sizes.pkl', 'wb') as f:
    pickle.dump(sizes, f)
    
print("Started Ex 1")
# -------------------------- Exercise 1 --------------------------------
for i in range(start, end, step):
    input = "1 " + str(i)
    java_child_process = subprocess.run(
        ['java', 'Matrix'], stdout=subprocess.PIPE, input=input.encode())
    c_child_process = subprocess.run(
        ['./matrix'], stdout=subprocess.PIPE, input=(input+" 0").encode())

    javaTimes1.append(float(java_child_process.stdout.decode(
        'UTF-8').split("\n")[3].split(" ")[-2]))
    cTimes1.append(float(c_child_process.stdout.decode(
        'UTF-8').split("\n")[4].split(" ")[5]))
# ----------------------------------------------------------------------
print("Finished Ex 1")
with open(savePath + 'cTimes1.pkl', 'wb') as f:
    pickle.dump(cTimes1, f)

with open(savePath + 'javaTimes1.pkl', 'wb') as f:
    pickle.dump(javaTimes1, f)

print("Started Ex 2")
# -------------------------- Exercise 2 --------------------------------
for i in range(start, end, step):
    input = "2 " + str(i)
    java_child_process = subprocess.run(
        ['java', 'Matrix'], stdout=subprocess.PIPE, input=input.encode())
    c_child_process = subprocess.run(
        ['./matrix'], stdout=subprocess.PIPE, input=(input+" 0").encode())

    javaTimes2.append(float(java_child_process.stdout.decode(
        'UTF-8').split("\n")[3].split(" ")[-2]))
    cTimes2.append(float(c_child_process.stdout.decode(
        'UTF-8').split("\n")[4].split(" ")[5]))
# ----------------------------------------------------------------------
print("Finished Ex 2")

with open(savePath + 'cTimes2.pkl', 'wb') as f:
    pickle.dump(cTimes2, f)

with open(savePath + 'javaTimes2.pkl', 'wb') as f:
    pickle.dump(javaTimes2, f)

# Exercise 2.2 and 3 user diferent ranges for the matrix size
start = 4096
end = 10240+1
step = 2048
for i in range(start, end, step):
    sizes2.append(int(i))

with open(savePath + 'sizes2.pkl', 'wb') as f:
    pickle.dump(sizes2, f)

print("Started Ex 2.2")
# -------------------------- Exercise 2.2 --------------------------------
for i in range(start, end, step):
    input = "2 " + str(i)
    c_child_process = subprocess.run(
        ['./matrix'], stdout=subprocess.PIPE, input=(input+" 0").encode())

    # Traceback (most recent call last): File "calc.py", line 74, in <module> cTimes22.append(float(c_child_process.stdout.decode( IndexError: list index out of range
    cTimes22.append(float(c_child_process.stdout.decode(
        'UTF-8').split("\n")[4].split(" ")[5]))
# ----------------------------------------------------------------------
print("Finished Ex 2.2")

with open(savePath + 'cTimes22.pkl', 'wb') as f:
    pickle.dump(cTimes22, f)

print("Starting Ex 3")
# -------------------------- Exercise 3 --------------------------------
# Defining what block size to use
bStart = b = 128
bEnd = 512
while b <= bEnd:
    cTimes3[b] = []
    b = b*2
b = bStart

while b <= bEnd:
    for i in range(start, end, step):
        if(i%b != 0): # Invalid block size
            with open('log', 'a') as f:
                f.write('Invalid Block Size: i=' + str(i) + ' b=' + str(b)+'\n')
            continue
        print("Start:", i, " Step:", b)  
        input = "3 " + str(i) + " " + str(b)
        c_child_process = subprocess.run(
            ['./matrix'], stdout=subprocess.PIPE, input=(input+" 0").encode())
        cTimes3[b].append(float(c_child_process.stdout.decode(
            'UTF-8').split("\n")[4].split(" ")[7]))
    b = b*2
# ----------------------------------------------------------------------
print("Finished Ex 3")

with open(savePath + 'cTimes3.pkl', 'wb') as f:
    pickle.dump(cTimes3, f)