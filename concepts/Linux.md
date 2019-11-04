# Linux

## Document Legend
* 🔵 - Definition
* 👌 - Good Practice (Do this), 🔴 - Bad practice (Don't do this)
* 👻 - Myth
* 👍 - Advantage, 👎 - Disadvantage
* Other Emoji - These are to **emphasize** what's said in the sentences.


## Calling APIs
```asm
.data
    s:
        .ascii "hello world\n"
        len = . - s
.text
    .global _start
    _start:

        movl $4, %eax   /* write system call number */
        movl $1, %ebx   /* stdout */
        movl $s, %ecx   /* the data to print */
        movl $len, %edx /* length of the buffer */
        int $0x80

        movl $1, %eax   /* exit system call number */
        movl $0, %ebx   /* exit status */
        int $0x80 /* <<< interrupt 0x80 is used to call the api */
```
* 🔵 `syscall` is default way of entering kernel mode on x86-64. This instruction is not available in 32 bit modes of operation on Intel processors.
* 🔵 `sysenter` is an instruction most frequently used to invoke system calls in 32 bit modes of operation. It is similar to syscall, a bit more difficult to use though, but that is kernel's concern.
* 🔴 `int 0x80` is a legacy way to invoke a system call and should be avoided.


## References
* https://stackoverflow.com/a/31836988/1355145
* https://stackoverflow.com/a/12806910/1355145
