from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import pickle

def plotAndSave(x, ys, legend, title, saveName):
    # Plot graph
    for y in ys:
        plt.plot(x, y)

    # Highlighting Points
    for y in ys:
        plt.plot(x, y, '.')

    # naming the x axis
    plt.xlabel('Matrix Size')
    # naming the y axis
    plt.ylabel('Real Time Passed (in seconds)')

    plt.grid()
    plt.title(title)
    plt.legend(legend)
    # function to show the plot
    plt.savefig(saveName)
    plt.clf()

loadPath = "./pickle/"
savePath = "./graphs/"

# Loading List of sizes used
with open(loadPath + 'sizes.pkl', 'rb') as f:
    sizes = pickle.load(f)

# Normal Multiplication Results (C++)
with open(loadPath + 'cTimes1.pkl', 'rb') as f:
    cTimes1 = pickle.load(f)

# Normal Multiplication Misses (C++)
with open(loadPath + 'cTimes1L1.pkl', 'rb') as f:
    cTimes1L1 = pickle.load(f)
with open(loadPath + 'cTimes1L2.pkl', 'rb') as f:
    cTimes1L2 = pickle.load(f)

# Normal Multiplication Results (Java)
with open(loadPath + 'javaTimes1.pkl', 'rb') as f:
    javaTimes1 = pickle.load(f)

# Line Multiplication Results (C++)
with open(loadPath + 'cTimes2.pkl', 'rb') as f:
    cTimes2 = pickle.load(f)

with open(loadPath + 'cTimes2L1.pkl', 'rb') as f:
    cTimes2L1 = pickle.load(f)
with open(loadPath + 'cTimes2L2.pkl', 'rb') as f:
    cTimes2L2 = pickle.load(f)

with open(loadPath + 'javaTimes2.pkl', 'rb') as f:
    javaTimes2 = pickle.load(f)

with open(loadPath + 'sizes2.pkl', 'rb') as f:
    sizes2 = pickle.load(f)

with open(loadPath + 'cTimes22.pkl', 'rb') as f:
    cTimes22 = pickle.load(f)

with open(loadPath + 'cTimes3.pkl', 'rb') as f:
    cTimes3 = pickle.load(f)

with open(loadPath + 'cTimes3L1.pkl', 'rb') as f:
    cTimes3L1 = pickle.load(f)
with open(loadPath + 'cTimes3L2.pkl', 'rb') as f:
    cTimes3L2 = pickle.load(f)

print(sizes)
print(sizes2)
print(cTimes1)
print(cTimes1L1)
print(cTimes1L2)
# print(cTimes3)

# -------------------------- Exercise 1/2 ------------------------------
plotAndSave(sizes, [cTimes1, javaTimes1],
            ['Java', 'C++'], 'Exercise 1', savePath+'ex1.png')

plotAndSave(sizes, [cTimes2, javaTimes2],
            ['Java', 'C++'], 'Exercise 2', savePath+'ex2.png')

plotAndSave(sizes, [javaTimes1, javaTimes2],
            ['Normal Mult', 'Line Mult'], 'Normal Multiplication vs Line Multiplication (Java)', savePath+'java_comparison.png')

plotAndSave(sizes, [cTimes1, cTimes2],
            ['Normal Mult', 'Line Mult'], 'Normal Multiplication vs Line Multiplication (C++)', savePath+'c_comparison.png')

# -------------------------- Exercise 2.2/3 ----------------------------
plotAndSave(sizes2, cTimes3.values(),
            ["Block Size="+str(b) for b in cTimes3.keys()], 'Block Multiplication (C++)', savePath+'ex3.png')

plotAndSave(sizes2, [cTimes22] + list(cTimes3.values()),
            ['Line Mult'] + ["Block Mult (b="+str(b)+")" for b in cTimes3.keys()], 'Block Multiplication vs Line Multiplication (C++)', savePath+'ex3And2_2.png')
