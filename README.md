# Gomoku
Program na hranie hry gomoku, ktorá sa hrá ako piškvorky na hracom pláne 15 x 15 na aspoň 5 kameňov v rade.

# Návod na inštaláciu a obsluhu
## Inštalácia a spustenie
Je potrebné nainštalovať Python. V adresári projektu sa nainštaluje balíček PyGame pomocou ```py -m pip install -r requirements.txt```. Program sa potom spustí pomocou ```py gomoku.py```.

## Hranie
Hráč umiestni svoj kameň kliknutím na príslušné pole hracieho plánu, program následne zahrá svoj vlastný ťah. Hrá sa, pokým niekto nevyhrá, alebo sa nezaplní hracia plocha. Klávesou ```R``` môže hráč vo svojom ťahu hru reštarovať (začína potom ten, kdo nezačínal), klávesou ```←``` sa môže hráč vrátit o ťah naspäť a klávesou ```Q``` môže hráč program ukončiť.

# Technický popis
Program pozostáva zo základnej inicializácie modulu PyGame, pomocných zoznamov a slovníkov, funkcií starajúcich sa o správne vykreslenie hry, funkcií starajúcich sa o chod hry a z dvoch While loopov, ktoré predstavujú hru samotnú. Program ku hraniu svojich ťahov využíva algoritmus Minimax s alfa-beta orezávaním.
## Zoznamy a slovníky
Zoznam ```board``` reprezentuje hracie pole, zoznamy ```bounds4```, ```bounds7``` a ```Ls``` obsahujú predpočítané hodnoty určené k rýchlejšiemu chodu funkcií ```check_win()```
a ```move_eval()```, slovníky ```d1``` a ```d2``` slúžia k ohodnoteniu štruktúr (napríklad tri kamene v rade) pomocou funckie ```structure_eval()```.

## Funkcie - Vykreslenie hry
### draw_lines()
Táto funkcia vykresluje horizontálne a vertikálne čiary, ktoré vymedzujú jednotlivé hracie polia.
### draw_figures()
Táto funkcia vykresuje kamene, ktoré boli zahrané.
### update_display()
Táto funkcia sa stará o aktualizaciu vyobrazenia hracej plochy po jednotlivých ťahoch.

## Funkcie - Chod hry
### mark_square()
Táto funkcia označí pole v zozname ```board``` číslom príslušného hráča. Pozíciu tohoto poľa vracia.
### available_square()
Táto funkcia vracia, či je dané pole voľné.
### is_board_full()
Táto funkcia vracia, či je hracia plocha zaplnená.
### five_in_a_row()
Táto funkcia vracia, či daná štruktúra obsahuje 5 kameňov daného hráča v rade.
### check_win()
Táto funkcia vracia, či bol posledný ťah výherný pomocou funkcie ```five_in_a_row``` a zoznamu ```bounds4```.
### board_add()
Táto funkcia označí dané pole v zozname ```checkboard``` číslom príslušného hráča. Zoznam ```checkboard``` reprezentuje hraciu plochu, ktorú využíva algoritmus Minimax.
### board_del()
Táto funkcia dané pole v zozname ```checkboard``` uvoľní.
### structure_eval()
Táto funkcia prejde danú štruktúru a hľadá v nej podštruktúry (napríklad tri kamene v rade bez ohraničenia), ktoré ohodnotí pomocou jedného zo slovníkov ```d1``` alebo ```d2```. Vráti hodnotu najlepšie hodnotenej podštruktúry.
### move_eval()
Táto funkcia ohodnotí daný ťah daného hráča. Pre tento ťah určí v štyroch smeroch (vertikálne, horizontálne a diagonálne) štruktúry obsahujúce tento ťah pomocou zoznamu ```bounds7``` a tieto štruktúry ohodnotí pomocou funkcie ```structure_eval()```. Tieto hodnoty posčíta dokopy a k nim pomocou zoznamu ```Ls``` pripočíta hodnotu 50 za každý kameň daného hráča, na ktorý by dokázal skočiť šachový kôň z poľa daného ťahu. Výslednú hodnotu vráti.
### evaluation()
Táto funkcia ohodnotí jednotlivé ťahy v danom zozname pomocou funkcie ```move_eval()```. Pokiaľ sa jedná o ťah hráča, bude táto hodnota záporná. Všetky tieto hodnoty posčíta a vráti výslednú hodnotu - skóre. Jedná sa o hodnotiacu funkciu algoritmu Minimax.
### children()
Táto funkcia vracia zoznam ďalších vhodných ťahov z závislosti na ťahoch predchádzajúcich. Vracia vlastne synov daného stavu v stavovom priestore hry algoritmu Minimax.
### minimax()
Implementácia algoritmu Minimax s alfa-beta orezávaním pomocou funkcií ```evaluation()```, ```children()``` a ďalších pomocných funkcií. Funkcia v sebe zahŕňa ukončenie hry pomocou klávesy ```Q```. Vracia ťah s najvyšším skóre a toto skóre.
### best_move()
Táto funkcia pomocou viacerych volaní funkcie ```minimax()``` určí najlepší ťah.
### restart_game()
Táto funkcia reštartuje hru.
### user_input()
Táto funkcia spracováva vstupy od hráča (kliknutie myšou, stlačenie klávesy).
### process_move()
Táto funkcia spracováva hráčov ťah.
### computer_move()
Táto funkcia spracováva ťah programu určený pomocou funkcie ```best_move()```.
