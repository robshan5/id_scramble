# ID Scrambler
A script that reads a file from standard input and finds student IDs, it then scrambles them by adding 2 to each digit and then modding 10. 

## Installation
1. First, clone the repository
```
# clone the repo
git clone https://github.com/robshan5/id_scramble
cd id_scramble
```
2. Then enter the nix flake to install all dependencies needed (python 3.12)
```
# enter the nix flake
nix develop
```
3. Lastly, run the program feeding it a text file with IDs at the start of lines
```
# run the file
python scramble-id.py < example-file.txt
```
