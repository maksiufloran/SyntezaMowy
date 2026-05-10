# Syntezator komunikatów PKP Warszawa Centralna

Prosty syntezator korpuskularny napisany w Pythonie, służący do generowania komunikatów głosowych o odjazdach i przyjazdach pociągów. Program łączy gotowe próbki dźwiękowe w pełne zdania.

## 1. Struktura folderów

Dla poprawnego działania programu, w katalogu głównym muszą znajdować się następujące foldery z plikami `.wav`:

* `/do_z_stacji` – zawiera frazy wprowadzające (np. `pociag_ze_stacji.wav`, `do_stacji.wav`).
* `/perony_i_tory` – zawiera nagrania torów i peronów (np. `drugiego.wav`, `trzecim.wav`, `przy_peronie.wav`).
* `/stacje` – zawiera nazwy miejscowości (np. `warszawa_wschodnia.wav`, `kutno.wav`).
* `main.py` – główny plik programu.

## 2. Jak to działa?

Program działa w cyklu przetwarzania tekstu na dźwięk:
1.  **Pobranie tekstu:** Użytkownik wpisuje komunikat (np. "Pociąg do stacji Poznań...").
2.  **Normalizacja:** Tekst jest czyszczony z polskich znaków i zamieniany na format pasujący do nazw plików (małe litery, podkreślniki zamiast spacji).
3.  **Mapowanie plików:** Program skanuje foldery i sprawdza, które fragmenty tekstu mają swoje odpowiedniki w plikach audio.
4.  **Generowanie:** Program "skleja" surowe dane dźwiękowe (ramki) z wybranych plików i zapisuje je jako jeden nowy plik `.wav`.

## 3. Opis funkcji

### `string_converter(text)`
* **Zadanie:** Przygotowuje tekst do wyszukiwania plików.
* **Działanie:** Zamienia wszystkie litery na małe, podmienia polskie znaki diakrytyczne (np. `ą` -> `a`, `ł` -> `l`) oraz zamienia spacje na znaki podkreślenia `_`.

### `file_finder(text)`
* **Zadanie:** Kataloguje dostępne nagrania.
* **Działanie:** Przeszukuje trzy foldery źródłowe. Jeśli nazwa pliku (bez rozszerzenia `.wav`) znajduje się w przetworzonym tekście, dodaje ścieżkę do tego pliku do słownika.

### `wav_create(text, wav_files, file_name)`
* **Zadanie:** Tworzy wynikowy plik audio.
* **Działanie:** * Iteruje po znakach tekstu, budując frazy i dopasowując je do znalezionych plików.
    * Otwiera każdy dopasowany plik za pomocą modułu `wave`.
    * Pobiera parametry dźwięku (częstotliwość, kanały) z pierwszego pliku.
    * Łączy ramki audio wszystkich plików i zapisuje je pod wskazaną nazwą.

## 4. Uruchomienie

1.  Upewnij się, że masz zainstalowanego **Pythona 3.x**.
2.  Umieść skrypt w folderze z nagraniami (zachowując strukturę opisaną w punkcie 1).
3.  Uruchom program:
    ```bash
    python main.py
    ```
4.  Po uruchomieniu program wygeneruje plik testowy `test.wav`.
5.  Następnie w konsoli pojawi się pole do wpisywania własnych komunikatów. Każdy wpisany komunikat stworzy nowy plik `.wav`, którego nazwa będzie zawierać 8 pierwszych znaków wpisanego tekstu.

---
*Projekt wykonany w ramach ćwiczeń z syntezy mowy.*