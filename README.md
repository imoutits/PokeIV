# PokeIV
Pokemon management tool for Go using [pgoapi](https://github.com/pogodevorg/pgoapi).

# About
PokeIV provides an interface to manage your pokemon in Pokemon Go. 

Current features:
* Player information
* Batch pokemon transfering. 
* Batch pokemon evolution.
* Batch renaming pokemon with configurable format.
* Lists of pokemon all pokemon indicating their IV, CP, ATK, DEF, and STA.
  * Pokemon are divided into 3 lists:
    * Highest IV pokemon--those above a given threshold (default 80%)
    * Pokemon that can be evolved, in descending IV order (evolve the best first)
    * Recommended pokemon to transfer--those which can/should not be evolved and are below threshold(s)
* Options to set how the tool splits up and displays your pokemon.
  * White/black lists to only display the pokemon you want to
  * delays for transferring, evolution and renaming to avoid suspicious activity
  
# Linux / other
Requires Python 2/3

E.g. in Ubuntu run:
```
sudo apt-get install python python-tk
```

### Installation
```
pip install -r requirements.txt
```

# Screenshot
![pokeIV screen shot](./screenshot.jpg "Screenshot")
