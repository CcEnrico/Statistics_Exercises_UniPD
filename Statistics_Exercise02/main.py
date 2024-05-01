import matplotlib.pyplot as plt
import numpy as np
import time as t
import PMF
    

N_p_M = 1000000
M_max = 5000
p = 0.5
step = 5
M_values = np.linspace(0, M_max, step, dtype=int)
A_win = []

N_values = N_p_M - M_values

start_time = t.time()

print(M_values)

i = 0
for M, N in zip(M_values, N_values):
    k_values = np.arange(int((N - M) / 2) + 1, N)

    p_A = np.sum([PMF.pmf(N, k, p) for k in k_values])

    # implementazione funzione scipy 25x piu lento rispetto al primo
    # p_A = np.sum([PMF.scipy_pmf(N, k, p) for k in k_values])
    print(i)
    i += 1
    
    A_win.append(p_A)

end_time = t.time()

elapsed_time = end_time - start_time 
print('Tempo di pmf: ', elapsed_time)

plt.plot(M_values, A_win)
plt.xlabel('M')
plt.ylabel('Probabilità di vittoria di A')
plt.title('Probabilità di vittoria di A in funzione di M per N + M =1000000')
plt.savefig('probabilita_vittoria_A.pdf')
plt.show()
