''' constants for the final wing box design '''
# material properties
E = 72.4 * 10**9 # young's modulus [Pa]
poisson = 0.33  # poisson's ratio 

k_s1 = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35]  # buckling coefficient for rectangular plate under shear, starting at a/b = 1 and 0.1 increments
b = 35.48
taper = 0.246  # taper ratio [-]
# wing box characteristics ALL VALUES FOR ROOT POSITION ONLY
d_1 = 0.609118 #Place Holder value Length of front spar
d_2 = 2.582268 #Place holder value for Distance between front and back spar
d_3 = 0.487393 # Place Holder value for length of back spar
d_4 = 1.2 # Place Holder  value for distrance between front spar amd multibox spar
t_1 = 0.005 # Place Holder  value for thickness of spars
t_2 = 0.005 # Place Holder value for thickness of wing box skin (top and bottom)


#Design 1
k_s1 = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35, 10.2, 10.1, 10, 9.9, 9.85, 9.8, 9.78,  9.76, 9.74, 9.73, 9.7, 9.68, 9.64, 9.62, 9.6, 9.58, 9.56, 9.54, 9.54, 9.54, 9.52, 9.52, 9.52, 9.52, 9.52, 9.52, 9.53, 9.53, 9.53, 9.53, ]  # buckling coefficient for rectangular plate under shear, starting at a/b = 1 and 0.1 increments
span_t1_1 = [0, 3.5, 7]
t1_1 = [0.007, 0.006, 0.005]
span_t2_1 = [0, 3.5, 7]
t2_1 = [0.007, 0.006, 0.005]

#Design 2
k_s2 = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35, 10.2, 10.1, 10, 9.9, 9.85, 9.8, 9.78,  9.76, 9.74, 9.73, 9.7, 9.68, 9.64, 9.62, 9.6, 9.58, 9.56, 9.54, 9.54, 9.54, 9.52, 9.52, 9.52, 9.52, 9.52, 9.52, 9.53, 9.53, 9.53, 9.53, ] # buckling coefficient for rectangular plate under shear, starting at a/b = 1 and 0.1 increments
span_t1_2 = [0, 21, 25, 30, 36]
t1_2 = [0.005, 0.005, 0.005, 0.005, 0.005]
span_t2_2 = [0, 21, 25, 30, 36]
t2_2 = [18, 21, 25, 30, 36]

#Design 3
k_s3 = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35, 10.2, 10.1, 10, 9.9, 9.85, 9.8, 9.78,  9.76, 9.74, 9.73, 9.7, 9.68, 9.64, 9.62, 9.6, 9.58, 9.56, 9.54, 9.54, 9.54, 9.52, 9.52, 9.52, 9.52, 9.52, 9.52, 9.53, 9.53, 9.53, 9.53, ] # buckling coefficient for rectangular plate under shear, starting at a/b = 1 and 0.1 increments
span_t1_3 = [0, 21, 25, 30, 36]
t1_3 = [0.005, 0.005, 0.005, 0.005, 0.005]
span_t2_3 = [0, 21, 25, 30, 36]
t2_3 = [18, 21, 25, 30, 36]