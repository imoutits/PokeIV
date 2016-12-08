# PokeIV
Pokemon GO management tool using [pgoapi](https://github.com/pogodevorg/pgoapi).

# About
PokeIV provides an interface to manage your pokemon in Pokemon Go. 

# Current features
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
  
# Requirements
Python TK:

For Ubuntu run:
```
sudo apt-get install python python-tk
```
For Windows, something like this:
```
Download and install C compiler and redistributable installers from Visual Studio downloads section.
Download and install Python 3.5 or higher and add to PATH!
Use pip to install mycryptodomex with --no-use-wheel.
Run python setup.py install, from within the pgoapi folder if after installation PokeIV whines about installing protobuf!
```

### Installation
```
git submodule init
git submodule update
pip install -r requirements.txt
```

# Screenshot
![pokeIV screen shot](./screenshot.jpg "Screenshot")
