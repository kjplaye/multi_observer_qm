import pylab
from byd import *

X = np.array([
    [1,0],
    [0,1],
    [0.3,0.5]])
B = np.array([
    [0,0,0],
    [0,0,1],
    [0,1,0],
    [0,1,1],
    [1,0,0],
    [1,0,1],
    [1,1,0],
    [1,1,1]])

def draw_cube():
    fig = pylab.figure()
    ax = fig.add_subplot()
    BX = np.dot(B,X)
    for i in range(4):
        pylab.plot([BX[i,0],BX[i+4,0]],[BX[i,1],BX[i+4,1]],color = 'green', linewidth=3)
        i2 = [0,1,4,5][i]
        pylab.plot([BX[i2,0],BX[i2+2,0]],[BX[i2,1],BX[i2+2,1]],color = 'red', linewidth=3)
        i3 = 2*i
        pylab.plot([BX[i3,0],BX[i3+1,0]],[BX[i3,1],BX[i3+1,1]],color = 'blue', linewidth=3)
    for i in range(8):
        label = ''.join([['H','T'][e] for e in B[i]])
        pylab.text(BX[i,0] + 0.1, BX[i,1] + 0.09,f'{label} ({i})', size = 20)
    pylab.scatter(BX[:,0],BX[:,1],s = 250, color = 'black')
    pylab.grid(False)
    pylab.axis('off')
    for i in [4,7]:
        circ = pylab.Circle((BX[i,0],BX[i,1]),0.15,fill = False, color = 'yellow', linewidth = 10)
        ax.add_patch(circ)
    ax.axis('equal')
    
