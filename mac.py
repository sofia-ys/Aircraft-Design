import matplotlib.pyplot as plt

S = 173.77  # wing area m^2
b = 37.98  # wing span m
AR = 8.3  # aspect ratio
taper = 0.292  # taper ratio
cRoot = 7.08  # root chord m
cTip = 2.07  # tip chord m
sweep = 31  # wing sweep deg

segments = [
    ([0, 0], [0, cRoot]), ([0, cRoot], [0, (cRoot + cTip)]), ([(b/2), ], [])
    ]

for x, y in segments:
    plt.plot(x, y, color="#8ace00")

plt.show()

