# Wstępnie jak wszystko na razie działa
W grid.py na razie musimy ustawić sobie wielkość boku kwadratowej siatki
w net = Net(x). Za pomocą tego programu tworzymy wzory którym nadajemy
konkretny numer (kategorię) i zapisujemy. Kilka wzorów może mieć przypisany
jeden numer(kategorię). Na razie pominąłem możliwość twortzenia katalogów
podczas tworzenia danych. Kategorie muszą być numerowane ciągle począwszy
od 0

W programie perceptron.py po if \_\_name\_\_ == '\_\_main\_\_'. W
perceptron=Perceptron(r, s) należy podać:
r - ilość kwadratów w siatce x^2, s - ilość kategorii   
Wywołanie: python perceptron.py katalog_z_danymi_do_uczenia nauczona_sieć   
nauczona_sieć jest zapisaną klasą Perceptron

W asking.py wywołanie:
python asking.py nauczona_siec   
Możemy się bawić w testowanie
