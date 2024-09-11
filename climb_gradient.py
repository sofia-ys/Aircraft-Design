import math as ma
import aircraft_data as ad


# create a function to calculate all flight gradient requirements
def calcClimbGradientGeneral(wing_loading, cl_req, cd_0, oswald, c_v, beta, thrust_fraq, T, P, rho):
    V = []
    M = []
    theta_t = []
    delta_t = []
    alpha_t = []
    B = ad.bypass
    climb_gradient = []
    for i in wing_loading:
        V.append(ma.sqrt((2 * i) / (rho * cl_req / 1.1)))

    for i in V:
        M.append(i / (ma.sqrt(1.4 * 287 * T)))

    for i in M:
        theta_t.append((T * (1 + 0.2 * i ** 2)) / ad.T_sl)

    for i in M:
        delta_t.append((P * pow((1 + 0.2 * pow(i, 2)), (1.4 / 0.4))) / ad.P_sl)

    for i in range(len(wing_loading)):
        if theta_t[i] < ad.theta_t_break:
            alpha_t.append(delta_t[i] * (1 - (0.43 + 0.014 * B) * ma.sqrt(M[i])))
        else:
            alpha_t.append(delta_t[i] * (1 - (0.43 + 0.014 * B) * ma.sqrt(M[i])
                                         - (3 * (theta_t[i] - ad.theta_t_break)) / (1.5 + M[i])))

    for i in alpha_t:
        climb_gradient.append(thrust_fraq * (beta / i) * (c_v + 2 * ma.sqrt(
            cd_0 / (ma.pi * ad.AR * oswald))))  # 0.011 shall be replaced with cd_0 and 0.8 with e (oswald)!!

    return climb_gradient


# functions to calculate the climb gradient for a particular CS-25 requirement with adjusted cd0 and oswald
def calcGradient119(wing_loading):
    # 35 is the flap deflection
    beta = 1
    c_v = 0.032 # c_v specified in cs25.119 req
    thrust_fraq = 1
    cd0_adj = ad.c_d0 + 35 * 0.0013 + 0.0175
    osw_adj = ad.oswald + 0.0026 * 35
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_landing, cd0_adj, osw_adj, c_v, beta, thrust_fraq, ad.T_landing, ad.P_landing, ad.rho_landing)  # np.linspace(100, 9000, num=90)
    return T_W


def calcGradient121a(wing_loading):
    # 15 is the flap deflection
    beta = 1
    c_v = 0
    thrust_fraq = ad.Ne / (ad.Ne - 1)
    cd0_adj = ad.c_d0 + 15 * 0.0013 + 0.0175
    osw_adj = ad.oswald + 0.0026 * 15
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_take_off, cd0_adj, osw_adj, c_v, beta, thrust_fraq, ad.T_take_off, ad.P_take_off, ad.rho_take_off)
    return T_W


def calcGradient121b(wing_loading):
    c_v = 0.024
    beta = 1
    thrust_fraq = ad.Ne / (ad.Ne - 1)
    cd0_adj = ad.c_d0 + 15 * 0.0013
    osw_adj = ad.oswald + 0.0026 * 15
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_take_off, cd0_adj, osw_adj, c_v, beta, thrust_fraq, ad.T_take_off, ad.P_take_off, ad.rho_take_off)
    return T_W


def calcGradient121c(wing_loading):
    c_v = 0.012
    beta = 1
    thrust_fraq = ad.Ne / (ad.Ne - 1)
    cd0_adj = ad.c_d0
    osw_adj = ad.oswald
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_cruise, cd0_adj, osw_adj, c_v, beta, thrust_fraq, ad.T_take_off, ad.P_take_off, ad.rho_take_off)
    return T_W


def calcGradient121d(wing_loading):
    c_v = 0.021
    beta = ad.m_fraq_landing
    thrust_fraq = ad.Ne / (ad.Ne - 1)
    cd0_adj = ad.c_d0 + 35 * 0.0013
    osw_adj = ad.oswald + 0.0026 * 35
    T_W = calcClimbGradientGeneral(wing_loading, ad.cl_landing, cd0_adj, osw_adj, c_v, beta, thrust_fraq, ad.T_landing, ad.P_landing, ad.rho_landing)
    return T_W
