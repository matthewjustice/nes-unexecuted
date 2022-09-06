# nes-unexecuted
Find unexecuted code in a NES game

## Overview

Given a build of a NES game with a labels text file (from [ld65](https://cc65.github.io/doc/ld65.html)) and a CDL output file (from [FCEUX](https://fceux.com/web/home.html) or [MESEN](https://www.mesen.ca/)), this script will find ROM addresses that were not accessed.

## Usage
```
nes_unexecuted.py labels.txt file.cdl [show-addr]
```
where:
- `labels.txt` is the labels file output from ld65 (use the `-Ln` option)
- `file.cdl` is a Code Data Logger file generated with FCEUX or MESEN
- `show-addr` is an optional parameter that tells the script to output specific byte addresses as well as labels.

## Output

The output of the tool will show the labels (and optionally specific addresses) where at least one byte was not accessed while the CDL file was logged.

## Generating the CDL file
Here's how to use FCEUX to generate the CDL file needed for this tool:
1. Open FCEUX and load the NES game
2. Debug > Code/Data Logger...
3. Code Data Logger window > Reset Log
3. Code Data Logger window > Start
4. Play the game, covering all relevant scenarios
5. Code Data Logger window > Pause
6. Code Data Logger window > Save

Here's how to use MESEN to generate the CDL file needed for this tool:
1. Open MESEN and load the NES game
2. Debug > Debugger
3. Debugger > Tools > Code/Data Logger > Reset Log
4. Play the game, covering all relevant scenarios
5.  Debugger > Tools > Code/Data Logger > Save as CDL file...


## Authors

- **Matthew Justice** [matthewjustice](https://github.com/matthewjustice)


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
