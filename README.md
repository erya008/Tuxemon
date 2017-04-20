Pokemon Voz 
=========

A voice controlled pokemon prototype based on Tuxemon 0.3.2

![screenshot](http://www.tuxemon.org/images/featurette-01.png)

Requirements
-----------

Tuxemon uses a number of open source projects to work properly:

* *python* - version 2.7+
* *python-pygame* - python game library
* *python-pytmx* - python library to read Tiled Map Editor's TMX maps.
* *python-six* - python 2 and 3 compatibility library
* *[neteria](https://github.com/ShadowBlip/Neteria)* - Game networking framework for Python.

*Optional*

* *libShake* - rumble library for Linux.

Installation
--------------

**Ubuntu**

```sh
sudo apt-get install python python-pygame python-pip python-imaging python-six git
sudo pip install pytmx
sudo pip install neteria
git clone https://github.com/Tuxemon/Tuxemon.git
cd Tuxemon/tuxemon
./tuxemon.py
```

*Optional rumble support*

```sh
sudo apt-get install build-essential
git clone https://github.com/zear/libShake.git
cd libShake/
make; make install
```

**Mac OS X (Yosemite)**

```sh
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew tap Homebrew/python
brew update
brew install python
brew install sdl sdl_image sdl_ttf portmidi hg git
brew install sdl_mixer --with-libvorbis
pip install pytmx
pip install pillow
pip install six
pip install neteria
pip install hg+http://bitbucket.org/pygame/pygame
git clone https://github.com/Tuxemon/Tuxemon.git
cd Tuxemon/tuxemon
ulimit -n 10000; python tuxemon.py
```

**Arch Linux**

Tuxemon is available in the [AUR](https://aur.archlinux.org/packages/tuxemon-git/).

**Smartphones**
* [Android](http://www.tuxemon.org/files/builds/tuxemon-unstable-latest.apk) (APK file)

Controls
--------------

##### Tuxemon
* *Arrow Keys* - Movement
* *Enter* - Select/activate
* *ESC* - Menu/Cancel


