from math import sqrt, pow, pi
import aircraft_data as ad

def lapse_rate(wing_loading, cl_req, T, P, rho):
    V = []
    M = []
    theta_t = []
    delta_t = []
    alpha_t = []
    B = ad.bypass
    for i in wing_loading:
        V.append(sqrt((2 * i) / (rho * cl_req / 1.1)))

    for i in V:
        M.append(i / (sqrt(1.4 * 287 * T)))

    for i in M:
        theta_t.append((T * (1 + 0.2 * i ** 2)) / ad.T_sl)

    for i in M:
        delta_t.append((P * pow((1 + 0.2 * pow(i, 2)), (1.4 / 0.4))) / ad.P_sl)

    for i in range(len(wing_loading)):
        if theta_t[i] < ad.theta_t_break:
            alpha_t.append(delta_t[i] * (1 - (0.43 + 0.014 * B) * sqrt(M[i])))
        else:
            alpha_t.append(delta_t[i] * (1 - (0.43 + 0.014 * B) * sqrt(M[i])
                                         - (3 * (theta_t[i] - ad.theta_t_break)) / (1.5 + M[i])))
    return alpha_t

def take_off_field_length(wing_loading):
    t_w = []
    h2 = 11 # obstacle height req for cs25
    k_t = 0.85 # parameter that relates the thrust to V_2 assumed to be 0.85 for jet aircrafts
    cl_2 = ad.cl_take_off * (1 / 1.13) ** 2
    alpha_t = lapse_rate(wing_loading, cl_2, ad.T_lfl_hot, ad.P_lfl, ad.rho_lfl_hot)

    for i in range(len(wing_loading)):
        t_w.append(1.15 * alpha_t[i] *
                   sqrt(2 * wing_loading[i] / ad.dist_take_off / k_t / ad.rho_lfl_hot / ad.g / pi / ad.AR / ad.oswald)
                   + 2 * 4 * h2 / ad.dist_take_off)
    return t_w
