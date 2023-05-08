# CD-Lab

### to run lex commands on Ubuntu
```
lex filename.l 
gcc lex.yy.c -lfl
./a.out
```

### Installing Flex on Ubuntu: 
```
sudo apt-get update
sudo apt-get install flex
```

### To run lex commands on Windows
```
lex filename.l 
cc lex.yy.c 
a.exe
```

[All lex codes](https://www.geeksforgeeks.org/lex-program-count-number-words/)


## YACC Programs

### Run YACC program in windows
``` 
flex filename.l
bison -dy filename.y
gcc lex.yy.c y.tab.h
a.exe
```