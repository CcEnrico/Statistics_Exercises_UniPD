import matplotlib.pyplot as plt
import time as t
import game

game = game.PartitaScacchi()

volte = 1
# iterations = 1000000 per output tempi normali
iterations = 100000 * volte
victory_k = [0] * 12
probability_k = [0] * 12

sette_prima_di_otto = 0
mosse_tot = 0
mosse_tra_0_200 = [0] * 200
probability_mosse = [0] * 200
mosse_sopra_200 = 0

progress = 0

start_time = t.time()

expected_time = 18.552276611328125 * volte

for i in range(iterations):
    game.play()

    victory_k[game.winning_column()] += 1
    sette_prima_di_otto += game.pedina_colonna_7_prima_di_8()
    mosse_tra_0_200[game.get_mosse()] += 1
    mosse_sopra_200 += not game.check_mosse_200()

    game.reset()

    current_time = t.time()


    progress += 1
    if progress % 10000 == 0:
        print("Progress: {}/{} , time: {}s, Remaining Time: {}s".format(progress, iterations, current_time - start_time, expected_time - (current_time - start_time)))


end_time = t.time()

elapsed_time = end_time - start_time

print("Elapsed time: {}".format(elapsed_time))


for i in range(12):
    probability_k[i] = victory_k[i] / iterations
    
for i in range(200):
    probability_mosse[i] = mosse_tra_0_200[i] / iterations
    


# Results

output_file = "results.txt"

with open(output_file, "w") as file:
    file.write("Probabilità dei seguenti eventi con {} iterazioni:\n".format(iterations))

    file.write("a) La pedina della colonna sette arriva prima di quella della colonna otto.\n")
    file.write("Probabilità: {:.15f}\n".format(sette_prima_di_otto / iterations))

    file.write("b) La pedina della colonna k arriva per prima, con k ∈ {1, . . . , 12}.\n")
    for i in range(12):
        file.write("Colonna {}: {:.15f}\n".format(i + 1, probability_k[i]))

    file.write("c) Il gioco ha durata di esattamente N mosse, con N ∈ {1, . . . , 200}.\n")
    for i in range(200):
        file.write("Mosse {}: {:.15f}\n".format(i + 1, probability_mosse[i]))

    file.write("d) Il gioco ha durata di più di 200 mosse.\n")
    file.write("Probabilità: {:.15f}\n".format(mosse_sopra_200 / iterations))

    file.write("Tempo Impiegato: {}s\n".format(elapsed_time))

print("Results written to {}".format(output_file))


# Plot
plt.figure(1)
plt.plot(range(1, 13), probability_k)
plt.xticks(range(1, 13))

plt.xlabel('Colonna')
plt.ylabel('Probabilità')
plt.title('Probabilità di vittoria per colonna')
plt.savefig('probabilita_vittoria_colonna.pdf')


plt.figure(2)
plt.plot(range(1, 201), probability_mosse)
plt.xlabel('Mosse')
plt.ylabel('Probabilità')
plt.title('Probabilità di durata del gioco')
plt.savefig('probabilita_durata_gioco.pdf')
plt.show()