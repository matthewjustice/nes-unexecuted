# nes-unexecuted
Find unexecuted code in a NES game

## Overview

Given a build of a NES game with a `labels.txt` file (from [ld65](https://cc65.github.io/doc/ld65.html)) and a CDL output file (from [FCEUX](https://fceux.com/web/home.html)), this script will find ROM addresses that were not accessed.

## Usage
```
nes_unexecuted.py labels.txt file.cdl [show-addr]
```
Where:
- `labels.txt` is the labels file output from ld65 (use the `-Ln` option)
- `file.cdl` is a Code Data Logger file generated with FCEUX
- `show-addr` is an optional parameter that tells the script to output specific byte addresses as well as labels.

## Output

The output of the tool will show the labels (and optionally specific addresses) where at least one byte was not accessed while the CDL file was logged.

## Generating the CDL file.
1. Open FCEUX and load the NES game
2. Debug > Code/Data Logger... > Start
3. Play the game, covering all relevant scenarios
4. Pause CDL log
5. Save CDL log to file
