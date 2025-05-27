# steam-invest
Projekt Stem-Invers polega na web-scrappingu danych z Rynku Steam oraz anazlizowaniu ich pod kątem potencjalnych inwestycji.
# Jak uruchomić kod:
1. Zainstaluj biblioteki i w swoim środowisku wirtualnym, którego użyjesz do uruchamiania notebooków:
 - Pandas
 - Numpy
 - matplotlib
 - plotly
 - sklearn
 - BeautifulSoup
 - selenium
2. Uruchom Steam_data_dow.ipynb
   - Należy wybrać odpowiedni link, aby pobierać nazwy skrzynek, broni albo naklejek
   - Należy wejść w wybranego linka i wpisać odpowiednią libiczbę stron w wyznaczonym do tego miejscu
   - Po pobraniu nazw należy zalogować się na stronie [steama](https://store.steampowered.com/) w przegląrce Chrome i trzeba skopiować Cookies:
     - steamLoginSecure
     - sessionid
   - Są to dane z pliku Cookies, które regularnie się zmieniają dlatego trzeba je wprowadzać ręcznie
   - Po pobraniu dane przerabiane są na plik CVS.
3. Uruchom jeden z notebooków zależnie od tego jakie dane pobrało się we wcześniejszym kroku:
  - Steam_pred_case.ipynb
  - Steam_pred_guns.ipynb
  Wewnątrz tych notebooków zanajduje się kod do analizy pobranych danych.
  Dane są agregowane oraz konstruowany jest model Machine Learningowy mający na celu ocenę jakości inwestycji.

# Projekt został napisapisany z czystej ciekwaości, nie był projektem zaliczeniowym
# Jak narazie większość inwestycji okazała się być skuteczna, a sama analiza pogłębiła moje zrozumienie rynku Steam
