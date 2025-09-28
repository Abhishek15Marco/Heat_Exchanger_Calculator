import numpy as np

def heat_load (m_dot, Cp, T_in, T_out):
  
  # Calculating the heat load of exchanger
  # m_dot : mass flow rate (kg/s)
  # Cp : heat capacity (J/kg.K)
  # T_in : inlet temperature (K)
  # T_out : outlet temperature (K)
  # heat load = m_dot * Cp * (T_out - T_in)

  return m_dot * Cp * (T_out - T_in)

def lmtd (TH_in, TH_out, TC_in, TC_out, flow_type):

  # Calculating Log Mean Temperature Difference (lmtd)
  # TH_in : hot fluid inlet temperature
  # TH_out : hot fluid outlet temperature
  # TC_in : cold fluid inlet temperature
  # TC_out : cold fluid outlet temperature
  #  flow_type : can either be parallel or counter

  if (flow_type == "counter"):
    dT1 = TH_in-TC_out
    dT2 = TH_out-TC_in
  elif (flow_type == "parallel"):
    dT1= TH_in-TC_in
    dT2 = TH_out-TC_out
  else:
    raise ValueError("flow_type must be either 'parallel' or 'counter'")

  if (dT1=dT2):
    # To avoid log(1)
    return dT1
  return (dT1 - dT2) / np.log(dT1/dT2)

def area_required (Q, U, lmtd):

  # Calculating the area required for heat exchanger
  # Q : heat load (W)
  # U : overall heat transfer coefficient (W/m2.K)
  # lmtd : log mean temperature difference (K)

  return Q / (U * lmtd)
