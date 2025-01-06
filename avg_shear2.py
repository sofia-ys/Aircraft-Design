import sys
sys.path.append('Wing Structure')
sys.path.append('Wing_Box_Detailed')
import shear_bending_flight as sbf
import wing_box_constants as wb
import shear_buckling as sb
import numpy as np
import matplotlib.pyplot as plt
import Ixx

x = sb.getSparHeight

def tau_avg(id, y_value)