# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 18:33:50 2024
Sammenligne årlige totalkostnader for elbil og bensinbil samt årlig kostnadsdifferanse
    
@author: robhan
"""
km = 16000  # Km/pr år, begge biler
trafikkforsikringsavgift = 8.38*365  # pr/år, begge biler
forsikring_elbil = 5000  # pr/år
forbruk_elbil = 0.2  # kWh/km
strømpris_elbil = 2.00  # kr/kWh
bomavgift_elbil = 0.1  # pr/Km
bomavgift_bensinbil = 0.3  # pr/km
forbruk_bensinbil = 1.0  # kr/km
forsikring_bensinbil = 7500  # pr/år

  # kostnader bensinbil
drivstoffkostnader_bensinbil = forbruk_bensinbil * km
bomavgift_bensin = bomavgift_bensinbil * km
totalkostnader_bensinbil = forsikring_bensinbil + trafikkforsikringsavgift + drivstoffkostnader_bensinbil + bomavgift_bensin

  # kostnader elbil
drivstoffkostnader_elbil = forbruk_elbil * strømpris_elbil * km
bomavgift_el = bomavgift_elbil * km
totalkostnader_elbil = forsikring_elbil + trafikkforsikringsavgift + drivstoffkostnader_elbil + bomavgift_el

print("årlige kostnader for bensinbil =" , totalkostnader_bensinbil)
print("årlige kostnader for elbil =" , totalkostnader_elbil)
print("årlig kostnadsdifferanse =" , totalkostnader_bensinbil - totalkostnader_elbil)
