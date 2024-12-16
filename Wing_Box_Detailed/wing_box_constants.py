''' constants for the final wing box design '''
# material properties
E = 72.4 * 10**9 # young's modulus [Pa]
poisson = 0.33  # poisson's ratio 

k_s1 = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35]  # buckling coefficient for rectangular plate under shear, starting at a/b = 1 and 0.1 increments
b = 35.48

k_v = 0 #constant for the average shear

# wing box characteristics ALL VALUES FOR ROOT POSITION ONLY
d_1 = 0.609118 #Place Holder value Length of front spar
d_2 = 2.582268 #Place holder value for Distance between front and back spar
d_3 = 0.487393 # Place Holder value for length of back spar
d_4 = 1.2 # Place Holder  value for distrance between front spar amd multibox spar
t_1 = 0.005 # Place Holder  value for thickness of spars
t_2 = 0.005 # Place Holder value for thickness of wing box skin (top and bottom)
ribs = [0, 2, 4, 6, 9, 10, 12, 14, 16, 17.74]

#Design 1
k_s1 = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35, 10.2, 10.1, 10, 9.9, 9.85, 9.8, 9.78,  9.76, 9.74, 9.73, 9.7, 9.68, 9.64, 9.62, 9.6, 9.58, 9.56, 9.54, 9.54, 9.54, 9.52, 9.52, 9.52, 9.52, 9.52, 9.52, 9.53, 9.53, 9.53, 9.53, ]  # buckling coefficient for rectangular plate under shear, starting at a/b = 1 and 0.1 increments
span_t1_1 = [0, 7.5, 12.5]
t1_1 = [0.019, 0.015, 0.01]  # t1 is the thickness of the spar, which is the same for all spars in the design
span_t2_1 = [0, 7.5, 12.5]
t2_1 = [0.016, 0.014, 0.012]  # t2 is the thickness of the skin

#Design 2
k_s2 = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35, 10.2, 10.1, 10, 9.9, 9.85, 9.8, 9.78,  9.76, 9.74, 9.73, 9.7, 9.68, 9.64, 9.62, 9.6, 9.58, 9.56, 9.54, 9.54, 9.54, 9.52, 9.52, 9.52, 9.52, 9.52, 9.52, 9.53, 9.53, 9.53, 9.53, ] # buckling coefficient for rectangular plate under shear, starting at a/b = 1 and 0.1 increments
span_t1_2 = [0, 7, 8, 10.15, 15.5]
t1_2 = [0.005, 0.005, 0.005, 0.005, 0.005]
span_t2_2 = [0, 10, 12, 13, 15.5]
t2_2 = [0.006, 0.006, 0.006, 0.006, 0.006]

#Design 3
k_s3 = [15, 13.6, 12.8, 12.3, 11.9, 11.6, 11.35, 11, 10.8, 10.55, 10.35, 10.2, 10.1, 10, 9.9, 9.85, 9.8, 9.78,  9.76, 9.74, 9.73, 9.7, 9.68, 9.64, 9.62, 9.6, 9.58, 9.56, 9.54, 9.54, 9.54, 9.52, 9.52, 9.52, 9.52, 9.52, 9.52, 9.53, 9.53, 9.53, 9.53, ] # buckling coefficient for rectangular plate under shear, starting at a/b = 1 and 0.1 increments
span_t1_3 = [0, 7, 10]
t1_3 = [0.016, 0.015, 0.014]
span_t2_3 = [0, 7, 10]
t2_3 = [0.016, 0.015, 0.014]