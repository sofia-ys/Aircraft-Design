import math as ma
import aircraft_data as ad


# create a function to calculate all flight gradient requirements
def calcClimbGradientGeneral(wing_loading, cl_req, cd_0, oswald):
    V = []
    M = []
    theta_t = []
    delta_t = []
    alpha_t = []
    c_v = 0.032
    B = ad.bypass
    climb_gradient = []
    for i in wing_loading:
        V.append(ma.sqrt((2 * i) / (1.225 * cl_req / 1.1)))

    for i in V:
        M.append(i / (
            ma.sqrt(1.4 * 287 * 288.15)))  # using sea level values, since all the flight gradient requirements use it

    for i in M:
        theta_t.append((ad.T_sl * (1 + 0.2 * i ** 2)) / ad.T_sl)

    for i in M:
        delta_t.append((ad.P_sl * pow((1 + 0.2 * pow(i, 2)), (1.4 / 0.4))) / ad.P_sl)

    for i in range(90):
        alpha_t.append(delta_t[i] * (1 - (0.43 + 0.014 * B) * ma.sqrt(M[i])))

    for i in alpha_t:
        climb_gradient.append((1 / i) * (c_v + 2 * ma.sqrt(
            cd_0 / (ma.pi * ad.AR * oswald))))  # 0.011 shall be replaced with cd_0 and 0.8 with e (oswald)!!

    return climb_gradient


# functions to calculate the climb gradient for a particular CS-25 requirement with adjusted cd0 and oswald
def calcGradient119(wing_loading):
    # 35 is the flap deflection
    cd0_adj = ad.c_d0 + 35 * 0.0013 + 0.02
    osw_adj = ad.oswald - 0.0026 * 35
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_landing, cd0_adj, osw_adj)  # np.linspace(100, 9000, num=90)
    return T_W


def calcGradient121a(wing_loading):
    # 15 is the flap deflection
    cd0_adj = ad.c_d0 + 15 * 0.0013 + 0.02
    osw_adj = ad.oswald - 0.0026 * 15
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_take_off, cd0_adj, osw_adj)
    return T_W


def calcGradient121b(wing_loading):
    cd0_adj = ad.c_d0 + 15 * 0.0013
    osw_adj = ad.oswald - 0.0026 * 15
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_take_off, cd0_adj, osw_adj)
    return T_W


def calcGradient121c(wing_loading):
    cd0_adj = ad.c_d0
    osw_adj = ad.oswald
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_cruise, cd0_adj, osw_adj)
    return T_W


def calcGradient121d(wing_loading):
    cd0_adj = ad.c_d0 + 35 * 0.0013
    osw_adj = ad.oswald - 0.0026 * 35
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_landing, cd0_adj, osw_adj)
    return T_W
