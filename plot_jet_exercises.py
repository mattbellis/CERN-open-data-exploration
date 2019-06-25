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

plt.figure(figsize=(8,5))
plt.hist(jet_pt,bins=100,range=(0,500))
plt.xlabel(r'Jet $p_T$ [GeV/c]', fontsize=18)
plt.yscale('log')
plt.tight_layout()
plt.savefig('jetpT.png')

plt.figure(figsize=(8,5))
plt.hist(jet_eta,bins=100)
plt.xlabel(r'Jet $\eta$', fontsize=18)
plt.tight_layout()
plt.savefig('jeteta.png')

plt.figure(figsize=(8,5))
plt.hist(jet_phi,bins=100)
plt.xlabel(r'Jet $\phi$', fontsize=18)
plt.tight_layout()
plt.savefig('jetphi.png')

plt.show()


'''

for i in range(nentries):

    jet_pt = data[b'jet_pt'][i]

    print(jet_pt)



print(len(data[b'jet_pt']))
print(len(data[b'jet_eta']))

'''
