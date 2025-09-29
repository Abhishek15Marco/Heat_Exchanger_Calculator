import matplotlib.pyplot as plt
# using matplotlib for plotting

from src.Heat_Exchanger.py import heat_load, lmtd, area_required

# As an example taking hot water to heat up oil
# water : m_dot = 1.0 kg/s, Cp = 4180 J/kg.K, T_in = 90 deg C, T_out = 60 deg C
# oil : m_dot = 1.5 kg/s, Cp = 2000 J/kg.K, T_in = 20 deg C, T_out = 41 deg C

U = 450 # U is overall heat transfer coefficient W/m2.K

# water loosing heat and oil gaining this heat

Q_hot = heat_load(1.0, 4180, 90, 60)
Q_cold = heat_load(1.5, 2000, 20, 41)

print( "Heat load from the hot stream : {Q_hot/1000:.2f} kW")
print( "Heat load from the cold stream : {Q_cold/1000:.2f} kW")

# lmtd for counterflow

LMTD = lmtd(90, 60, 20, 41)
