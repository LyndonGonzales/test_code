ECHO OFF
REM gcc -m32 -o hello.exe hello.obj 
REM -lmsvcrt 
REM -mconsole 
REM -nostartfiles 
REM -lkernel32  --never worked 

SET PROG_NAME=parameters
REM SET PROG_NAME=hello

ECHO ON
nasm -f win32 %PROG_NAME%.asm -o %PROG_NAME%.obj 
gcc -m32 -o %PROG_NAME%.exe %PROG_NAME%.obj -nostartfiles -lmsvcrt 