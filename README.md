# Racer-Boy
A small game based on Pygame.
I am learning about pygame library and this is the first game that i have made.
During the course of this game, i came across many new functions and features of pygame
After the game is up and runnng, it is then converted to .exe

# Description
This is a very small version of what we can do with this great [pygame](https://pypi.org/project/pygame/) library.
The user can use Left or Right Keys to move the car and then avoid the blocks.
The speed and size of the block increases as the score increases.

# Libraries used:
  - Pygame
  - random
  - time
  - cx_Freeze

#### cx_Freeze: 
What if we share this awesome game with our friend?
We can run our game because we have python and pygame installed but they do not.
Hence, we use cx_Freeze.
This is a very useful library to convert python games into windows executables.
You can find the documentation [here](https://cx-freeze.readthedocs.io/en/latest/).

We can make a racerboy.exe with
> python setup.py build 

This command will create a subdirectory called build with a further subdirectory starting with the letters exe. and ending with the typical identifier for the platform that distutils uses. This allows for multiple platforms to be built without conflicts.

****OR****
On Windows, you can build a simple installer containing all the files cx_Freeze includes for your application with

> python setup.py bdist_msi

On Mac OS X, you can use this command to build a Mac disk image. 
>bdist_dmg

# What's included?
 - Racecar.png(A png image for Race car).
 - RacerBoy.py(python program for Racer Boy)
 - Setup.py(A progtam to convert python program to .exe)
 - A folder containing the executable file of racer boy

_Run setup.py in CMD_


