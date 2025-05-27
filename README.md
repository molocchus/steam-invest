# steam-invest

Projekt **steam-invest** polega na web-scrapingu danych z rynku Steam oraz analizowaniu ich pod kątem potencjalnych inwestycji.

# Jak uruchomić kod:

0. Sklonuj repozytorium.
1. Zainstaluj biblioteki w swoim środowisku wirtualnym, którego użyjesz do uruchamiania notebooków:
   - pandas  
   - numpy  
   - matplotlib  
   - plotly  
   - scikit-learn (`sklearn`)  
   - BeautifulSoup  
   - selenium  
2. Uruchom `Steam_data_dow.ipynb`:
   - Wybierz odpowiedni link, aby pobierać nazwy skrzynek, broni lub naklejek.  
   - Wejdź w wybrany link i wpisz odpowiednią liczbę stron w wyznaczonym miejscu.  
   - Po pobraniu nazw należy zalogować się na stronie [Steam](https://store.steampowered.com/) w przeglądarce Chrome i skopiować pliki cookies:
     - `steamLoginSecure`  
     - `sessionid`  
   - Są to dane z pliku cookies, które regularnie się zmieniają, dlatego trzeba je wprowadzać ręcznie.  
   - Po pobraniu dane przetwarzane są na plik CSV.  

3. Uruchom jeden z poniższych notebooków w zależności od tego, jakie dane zostały pobrane we wcześniejszym kroku:
   - `Steam_pred_case.ipynb`  
   - `Steam_pred_guns.ipynb`  

   Wewnątrz tych notebooków znajduje się kod do analizy pobranych danych. Dane są agregowane, a następnie budowany jest model uczenia maszynowego mający na celu ocenę jakości inwestycji.

# Projekt został napisany z czystej ciekawości — nie był projektem zaliczeniowym.

# Jak dotąd większość inwestycji okazała się trafna, a sama analiza pogłębiła moje zrozumienie rynku Steam.
