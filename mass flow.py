# ask maria if questions

import numpy as np
import matplotlib.pyplot as plt

cve = 6
ge = 0.798  # kg/m^3
cd = 0.5
rho_e = 789 * .001 * 3.785  # kg/m^3 -> kg/L -> kg/gal
tankP = 2.5 * 145  # MPa -> psi
chamberP = 0.8 * 145  # MPa -> psi
c = 1537  # m/s
At = 2.38 * .0001  # cm^2 -> m^2
Ae = 0.020357 * .0001  # cm^2 -> m^2

m = chamberP * At / c

deltaP1 = (m / (rho_e*cve))**2 * ge / 3600
deltaP2 = (m / (cd*Ae))**2 / (2*rho_e)
Pc = tankP - deltaP1 - deltaP2

it = 15
mdot = np.zeros(it)
Pca = np.zeros(it)
chamberPa = np.zeros(it)

for i in range(it):
    chamberP = chamberP + 0.05*145

    m = chamberP * At / c
    deltaP1 = (m / (rho_e * cve)) ** 2 * ge / 3600
    deltaP2 = (m / (cd * Ae)) ** 2 / (2 * rho_e)
    Pc = tankP - deltaP1 - deltaP2

    mdot[i] = m / 145*10**6
    Pca[i] = Pc/145
    chamberPa[i] = chamberP/145

    if chamberP > Pc:
        end = i+1
        break

Pca = Pca[Pca != 0]
chamberPa = chamberPa[chamberPa != 0]
mdot = mdot[mdot != 0]

print(Pca)
print(mdot)

print(mdot[end-1]/(789*15*4.5))
print(mdot[end-1]/rho_e*60)

x = np.linspace(0, end, end)
plt.plot(x, Pca, color='g')
plt.plot(x, chamberPa, color='r')
plt.legend(['Chamber Pressure from Mass Flow', 'Theoretical Chamber Pressure'])
plt.ylabel("Pressure (MPa)")
plt.xlabel("Iterations")
plt.show()
