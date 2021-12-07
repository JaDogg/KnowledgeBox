# C Runtime 🌊

## Document Legend
* 🔵 - Definition
* 👌 - Good Practice (Do this), 🔴 - Bad practice (Don't do this)
* 👻 - Myth
* 👍 - Advantage, 👎 - Disadvantage
* Other Emoji - These are to **emphasize** what's said in the sentences.

## Introduction 😈
* 🔵 Program object - region of **data storage** in the *execution environment*,
  the contents of which can represent values.
* 🔵 Execution environments
  * 🔵 Hosted 💻
    * You are running in a standard operating system (Windows, Linux, etc.).
    * `__STDC_HOSTED__ == 1`
  * 🔵 Freestanding ⌨
    * Embedded.
    * `__STDC_HOSTED__ == 0`

## Scope/Lifetime/Memory 🧠
* 🔵 Scope - Placement of the *declaration* defines the **scope** of an object.
  * `extern int elo;` this is in program somewhere.
  * `static int iso = 10;` internal (to file) cannot be accessed elsewhere.
  * `int eso = 100;` - external (global variables). (This is at start of a file)
  * `void myfunc(void) {int bso = 1; /* ... */ }` - bso is accessible in the block `{}`. (local variables, automatic objects)
* Placement of the *definition* defines the **lifetime** of the object.
  * `int global = 10` - (at start of a file) this has a constant address in memory. Lasts through the whole program.
  * Automatic objects have block-lifetime - Theses are in functions, control-structures (for, ..) and blocks `{}`.
  * Stack Frame - store's automatics (local variables). Return values, return addresses.
  * Static storage - `static int st_local = 100;` inside a function. - This has a static lifetime and retains it's value between calls. But it's block scope so it cannot be accessed from outside. (It's initialized on first call)
  * Allocated objects
    * Allocate - `malloc(n * sizeof(int))`
    * Deallocate - `free(yourptr);`
    * Lifetime is controlled by the programmer.
* Where?
  * Automatic - Stack
  * Allocated - Heap
  * Static - Static
* Uninitialized objects (What will you get if you `printf` these)
  * Automatic - Garbage/Random
  * Allocated - Garbage/Random
  * Global `int global` - these are initialized to zero. Standard #6.9.2
* Memory Sections (GCC) (This is in SRAM)
  * Automatic - `.stack`
  * Allocated - `.heap`
  * Value initialized static - `.data` (Knows size at link time. In all .c and libs)
  * Zero initialized static `.bss` (Knows size at link time. In all .c and libs)
  * 🔵 BSS means **block started by symbol** in PDP10 assembly.
  * Literals - `.rodata` (sometimes in `.text`)
  * Functions, Main - `.text`
  * Using `static const` will give compiler ability to optimize allocation 🤔

## The build process 🛠⚒🔨
* Compilation
  * `user headers + lib headers + C files` -> `.o` files - relocatable object files.
    * Knows required size of `.bss` and `.data`, has `.text` and `.rodata`
    * Doesn't know about heap or stack requirements (as those are obviously runtime related)
  * Compilation can be done in parallel but not the link stage.
* Linking
  * Gets Control File, Library files and .o files.
  * Control file - how to map sections to which part of memory.
    * `.text` to Flash and `.bss` `.data` to RAM.
  * Can generate map file with all address for data, functions, static objects, globals,...
* Converter - convert ELF/DWARF file to raw binary image.
* This binary image is put in to flash using some `JTag`.

## Power up ⚡
* `.cstartup` section. `0x00000` (or something else)
```
_startup:
* Set up stack pointer
* Set up .bss
* Initialize data
* Set up C runtime
* Call main()
```
* When setting up stack pointer we fill it with something such as `0xDEADBEEF` so in a stack death we can see how much of it was filled.
* When setting up `.bss` we just write 0 to it. More global objects you have longer it takes to get to main.
* Initialized global static data is going to be copied from flash to ram.
* If you need to initialize to `0` avoid specifying it. So it always go to `.bss` (Some compilers may optimize this properly and put it in the `.bss`)

## Program object path & Memory errors 🛣
* 👌 Defined-used path: Defined -> Initialized -> Used -> Destroyed. (all program objects should do this).
* 🔴 Defined-destroyed problem - We initialize, but we don't use it.
* 🔴 Defined-used problem - We define it and use it. So we get a garbage value.
* 👌 `malloc` vs `calloc` - `calloc` zero initializes it. Use `calloc` when necessary.
* 🔴 Memory Leak - never destroyed.
* 🔴 Mismatched free leak - in case of `int **array` you will need a for loop to free individual pointers and a `free(array)`. Whatever you do for initialization you will need to do for free.
* 🔴 Used after free, Destroyed-used - Use a deallocated memory.
* 🔴 Double free, destroy-after-destroy - Freeing something that is already freed.
* 🔴 Overflow - memory is written more than the size, corrupting memory. Common exploitation. (Works for both arrays in stack and heap)
* Memory regions
	* 🔵 Single region - both stack and heap in a single region of memory
	* 🔵 Dual region - stack and heap are in 2 different regions of memory.
		* Heap exhaustion - malloc returns zero.
		* Link control file can configure sizes for these regions.
		* Link time region overflow - if it's not possible to fit all things in to given ranges.
* 🔵 VLA - variable length array - where does it go? For smaller allocations it's in `.stack` and larger in `.heap`
	* Introduced in C99 where you can have dynamically sized automatic arrays (from arguments to a function, etc.)
	* MISRA-C:2012 standard - bans malloc and VLAs.
* Memory Protection Unit (ARMv6/7-M) & Stack Limit Register (ARMv8-M)


## Multi-tasking 💭
* 🔵 PC - Program Counter, SP - Stack Register, SP - Stack Pointer, (other registers) - we take a snapshot of these and swap with another tasks' snapshot to switch tasks.
* RTOS allocates - allocates task stacks in `.heap`
* User allocates - allocate task stacks in `.bss`

# Reference
* Video: https://www.youtube.com/watch?v=3F3lp_F2YpQ
