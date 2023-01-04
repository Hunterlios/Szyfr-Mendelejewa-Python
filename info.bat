@echo off
echo Autor projektu: Jakub Mrozek

echo -----------------------------------------------------

echo Program pobiera dane z plików "input/*.txt" i szyfruje zawarte tam słowa przy użyciu liczb atomowych pierwiastków z których skrótów składa się słowo. Pomiędzy każdą liczbą atomową wstawiona zostanie "*", a pomiędzy słowami "**".  

echo -----------------------------------------------------

echo Przykład: SobOta rANo - zostanie zaszyfrowane jako - 16*8*5*8*73**88*7*8. Niektórych słów nie da się zaszyfrować za pomocą programu (Nie sprawdza on wszystkich możliwych kombinacji, widząc pierwszą literę która jest symbolem pierwiastka zastępuje ją liczbą atomową, np. Hello - H = 1, El - nie istnieje).

echo -----------------------------------------------------

echo Cały projekt obudowany jest w menu, posiada ono cztery opcje: Uruchom, Opis, Backup oraz Wyjście. Główny program Pythona pobiera sobie pliki .txt z katalogu inputs, procesuje te dane i na wyjściu daje nam wynik, który zapisywany jest do plików "*.txt" w katalogu outputs. Dodatkowo tworzony jest "raport.html" generowany przez pythona. Backup robi kopie zapasową wszystkich inputów, outputów oraz "raport.html".

echo -----------------------------------------------------
echo .
echo Kliknij dowolny przycisk by wrócić do menu głównego.
pause
menu.bat
