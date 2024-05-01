#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <fstream>

#include "../matplotlib-cpp-master/matplotlibcpp.h"

namespace plt = matplotlibcpp;


class PartitaScacchi {
private:
    std::vector<std::vector<int>> scacchiera;
    std::vector<int> posizioni_pedine;
    int mosse;
    bool win;

public:
    PartitaScacchi() {
        scacchiera = std::vector<std::vector<int>>(20, std::vector<int>(12, 0));
        posizioni_pedine = std::vector<int>(12, 0);

        for (int i = 0; i < 12; ++i) {
            posizioni_pedine[i] = 0;
            scacchiera[0][i] = 1;
        }

        mosse = 0;
        win = false;
        srand(time(0));
    }

    int lancioDadi() {
        int dado1 = rand() % 6 + 1;
        int dado2 = rand() % 6 + 1;
        return dado1 + dado2;
    }

    void avanzaPedina(int colonna) {
        int riga_attuale = posizioni_pedine[colonna];
        scacchiera[riga_attuale][colonna] = 0;

        if (riga_attuale < 19) {
            posizioni_pedine[colonna] += 1;
            scacchiera[posizioni_pedine[colonna]][colonna] = 1;
        }
    }

    bool check_win() {
        for (int i = 0; i < 12; ++i) {
            if (posizioni_pedine[i] == 19)
                return true;
        }
        return false;
    }

    int winning_column() {
        for (int i = 0; i < 12; ++i) {
            if (posizioni_pedine[i] == 19)
                return i;
        }
        return -1;
    }

    int get_mosse() {
        return mosse;
    }

    bool pedina_colonna_7_prima_di_8() {
        return posizioni_pedine[6] > posizioni_pedine[7];
    }

    bool pedina_colonna_k_prima_di_tutte_le_altre(int k) {
        for (int i = 0; i < 12; ++i) {
            if (i != k && posizioni_pedine[k] <= posizioni_pedine[i])
                return false;
        }
        return true;
    }

    bool check_mosse_200() {
        return mosse <= 200;
    }

    void results() {
        std::cout << "Numero di mosse: " << mosse << std::endl;
        std::cout << "Posizioni pedine:";
        for (int i = 0; i < 12; ++i)
            std::cout << " " << posizioni_pedine[i];
        std::cout << std::endl;

        for (const auto& riga : scacchiera) {
            for (int cella : riga)
                std::cout << cella << " ";
            std::cout << std::endl;
        }

        std::cout << "Pedina in colonna 7 prima di colonna 8: " << (pedina_colonna_7_prima_di_8() ? "true" : "false") << std::endl;
        for (int i = 0; i < 12; ++i)
            std::cout << "Pedina in colonna " << i << " prima di tutte le altre: " << (pedina_colonna_k_prima_di_tutte_le_altre(i) ? "true" : "false") << std::endl;

        std::cout << "Il gioco ha durata di esattamente N mosse con N compreso tra 0 e 200: " << (check_mosse_200() ? "true" : "false") << std::endl;
        std::cout << "Il gioco ha più di 200 mosse: " << (!check_mosse_200() ? "true" : "false") << std::endl;
    }

    void play() {
        while (!win) {
            int somma_dadi = lancioDadi();
            int colonna = somma_dadi - 1;
            avanzaPedina(colonna);
            mosse += 1;

            win = check_win();
        }
    }

    void reset() {
        scacchiera = std::vector<std::vector<int>>(20, std::vector<int>(12, 0));
        posizioni_pedine = std::vector<int>(12, 0);

        for (int i = 0; i < 12; ++i) {
            posizioni_pedine[i] = 0;
            scacchiera[0][i] = 1;
        }

        mosse = 0;
        win = false;
    }
};




int main() {
    
    const int iterations = 1000000000;
    std::vector<int> victory_k(12, 0);
    int sette_prima_di_otto = 0;
    std::vector<int> mosse_tra_0_200(200, 0);
    int mosse_sopra_200 = 0;

    PartitaScacchi game;

    for (int i = 0; i < iterations; ++i) {
        game.play();
        victory_k[game.winning_column() - 1]++;
        sette_prima_di_otto += game.pedina_colonna_7_prima_di_8();
        mosse_tra_0_200[game.get_mosse()]++;
        mosse_sopra_200 += !game.check_mosse_200();

        if (i % 10000 == 0)
        {
            std::cout << "Progresso: " << i << "/" << iterations << "    " << ( (double)(i) / iterations) * 100.0 << "% " << "Nasa akkkata4.0" << std::endl;
        }
        

        game.reset();
    }

    // std::cout << "A)Probabilità pedina colonna 7 arriva prima della colonna 8:" << std::endl;
    // std::cout << (double)sette_prima_di_otto / iterations << std::endl;

    // std::cout << "B)Probabilità per colonna:" << std::endl;
    // for (int i = 0; i < 12; ++i)
    //     std::cout << "Colonna " << i + 1 << ": " << (double)victory_k[i] / iterations << std::endl;

    // std::cout << "C)Probabilità di durata N mosse con N compreso tra 0 e 200:" << std::endl;
    // for (int i = 0; i < 200; ++i)
    //     std::cout << "Mosse " << i << ": " << (double)mosse_tra_0_200[i] / iterations << std::endl;

    // std::cout << "D)Probabilità di durata più di 200 mosse:" << std::endl;
    // std::cout << (double)mosse_sopra_200 / iterations << std::endl;

    // su File txt


    std::ofstream file("statistiche.txt");  // Apre il file in modalità di scrittura

    if (file.is_open()) {
        file << "A) Probabilità pedina colonna 7 arriva prima della colonna 8:" << std::endl;
        file << (double)sette_prima_di_otto / iterations << std::endl;

        file << "B) Probabilità per colonna:" << std::endl;
        for (int i = 0; i < 12; ++i)
            file << "Colonna " << i + 1 << ": " << (double)victory_k[i] / iterations << std::endl;

        file << "C) Probabilità di durata N mosse con N compreso tra 0 e 200:" << std::endl;
        for (int i = 0; i < 200; ++i)
            file << "Mosse " << i << ": " << (double)mosse_tra_0_200[i] / iterations << std::endl;

        file << "D) Probabilità di durata più di 200 mosse:" << std::endl;
        file << (double)mosse_sopra_200 / iterations << std::endl;

        file.close();  // Chiude il file
        std::cout << "Statistiche scritte su 'statistiche.txt'." << std::endl;
    } else {
        std::cerr << "Impossibile aprire il file." << std::endl;
        return 1;
    }

    // Probabilita

    std::vector<double> probabilita_vittoria;
    std::vector<double> probabilita_mosse;

    for (int i = 0; i < 12; i++)
    {
        probabilita_vittoria.push_back((double)victory_k[i-1] / iterations);
    }
    for (int i = 0; i < 200; i++)
    {
        probabilita_mosse.push_back((double)mosse_tra_0_200[i-1] / iterations);
    }
    

    // Plot
    std::vector<double> x_values;
    for (int i = 0; i < 12; ++i) {
        x_values.push_back(i + 1);
    }
    std::vector<double> ticks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};


    plt::figure(1);
    plt::plot(x_values, probabilita_vittoria);
    plt::xticks(ticks);
    plt::save("vittoria.pdf");
    
    plt::figure(2);
    plt::plot(probabilita_mosse);
    plt::save("mosse.pdf");
    
    plt::show();

    

    return 0;
}