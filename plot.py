from cProfile import label
from time import ctime
from turtle import color
from click import style
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

with open(loadPath + 'cTimes22L1.pkl', 'rb') as f:
    cTimes22L1 = pickle.load(f)

with open(loadPath + 'cTimes22L2.pkl', 'rb') as f:
    cTimes22L2 = pickle.load(f)

with open(loadPath + 'cTimes3.pkl', 'rb') as f:
    cTimes3 = pickle.load(f)

with open(loadPath + 'cTimes3L1.pkl', 'rb') as f:
    cTimes3L1 = pickle.load(f)
with open(loadPath + 'cTimes3L2.pkl', 'rb') as f:
    cTimes3L2 = pickle.load(f)

cTimes1L2 = [int(i) for i in cTimes1L2]
cTimes2L2 = [int(i) for i in cTimes2L2]
cTimes22L2 = [int(i) for i in cTimes22L2]
for k in cTimes3L2:
    cTimes3L2[k] = [int(i) for i in cTimes3L2[k]]

# # -------------------------- Exercise 1/2 ------------------------------
# plotAndSave(sizes, [javaTimes1, cTimes1],
#             ['Java', 'C++'], 'Exercise 1', savePath+'ex1.png')

# plotAndSave(sizes, [javaTimes2, cTimes2],
#             ['Java', 'C++'], 'Exercise 2', savePath+'ex2.png')

# plotAndSave(sizes, [javaTimes1, javaTimes2],
#             ['Normal Mult', 'Line Mult'], 'Normal Multiplication vs Line Multiplication (Java)', savePath+'java_comparison.png')

# plotAndSave(sizes, [cTimes1, cTimes2],
#             ['Normal Mult', 'Line Mult'], 'Normal Multiplication vs Line Multiplication (C++)', savePath+'c_comparison.png')

# # -------------------------- Exercise 2.2/3 ----------------------------

# plotAndSave(sizes2, cTimes3.values(),
#             ["Block Size="+str(b) for b in cTimes3.keys()], 'Block Multiplication (C++)', savePath+'ex3.png')

# plotAndSave(sizes2, [cTimes22] + list(cTimes3.values()),
#             ['Line Mult'] + ["Block Mult (b="+str(b)+")" for b in cTimes3.keys()], 'Block Multiplication vs Line Multiplication (C++)', savePath+'ex3And2_2.png')

# -------------------------- L1/L2 Cache Misses Comparisons ----------------------------


def bar2PlotAndSave(xticks, yss, legend, title, saveName):
    # create data
    # Represents bar plot x axis (does not match the points x)
    x = np.arange(len(xticks))
    w = 0.4

    # # plot data in grouped manner of bar type
    plt.bar(x-w/2, yss[0], w)
    plt.bar(x+w/2, yss[1], w)

    plt.xticks(x, xticks)
    plt.xlabel("Array Size")
    plt.ylabel("Cache Misses")
    plt.legend(legend)
    plt.title(title)
    plt.savefig(saveName)
    plt.show()
    plt.clf()


bar2PlotAndSave(sizes, [cTimes1L1, cTimes2L1], ["Normal Mult", "Line Mult"],
                "L1 Cache Misses (Normal vs Line Multiplication)", savePath+"ex1And2L1.png")

bar2PlotAndSave(sizes, [cTimes1L2, cTimes2L2], ["Normal Mult", "Line Mult"],
                "L2 Cache Misses (Normal vs Line Multiplication)", savePath+"ex1And2L2.png")


def bar4PlotAndSave(xticks, yss, legend, title, saveName):
    # create data
    # Represents bar plot x axis (does not match the points x)
    x = np.arange(len(xticks))
    w = 0.2

    # # plot data in grouped manner of bar type
    plt.bar(x-w-w/2, yss[0], w)
    plt.bar(x-w/2, yss[1], w)
    plt.bar(x+w/2, yss[2], w)
    plt.bar(x+w+w/2, yss[3], w)

    plt.xticks(x, xticks)

    plt.xlabel("Array Size")
    plt.ylabel("Cache Misses")
    plt.legend(legend)
    plt.title(title)
    plt.savefig(saveName)
    plt.show()
    plt.clf()


bar4PlotAndSave(sizes2, [cTimes22L1, cTimes3L1[128], cTimes3L1[256], cTimes3L1[512]], ["Line Mult", "Block=128 Mult",
                "Block=256 Mult", "Block=512 Mult"], "L1 Cache Misses (Line vs Block Multiplication)", savePath+"ex22And3L1.png")

bar4PlotAndSave(sizes2, [cTimes22L2, cTimes3L2[128], cTimes3L2[256], cTimes3L2[512]], ["Line Mult", "Block=128 Mult",
                "Block=256 Mult", "Block=512 Mult"], "L2 Cache Misses (Line vs Block Multiplication)", savePath+"ex22And3L2.png")
