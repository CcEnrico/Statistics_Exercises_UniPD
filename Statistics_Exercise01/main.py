import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import Ols

# carica il dataset
data_path = "Meteo_Chioggia60.ods"

data = pd.read_excel(data_path, engine='odf', header=3)

tmin = np.hstack([data.values[::, 1]])
tmed = np.hstack([data.values[::, 2]])
ptot = np.hstack([data.values[::, 4]])


# Tmin vs Tmed
x1 = np.array(tmin)
y1 = np.array(tmed) 

# calcolo della retta di regressione
m1, q1 = Ols.least_squares(x1, y1)
y1_pred = q1 + m1*x1

# Plotta la distribuzione e la retta di regressione

plt.figure("Tmin vs Tmed", figsize=(25, 25))  
plt.title("Tmin vs Tmed", fontweight='bold')
plt.plot(x1, y1_pred, 'r')
plt.legend(['y = ' + str(m1) + ' x + ' + str(q1)])


plt.scatter(x1, y1, marker='o')
plt.xlabel( 'Tmin(C°)' , fontweight='bold')
plt.ylabel('Tmed(C°)', fontweight='bold')
plt.grid(True)


# Tmed vs Ptot
x2 = np.array(tmin) 
y2 = np.array(ptot) 

# calcolo della retta di regressione
m2, q2 = Ols.least_squares(x2, y2)
y2_pred = q2 + m2*x2

plt.figure("Tmin vs Ptot", figsize=(25, 25))
plt.title("Tmin vs Ptot", fontweight='bold')
plt.plot(x2, y2_pred, 'r')
plt.legend(['y = ' + str(m2) + ' x + ' + str(q2)])

plt.scatter(x2, y2, marker='o')
plt.xlabel( 'Tmin(C°)' , fontweight='bold')
plt.ylabel('Ptot(mm)', fontweight='bold')
plt.grid(True)


# Plotta le distribuzioni e Print dei coeficienti di regressione utilizzati per le due rette
plt.show()
print("Coeficienti di regressione per Tmin vs Tmed: m = ", m1, " q = ", q1)
print("Coeficienti di regressione per Tmin vs Ptot: m = ", m2, " q = ", q2)

