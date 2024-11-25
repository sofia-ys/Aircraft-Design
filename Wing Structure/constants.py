''' all values taken from WP3 final aircraft parameters'''

# fuselage parameters
L_fus = 36.65  # fuselage length [m]
d_f_outer = 3.722  # outer diameter [m]
d_f_inner = 3.561  # inner diameter [m]
l_cab = 30.42  # cabin length [m]
l_n = 4  # nose length [m]
n_SA = 5  # seats abreast [-]
theta_up = 20  # upwards angle [deg]
theta_nose = 18  # over nose angle [deg]
theta_graz = 25  # grazing angle [deg]

# wing parameters
S_wing = 129.8  # wing area [m^2]
b = 35.48  # wing span [m]
c_root = 5.918  # root chord [m]
c_tip = 1.4521  # tip chord [m]
taper = 0.246  # taper ratio [-]
ar = 9.7  # aspect ratio [-]
sweep_quarter = 30.8  # quarter chord sweep [deg]
dihedral = 5  # dihedral angle [deg]
mac = 3.94  # mean aerodynamic chord (MAC) [m]
y_mac = 7.58  # spanwise position of MAC [m]
x_LEMAC = 17.74  # XLEMAC [m]
v_wing = 37.52  # wing volume [m^3]
sar = 307.8  # specific air range (SAR) [m kg^-1]

# horizontal tail parameters
s_ht = 47.51  # area [m^2]
sweep_ht = 32  # sweep [deg]
AR_ht = 4  # aspect ratio [-]
taper_ht = 0.4  # taper ratio [-]
LE_c4_ht = 32.99  # position of C/4 LE [m]

# vertical tail parameters
s_vt = 33.38  # area [m^2]
sweep_vt = 38  # sweep [deg]
AR_vt = 2.5  # aspect ratio [-]
taper_vt = 0.7  # taper ratio [-]
LE_c4_vt = 32.99  # position of C/4 LE [m]

# high light devices parameters
sweep_hinge = 26.8  # hinge sweep [deg]
S_wf = 12.2  # flapped surface area [m^2]
x_inboard = 0  # inboard edge wrt root chord [m]
x_outboard = 2.39  # outboard edge wrt root chord [m]

# ailerons parameters
b_1 = 7.3  # spanwise position start [m]
b_2 = 9.45  # spanwise position end [m]
c_A = 0.834  # aileron chord length [m]

# engine parameters
T_req = 286.11  # required thrust [kN]
T_max = 311.36  # maximum thrust (both engines) [kN]
epr = 40  # engine pressure ratio 40:1 [-]
bypass = 11  # bypass ratio [-]
m_eng = 3008  # engine mass [kg]

# airfoil parameters
c_l_alpha = 5.17  # lift slope coefficient [rad^-1]
c_l_max = 1.94  # maximum lift coefficient [-]
c_d = 0.0067  # drag coefficient [-]
t_c = 0.11  # thickness to chord ratio [-]

# aerodynamics parameters
C_L_des = 0.384  # design lift coefficient [-]
C_L_max = 1.98  # maximum lift coefficient [-]
C_D_0 = 0.02798  # zero lift drag coefficient [-]
alpha_cruise = 0.01  # design angle of attack [deg]
alpha_stall = 22.3  # stall angle [deg]
M_dd = 0.89  # drag divergence Mach [-]
M_cr = 0.65  # critical Mach [-]

# mission profile parameters
m_p = 13745.5  # payload mass [kg]
range = 10630.5  # design range [km]
mach_cruise = 0.85  # cruise mach number at cruise altitude [-]
V_cruise = 256
density_cruise = 0.44165

# under carriage parameters
theta_scrape = 15  # scrape angle constraint [deg]
N_mw = 4  # number of main wheels [-]
N_nw = 2  # number of nose wheels [-]
D_mw = 49  # main wheel diameter [inch]
W_mw = 17  # main wheel width [inch]
D_nw = 26  # nose wheel diameter [inch]
W_nw = 6.8  # nose wheel width [inch]
l_wh = 14580  # distance from main to front wheel [mm]
l_mw = 4.06  # distance from centre to main wheel [m]

# wing box characteristics ALL VALUES FOR ROOT POSITION ONLY
d_1 = 15 #Place Holder value Length of front spar
d_2 = 15 #Place holder value for Distance between front and back spar
d_3 = 10 # Place Holder value for length of back spar
d_4 = 5 # Place Holder  value for distrance between front spar amd multibox spar
spac = 0.1 # Stringer spacing

#Design 1
d1_span_n1 = [18,21,25,30,36,44,51,59,68]
d1_n1 = [18,21,25,30,36,44,51,59,68] # n1 is the number of stringers on the top skin
d1_span_n2 = [18,21,25,30,36,44,51,59,68]
d1_n2 = [27,33,38,45,55,65,80,100,120] # n2 is the number of stringers on the bottom skin
d1_span_t1 = [18,21,25,30,36,44,51,59,68]
d1_t1 = [18,21,25,30,36,44,51,59,68]
d1_span_t2 = [18,21,25,30,36,44,51,59,68]
d1_t2 = [18,21,25,30,36,44,51,59,68]
d1_span_An = [18,21,25]
d1_An = [1,1,1] # cross sectional area of a stringer

#Design 2
d2_span_n1 = [18,21,25,30,36,44,51,59,68]
d2_n1 = [18,21,25,30,36,44,51,59,68] # n1 is the number of stringers on the top skin
d2_span_n2 = [18,21,25,30,36,44,51,59,68]
d2_n2 = [27,33,38,45,55,65,80,100,120] # n2 is the number of stringers on the bottom skin
d2_span_t1 = [18,21,25,30,36,44,51,59,68]
d2_t1 = [18,21,25,30,36,44,51,59,68]
d2_span_t2 = [18,21,25,30,36,44,51,59,68]
d2_t2 = [18,21,25,30,36,44,51,59,68]
d2_span_An = [18,21,25]
d2_An = [1,1,1] # cross sectional area of a stringer

#Design 3
d3_span_n1 = [18,21,25,30,36,44,51,59,68]
d3_n1 = [18,21,25,30,36,44,51,59,68] # n1 is the number of stringers on the top skin
d3_span_n2 = [18,21,25,30,36,44,51,59,68]
d3_n2 = [27,33,38,45,55,65,80,100,120] # n2 is the number of stringers on the bottom skin
d3_span_t1 = [18,21,25,30,36,44,51,59,68]
d3_t1 = [18,21,25,30,36,44,51,59,68]
d3_span_t2 = [18,21,25,30,36,44,51,59,68]
d3_t2 = [18,21,25,30,36,44,51,59,68]
d3_span_An = [18,21,25]
d3_An = [1,1,1] # cross sectional area of a stringer