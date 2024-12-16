from matplotlib import pyplot as plt

def tensile_stress(Mx,Ixx, Izz, Ixz, z):
    sigma = (Mx * Izz * z - Mx * Ixz * z)/ (Ixx * Izz - Ixz ** 2)

    return sigma

def saftey_margin(omega_yield, sigma_max):
    return sigma_max / omega_yield


plt.plot(saftey_margin)
plt.show()