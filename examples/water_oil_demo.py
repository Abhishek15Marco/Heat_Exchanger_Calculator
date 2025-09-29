import sys, os

# Add project root to Python path so it can find "src"
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.heat_exchanger import heat_load, lmtd, area_required

import matplotlib.pyplot as plt
# using matplotlib for plotting

# As an example taking hot water to heat up oil
# water : m_dot = 1.0 kg/s, Cp = 4180 J/kg.K, T_in = 90 deg C, T_out = 60 deg C
# oil : m_dot = 1.5 kg/s, Cp = 2000 J/kg.K, T_in = 20 deg C, T_out = 41 deg C

U = 450 # U is overall heat transfer coefficient W/m2.K

# water loosing heat and oil gaining this heat

Q_hot = abs(heat_load(1.0, 4180, 90, 60))
Q_cold = heat_load(1.5, 2000, 20, 41)

print( f"Heat load from the hot stream : {Q_hot/1000:.2f}  kW" )
print( f"Heat load from the cold stream : {Q_cold/1000:.2f} kW" )

# lmtd for counterflow

LMTD = lmtd(90, 60, 20, 41, flow_type = "counter")

# required area

A = area_required(Q_hot, U, LMTD)

print( f"LMTD for counterflow : {LMTD:.2f} K" )
print( f"Required area : {A:.2f} m2" )

# plotting T profiles for the counterflow

x = [0, 1]
Th = [90, 60]
Tc = [20, 41]

# matplot functions

plt.plot(x, Th, 'r-o', label='Hot fluid')
plt.plot(x, Tc[::-1], 'b-o', label='Cold fluid (counterflow)')
plt.xlabel("Exchanger length (Normalized)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature profiles in counterflow HX")
plt.legend()
plt.show()
