<img alt="Logo" src="http://coderslab.pl/svg/logo-coderslab.svg" width="400">

#  Podstawy Pythona &ndash; zadania

#### Zadanie 1 - Zmienne
1. Stwórz zmienną o nazwie `temp` i wartości `15`
2. Stworz zmienną o nazwie `temp_2` i wartości `'15'`
3. Czym różnią się zmienne `temp` i `temp_2`?
4. Spróbuj wykonać operacje (dodawania, mnożenie itp) na tych zmiennych i zobcz jake będą efekty tych działań

#### Zadanie 2 - Typy
Aby sprawdzić typ zmiennej należy użyć słówka kluczowego `type`
i tak jeśli mamy zadelkarowaną zmienną `title` to poleceniem `type(title)` sprawdzimy typ zmiennej title

1. Sprawdz typy zmiennych zadeklerowanych w pierwszym ćwiczeniu
2. Napisz program w którym sprawdzsz typ zmiennej:
  1. Jeśli jest integer to wypiszesz na ekran zmienną pomnożoną przez 5
  2. Jeśli jest Float to wypiszesz na ekran zmienną podzieloną przez 5
  3. Jeśli jest stringiem to poprosu wypiszesz ten string na ekran

#### Zadanie 3 - Pętla for
1. Zadeklaruj zmienną `no_of_stars` w której będzie losowa liczba z zakreso od 1 do 20. Żeby wygenerować losową liczbę musisz użyć modułu `random` i funkcji `randint`. Przkład poniżej losuje liczbę z zakresu 0 do 5 i wyświetla ją na ekranie:
```python
import random
random_number = random.randint(0, 5)
print random_number
```
2. Wyświetl na ekranie wylosowaną liczbę.
3. Wyśwetl na ekranie tyle gwiazdek (`*`) ile wynosi wartość liczby. 

Przykład działania programu:
```python
Wylosowana liczba: 6

******
```
#### Zadanie 4 - Pętla for
1. Zadeklaruj zmienne `rows` i `columns` w której będą losowe liczby z zakreso od 5 do 15.
2. Wyświetl na ekranie wylosowane liczby.
3. Wyśwetl na ekranie prostokąt zbudowany z gwiazdek (`*`) o wylosowanych rozmiarach. 

Przykład działania programu:
```python
Wartość zmiennej rows: 5
Wartość zmiennej columns: 10

**********
**********
**********
**********
**********
```

#### Zadanie 5 - Pętla for
1. Zadeklaruj zmienne `size` w której będzie losowa liczba z zakreso od 3 do 9.
2. Wyświetl na ekranie wylosowaną liczbę.
3. Wyśwetl na ekranie choinkę zbudowaną z gwiazdek (`*`) o wylosowanych rozmiarach. 

Przykład działania programu:
```python
Wielkość choinki: 5

*
**
***
****
*****
```

Hint: 
Musisz w tym przypadku użyć dwóch zależnych od siebie pętli for. 

