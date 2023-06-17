# Gra tower defense

Projekt został napisany przez Marcina Banaka jako zadanie końcowe, na zaliczenie pracowni, z przedmiotu "programowanie obiektowe" nauczanego na Instytucie Informatyki Uniwersytetu Wrocławskiego.

## Spis treści

 * [Informacje ogólne](#informacje-ogólne)
 * [Dokumentacja](#dokumentacja)
 * [Pobieranie](#pobieranie)
 * [Uruchamianie](#uruchamianie)
 * [Zrzuty ekranu](#zrzuty-ekranu)

## Informacje ogólne

Projekt został napisany w języku python przy użyciu biblioteki pygame, odpowiadającej za jego reprezentację graficzną. 
Program przedstawia grę typu "obrona wieży", w której zadaniem gracza jest budowanie wież, aby ochronić swoją bazę,
przed nadciągającymi falami wrogów.

## Dokumentacja
Dokumentacja zawiera opis poszczególnych klas, metod i stałych. Aby ją zobaczyć należy pobrać repozytorium i otworzyć za pomocą przeglądarki, plik znajdujący się pod adresem ".\docs\_build\html\main.html".

## Pobieranie

Aby pobrać program, należy przejść do [repozytorium projektu](https://github.com/marcin-banak/tower-defense-game), wcisnąć zielony przycisk z napisem "Code", który rozwinie kolejną zakładkę, na końcu której znajduje się kolejny przycisk "Download ZIP", tak jak na załączonym obrazku. Pobrany plik należy rozpakować.

<a>
  <img align="center" width="47%" src=".\ReadmeAssets\GithubDownloadInstruction.png"/>
</a>

## Uruchamianie

#### Instalacja elementów niezbędnych do uruchomienia programu:

 - Interpreter Python 3.11
    1. Pobranie interpretera [Pythona](https://www.python.org).
    2. Instalacja zgodnie z zalecanymi ustawieniami instalatora (należy zaznaczyć opcję dodającą Pythona do ścieżki systemu).

 - Biblioteka Pygame 2.3
    1. Uruchomienie wiersza poleceń systemu Windows (cmd).
    2. Wpisanie "pip install pygame".
    3. Jeżeli polecenie nie zostanie rozpoznane, należy upewnić się, że interpreter Pythona został poprawnie zainstalowany i dodany do ścieżki systemu.
    4. Jeżeli w dalszym ciągu polecenie "pip install pygame" nie jest wykonywane prawidłowo, należy spróbować użyć polecenia "python -m pip install pygame".

#### Uruchomienie Programu:

   - Należy upewnić się, że podane poniżej pliki, znajdują się w jednym folderze.
     * main.py, ArcherTower.py, Arrow.py, ArtilleryTower.py, Beam.py, Bomob.py, Building.py, Button.py, CONST.py, Enemy.py, font.ttf, Footman.py, Knight.py, MageTower.py, map.txt, mouse.py, Projectile.py, Tile.py, TileButton.py, Wolf.py, folder z teksturami o nazwie Textures
   - Uruchomienie wiersza poleceń systemu Windows (cmd). 
   - Przejście do folderu, gdzie znajdują się pliku programu. 
   - Użycie polecenia "python main.py".

## Zrzuty ekranu

<a>
  <img align="left" width="47%" src=".\ReadmeAssets\MenuImage.png"/>
</a>
<a>
  <img align="right" width="47%" src=".\ReadmeAssets\GameImage.png"/>
</a>
