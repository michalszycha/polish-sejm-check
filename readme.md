#Badanie aktywności poselskiej

##Opis projektu
Projekt składa się ze skryptu przygotowującego informacje o posłach i ich aktywności w kontekście głosowań w danej kadencji oraz dashboardu który te informacje przedstawia.
W folderze projektu znajdują się dane i dashboard dla bieżącej, dziesiątej kadencji.

Dashboard jest wykonany za pomocą programu Power BI i zawiera następujące widoki:
- Voting (lista wszystkich głosowań)
- MPs Personal Info (lista posłów wraz ze szczegółowymi informacjami)
- MP Voting (lista jak głosował wybrany poseł)
- Voting Details per Club (wyniki wybranego głosowania z podziałem na partie/kluby)
- Voting Details per MP (wyniki wybranego głosowania z podziałem na posłów)
- Analysis of Club Yes Votes (procent głosów `TAK` z podziałem na typ głosowania i partie/kluby)
- Analysis of Club No Votes (procent głosów `NIE` z podziałem na typ głosowania i partie/kluby)
- Analysis of Club Abstain Votes (procent posłów wstrzymujących się od głosu z podziałem na typ głosowania i partie/kluby)
- Analysis of Club Absent (procent posłów nieobecnych z podziałem na typ głosowania i partie/kluby)
- Percent of Votes By Club and Category (procent głosów z podziałem na kategorie i kluby/partie)
- Distribution of Yes Votes (rozkład głosów `TAK`)

##Instalacja
Do uruchomienia skryptu jest potrzebne zainstalowanie środowiska Python. Instalator można pobrać ze strony: https://www.python.org/downloads/

Lista wymaganych bibliotek znajduje się w pliku `requirements.txt`. W celu ich zainstalowania należy otworzyć wiersz poleceń, przejść do folderu projektu i uruchomić komendę:
```
pip intstall -r requirements.txt
```

Do otworzenia pliku `.pbix` w którym znajduje się dashboard potrzebny jest program Power BI Desktop. Plik instalacyjny oraz instrukcję instalacji można znaleźć pod adresem: https://learn.microsoft.com/pl-pl/power-bi/fundamentals/desktop-get-the-desktop

##Uruchamianie
Uruchamiając skrypt przygotowujący dane można podać kadencję dla której mają zostać pobrane.
W celu uruchomienia skryptu należy otworzyć wiersz poleceń, przejść do folderu projetu i uruchomić komendę:
```
python etl_polish_sejm.py <term>
```
`<term>` jest kadencją dla której mają zostać pobrane dane. Nie podając tego argumenty program zostanie wykonany dla bieżącej, dziesiątej kadencji.


##Przygotowanie dashboardu
Po przygotowaniu danych należy otworzyć plik `.pbix`. Power BI wymaga podania ścieżki bezwzględnej do danych. Aby to zrobić należy:
1. Kliknij `Przekształć dane`.
2. Dla każdego z zapytań zmienić zawartość kroku `FilePath` na ścieżkę do odpowiedniego pliku, odpowiednio:
   1. Dla zapytania `mps` podaj ścieżkę do pliku `.../polish-sejm-check/cache/mps_term<term>.csv`
   2. Dla zapytania `voting` podaj ścieżkę do pliku `.../polish-sejm-check/cache/voting_term<term>.csv`
   3. Dla zapytania `voting_per_mp` podaj ścieżkę do pliku `.../polish-sejm-check/cache/voting_per_mp_term<term>.csv`


##Link
Kod projektu znajduje się pod linkiem: https://github.com/michalszycha/polish-sejm-check