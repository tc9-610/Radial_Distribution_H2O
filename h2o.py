'''
import math

d = math.radians(104.45)

for i in range (0, 25, 2):
    for j in range (0, 25, 2):
        for k in range (0, 25, 2):
            print ('O', i, j, k)
            print ('H', i + 0.94, j, k)
            print ('H', round(i + 0.95 * math.cos(d)), round(j + 0.95 * math.sin(d)), k)
'''


import numpy as np
import matplotlib.pyplot as plt

l_spl = []

with open('solv.gro') as F:
 
   for line in F:
        stp = line.strip()
        spl = stp.split()
        l_spl.append(spl)


box = [float(x) for x in l_spl[-1]]
box_size = box[1]
l_spl.pop(0)
l_spl.pop(0)
l_spl.pop()
num_particles = len(l_spl)
vol = box_size ** 3
density = num_particles / vol

ox = []
hy = []
for i in l_spl:
    if i[1] == 'OW':
        ox.append(i)
    else:
        hy.append(i)

ox_cor = np.array([(i[3:]) for i in ox], dtype=float)
hy_cor = np.array([(j[3:]) for j in hy], dtype=float)
#print(ox_cor)
#diff = np.zeroes(len(ox), len(ox))
dist_oo = []
for i in range(len(ox)):
    for j in range(i+1, len(ox)):
        diff = ((ox_cor[i] - ox_cor[j]) **2)
        distance = np.sqrt(np.sum(diff))
        dist_oo.append(round(distance,2))

numbin = round((box_size/2)/0.02)


hist, bin_edge = np.histogram(dist_oo, bins = numbin, range= (0, box_size/2))
#print(hist, bin_edge)

ideal_p = []
dist = []
for i in bin_edge:
    ideal = 4 * np.pi * (i**2 * 0.02) * density
    dist.append(i)
    ideal_p.append(round(ideal))
dist.pop()
ideal_p.pop()
#print(ideal_p, dist)

g_r = hist/ideal_p
#print(g_r)
#for i in range(len(dist_r)):
#    for j in range(i+1, len(dist_r)):
#       if i == j:
           


#print(p)       

#print (box_size)
#print (diff)
#step = len(dist_r)
#dist = np.arange(0, box_size, (box_size/step))
#plt.plot(dist_r, dist,linewidth = 2.0)


plt.plot(dist, g_r)
plt.xlabel('dist_oo')
plt.ylabel('g(r)')
plt.title('radial')
plt.show()

'''
distance = []
for i in range(len(ox)):
    for j in range(len(ox)):
        diff = ox_cor[i] - ox_cor[j]
        dist = np.sqrt(diff ** 2)
        distance.append(dist)
print (distance)
plt.plot(distance, ox)
plt.show()
'''