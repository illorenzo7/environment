import numpy as np
import matplotlib.pyplot as plt
import sys, os
sys.path.append(os.environ['rapp'])
sys.path.append(os.environ['raco'])
sys.path.append(os.environ['raco'] + '/quantities_util')
sys.path.append(os.environ['rapl'])
sys.path.append(os.environ['rapl'] + '/azav')
sys.path.append(os.environ['rapl'] + '/slice')
sys.path.append(os.environ['rapl'] + '/timetrace')
from rayleigh_diagnostics import *
import rayleigh_diagnostics_alt as rdalt
from common import *
from numbers_util import *
from plotcommon import *
from azav_util import plot_azav
from slice_util import plot_moll_or_ortho
from timey_util import plot_timey
from reference_tools import equation_coefficients

def imshow(arr):
    sig = np.std(arr)
    plt.imshow(arr, vmin=-3*sig, vmax=3*sig, cmap='RdYlBu_r')
    plt.colorbar()
    plt.show()

def plot(x, y, x0=None):
    ymin, ymax = np.min(y), np.max(y)
    yvals = np.linspace(ymin,  ymax, 100)
    plt.plot(x, y)
    if not x0 is None:
        plt.plot(x0*np.ones(100), yvals, 'k--')
    plt.show()
