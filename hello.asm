section .data
    hello db 'This is a test message, will be using this for more assembly programs.',0

section .text
    global _start

extern _printf
extern _exit

_start:
    ; Call printf to display the string
    push hello
    call _printf
    add esp, 4

    ; Exit the program
    xor eax, eax
    call _exit
	