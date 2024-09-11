import numpy as np
import aircraft_data as ad


#Variables
Pressure_SLISA = ad.P_sl #Pa
Temperature_SLISA = ad.T_sl #Kelvin
height_climbrate = 3658 #meters, comes from average of reference ac
gamma_climbrate = 1.4 #Constant value
Temperature_climbrate = 264.3730 #Kelvin
Pressure_climbrate = 64432.1289 #Pascal
Density_climbrate = 0.8492 #kg/m^3
Massfraction_climbrate = 0.95 #placeholder
Climbrate_climbrate = 4 #placeholder
Cd0_climbrate = ad.c_d0
AR_climbrate = ad.AR
Oswald_climbrate = ad.oswald
Cl_climbrate = np.sqrt(Cd0_climbrate * np.pi * AR_climbrate * Oswald_climbrate)
Bypass_climbrate = ad.bypass
thetabrk_climbrate = ad.theta_t_break

print((ad.T_cruise*(1+0.2*ad.M **2))/ad.T_sl)
#def clim_rate(wing_loading):
  #  alpha_t = ((ad.P_cruise * (1 + 0.2 * ad.M) ** (1.4/0.4)) / ad.P_sl) * (1 - )



def climb_rate(wingloading_climbrate):
    velocity_climbrate = np.array(np.sqrt(wingloading_climbrate * (2/Cl_climbrate)*(1/Density_climbrate))) #Tabulate velocity

    Mach_climbrate = np.array(velocity_climbrate/(np.sqrt(gamma_climbrate * Temperature_climbrate * 287)))

    Totaltemp_climbrate = np.array(Temperature_climbrate * (1 + ((gamma_climbrate-1)/2) * (Mach_climbrate ** 2)))

    Totalpressure_climbrate = np.array(Pressure_climbrate * ((1 + ((gamma_climbrate-1)/2) * ((Mach_climbrate) ** 2)) ** (gamma_climbrate)/(gamma_climbrate-1)))

    Delta_climbrate = np.array(Totalpressure_climbrate / Pressure_SLISA)

    Theta_climbrate = np.array(Totaltemp_climbrate / Temperature_SLISA) # ASK WHAT THIS IS USED FOR!!!

    alphat_climbrate = np.array(Delta_climbrate * (1 - (0.43 + 0.014 * Bypass_climbrate) * np.sqrt(Mach_climbrate)))

    Thrustw_climbrate = np.array((Massfraction_climbrate/(alphat_climbrate)) *
                                 (np.sqrt((Climbrate_climbrate * Climbrate_climbrate * Delta_climbrate * Cl_climbrate)
                                          / (Massfraction_climbrate * 2 * wingloading_climbrate))
                                  + 2 * np.sqrt((Cd0_climbrate) / (np.pi * AR_climbrate * Oswald_climbrate))))
    return Thrustw_climbrate
