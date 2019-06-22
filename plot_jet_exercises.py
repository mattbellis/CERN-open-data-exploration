import numpy as np
import matplotlib.pylab as plt
import uproot as up

import sys

infilename = sys.argv[1]

f = up.open(infilename)

print(f['ak5ak7']['OpenDataTree'].keys())
tree = f['ak5ak7']['OpenDataTree']

data = tree.arrays(tree.keys())

print("here")
print(data.keys())

nentries = len(data[b'jet_pt'])

print(nentries)

tree.show()

jet_pt = tree.array('jet_pt').flatten()
jet_eta = tree.array('jet_eta').flatten()
jet_phi = tree.array('jet_phi').flatten()

print(jet_pt)

plt.figure()
plt.hist(jet_pt,bins=100,range=(0,500))

plt.figure()
plt.hist(jet_eta,bins=100)

plt.figure()
plt.hist(jet_phi,bins=100)

plt.show()


'''

for i in range(nentries):

    jet_pt = data[b'jet_pt'][i]

    print(jet_pt)



print(len(data[b'jet_pt']))
print(len(data[b'jet_eta']))

'''
