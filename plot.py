from turtle import color
import numpy as np
import matplotlib.pyplot as plt
import pickle

# # Matrix sizes used
# sizes = []  # x axis for ex 1 and 2
# sizes2 = []  # x axis for ex 2.2 and 3
# # Exercise 1 results
# cTimes1 = []
# javaTimes1 = []
# # Exercise 2 results
# cTimes2 = []
# javaTimes2 = []
# # Exercise 2.2 results
# cTimes22 = []
# # Exercise 3 (Dictionary that holds results from diferent block sizes)
# cTimes3 = {}  # Has block sizes as keys and data as values

# start = 100
# end = 400+1
# step = 50

# for i in range(start, end, step):
#     sizes.append(int(i))

# # -------------------------- Exercise 1 --------------------------------
# for i in range(start, end, step):
#     input = "1 " + str(i)
#     java_child_process = subprocess.run(
#         ['java', 'Matrix'], stdout=subprocess.PIPE, input=input.encode())
#     c_child_process = subprocess.run(
#         ['./matrix'], stdout=subprocess.PIPE, input=(input+" 0").encode())

#     javaTimes1.append(float(java_child_process.stdout.decode(
#         'UTF-8').split("\n")[3].split(" ")[-2]))
#     cTimes1.append(float(c_child_process.stdout.decode(
#         'UTF-8').split("\n")[4].split(" ")[5]))
# # ----------------------------------------------------------------------

# # -------------------------- Exercise 2 --------------------------------
# for i in range(start, end, step):
#     input = "2 " + str(i)
#     java_child_process = subprocess.run(
#         ['java', 'Matrix'], stdout=subprocess.PIPE, input=input.encode())
#     c_child_process = subprocess.run(
#         ['./matrix'], stdout=subprocess.PIPE, input=(input+" 0").encode())

#     javaTimes2.append(float(java_child_process.stdout.decode(
#         'UTF-8').split("\n")[3].split(" ")[-2]))
#     cTimes2.append(float(c_child_process.stdout.decode(
#         'UTF-8').split("\n")[4].split(" ")[5]))
# # ----------------------------------------------------------------------

# # Exercise 2.2 and 3 user diferent ranges for the matrix size
# start = 200
# end = 600+1
# step = 50
# for i in range(start, end, step):
#     sizes2.append(int(i))

# # -------------------------- Exercise 2.2 --------------------------------
# for i in range(start, end, step):
#     input = "2 " + str(i)
#     c_child_process = subprocess.run(
#         ['./matrix'], stdout=subprocess.PIPE, input=(input+" 0").encode())

#     cTimes22.append(float(c_child_process.stdout.decode(
#         'UTF-8').split("\n")[4].split(" ")[5]))
# # ----------------------------------------------------------------------

# # -------------------------- Exercise 3 --------------------------------
# # Defining what block size to use
# bStart = b = 25
# bEnd = 50
# while b <= bEnd:
#     cTimes3[b] = []
#     b = b*2
# b = bStart

# while b <= bEnd:
#     for i in range(start, end, step):
#         input = "3 " + str(i) + " " + str(b)
#         c_child_process = subprocess.run(
#             ['./matrix'], stdout=subprocess.PIPE, input=(input+" 0").encode())
#         cTimes3[b].append(float(c_child_process.stdout.decode(
#             'UTF-8').split("\n")[4].split(" ")[7]))
#     b = b*2
# # ----------------------------------------------------------------------


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

with open(loadPath + 'sizes.pkl', 'rb') as f:
    sizes = pickle.load(f)

with open(loadPath + 'cTimes1.pkl', 'rb') as f:
    cTimes1 = pickle.load(f)

with open(loadPath + 'javaTimes1.pkl', 'rb') as f:
    javaTimes1 = pickle.load(f)

with open(loadPath + 'cTimes2.pkl', 'rb') as f:
    cTimes2 = pickle.load(f)

with open(loadPath + 'javaTimes2.pkl', 'rb') as f:
    javaTimes2 = pickle.load(f)

with open(loadPath + 'sizes2.pkl', 'rb') as f:
    sizes2 = pickle.load(f)

# with open(loadPath + 'cTimes22.pkl', 'rb') as f:
#     cTimes22 = pickle.load(f)

# with open(loadPath + 'cTimes3.pkl', 'rb') as f:
#     cTimes3 = pickle.load(f)

print(sizes)
print(sizes2)
print(cTimes1)
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
# plotAndSave(sizes2, cTimes3.values(),
#             ["Block Size="+str(b) for b in cTimes3.keys()], 'Block Multiplication (C++)', savePath+'ex3.png')

# plotAndSave(sizes2, [cTimes22] + list(cTimes3.values()),
#             ['Line Mult'] + ["Block Mult (b="+str(b)+")" for b in cTimes3.keys()], 'Block Multiplication vs Line Multiplication (C++)', savePath+'ex3And2_2.png')
