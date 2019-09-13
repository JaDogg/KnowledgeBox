# Clean Code 🧹
[Clean Code](https://www.goodreads.com/book/show/3735293-clean-code) is a good book to understand how to write readable and easily maintainable code. Suggestions are directly applicable to Java ☕ and other statically typed languages. Some changes are needed for Python 🐍.

**My Opinion**: This is a really good book, how you apply the suggestions is up to you. Reading the actual book rather than a summary is recommended.

## Document Legend
* 🔵 - Definition
* 👌 - Good Practice (Do this), 🔴 - Bad practice (Don't do this)
* 👻 - Myth
* 👍 - Advantage, 👎 - Disadvantage
* Other Emoji - These are to **emphasize** what's said in the sentences.

## Meaningful Names 👶

* 👌 Use intention revealing names.
* 👌 Long names are better than names that don't make sense or acronyms.
* 👌 A Comment must not be necessary to understand what a variable does.
* 👌 Avoid mental mapping. → `l, m, n, k, j, z, p`
* 👌 Avoid using `l`(Simple L), `O`(Capital O) as names.
* 👌 Don’t encode additional details in names. → Hungarian Notation is bad.
* 👌 Make meaningful distinctions. → Don't misspell to make two names distinct. `class vs. klass`.
* 👌 Number series naming is wrong. → Avoid names such as `a1, a2, a3, a4`. (variadic or meaningful names should be used)
* 👌 Use searchable names. → `MAX_CLASSES_PER_STUDENT` instead of `7`.

### Python 🐍
* 👌 Functions - `are_like_this`
* 👌 Classes - `AreLikeThis` and `DbXmlWrapper`
* 👌 Member Functions - `are_also_like_this`
* 👌 Searchable values - `LIKE_THIS`
* 👌 Private stuff - `_starts_with_underscore`
* 👌 Ignored - `_`
* 👌 Object Names - `also_like_this`

## Functions 🤪

* 👌 A function should be able to read as a TO paragraph. And a set of functions should be read as set of TO paragraphs. (Readable from top to bottom)
  * TO `payTaxes()` we need to call `getAllExpenses()`
* 👌 A function should remain at constant level of abstraction. A function shouldn’t deal with both low level and high level stuff.
* 👌 Bury the switch statement 🎚 in an abstract factory. → Use polymorphism, and avoid switches.
* 👌 Number of arguments to a function, It should be zero (niladic) 0️⃣, one (monadic) 1️⃣ or two (dyadic) 2️⃣.
  * Three (triadic) 3️⃣ arguments are OK but should be avoided. (Argument lists are considered as a single argument)
* 👌 Instead of using Boolean arguments split the function in two. Avoid flag arguments.
* 👌 Don’t have side effects for functions.
  * `checkPassword()` function should not initialise the session.
* 👌 Avoid output arguments, Pass by reference for the purpose of modification is bad.
  * `appendFooter(StringBuffer report)` → `report.appendFooter()`
* 👌 Command query separation. A function can be a command or query but not both.
  * `setAttribute()` should not return an `attribute_exists==True`.
* 👌 Throw Exceptions instead of returning error codes.
* 👌 Error Handling is one thing. Functions that handle errors should only do that. They should start with try and end with catch or finally.
* 👌 Functions should be small 3-5(good) - 10-15(max) lines.

### Python 🐍
* 👌 For python it makes sense to have about 5 parameters with defaults because there is no way to overload a function otherwise.
* 👌 Python doesn't have a switch statement, we can use a dictionary as a mapping instead.

## Comments

* 👌 Logs in comments are clutter, use a source code control system.
* 👌 Avoid redundant comments. 😀😃😄😁😅
* 👌 Comments doesn't make up for bad code.
* 👌 Only use documentation comments if it is in a public API.
* 👌 Avoid closing braces comments. Make functions shorter instead.
* 👌 Don't comment code. Delete them completely or keep them.
* 👌 Don't add markup to comments. Ex: HTML, RST
* 👌 Avoid too much information. Ex: History of an algorithm
* 👌 Avoid function headers. You don't need a comment if function name already makes sense.
* 👌 Don't mark sections of file with banner comments.

## Formatting

* 👌 Use an automated tool for formatting.
* 👌 Whole team should agree to a certain formatting practice.
* 👌 Put high-level code first in a file. And it should be followed by low level code. Caller should be above the callee.
* 👌 Vertical Openness. → Separate each concepts.
* 👌 Vertical Density. → Keep related things closer.
* 👌 Vertical Distance. → Variables should be declared closer to their usage. Instance variables should be in either top of the class (Java) or the bottom of the class (C++).

### Python 🐍
* 👌 Unless you need to set a default value just define at the location you are assigning.

##	Objects and Data Structures

* 👌🔵 Law of Demeter. → Avoid method chaining to access unknown data. ❓ A function will know too much. 🙈 Don't talk to strangers.
* 👌 Procedural code makes it harder to add new data structures because all the functions should change. However you can add new functions easily without changing the data structures.
* 👌 OO code makes it harder to add new functions because all the classes must change. Easier to add new classes without changing functions.
* 👌🔵 Feature Envy. 🥵 → Don't create data structure + object hybrids. Example: Data transfer objects + Business Rule methods. (Put these to 2 classes)
* 👌 An Object exposes behavior and hides data.
* 👌 A data structure exposes data and has no behavior.

## Error Handling

* 👌 Error handling should not obscure logic 🖖. → High level functions can handle errors thrown by low level functions.
* 👌 Raise exceptions instead of returning error codes.
* 👌 Do not use checked exceptions. (Checked exceptions violate open/closed principle.)
* 👌 Provide context with exceptions.
* 👌 Write tests that forces exceptions.
* 👌🔵 Special Case Pattern. → Encapsulate special cases of business logic in a class.
* 👌 Don't return null. → Return a special case object or throw an exception.
* 👌 Don't pass null. → If you need to pass null to something it is a problem.
* 👌 Write try-catch-finally statement first. → If you are using TDD write a test that expects exceptions first.

### Python 🐍
* 👌 Python supports exceptions. Instead of returning error codes use exceptions.
* 👌 Even if your whole code doesn't use exceptions python std library uses them.

## Boundaries

* 👌 When using third party code - instead of depending on their implementations directly, depend on wrapper classes with limited features.
* 👌 Learn boundaries through *learning tests*.
* 👌 Learning tests can be used to verify newer releases.
* 👌 Adaptor pattern is useful when dealing with things that doesn't exist.
  * Create an interface, use it. When the API is completed create an *Adaptor*.
  * When the API changes only the adaptor needs to change.

## Unit Tests

* 👌 Unit Tests should be written with same care as the production code.
  * Easier to change when the production code is refactored or changed.
  * However tests don't need to be as efficient as production code. (Memory efficient, Size efficient...)
* 👌 TDD - Test Driven Development
  * Failing test 🔴 
  * Make test pass ✅
  * Refactor 🔵
* 👌 Three Laws of TDD
  * 1️⃣ You may not write production code until you have written a failing unit test.
  * 2️⃣ You may not write more of unit test than is sufficient to fail, and not compiling is failing.
  * 3️⃣ You may not write more of production code that is sufficient to pass current failing test.
* 👌 Test a single concept in a single test.
* 👌 Test function should have `BUILD-OPERATE-CHECK` sections.
* 👌 Create a domain specific testing language based on the assertions you need to make. Example: `assertHtmlEquals()`, `assertResponseIsXml()`
  * Possible to use `GIVEN-WHEN-THEN` approach for naming.
* 👌 Use *Template* Pattern to avoid duplication.
* 👌🔵 F.I.R.S.T.
  * Fast. → Fast unit tests can be executed often. Find problems early. 🚗
  * Independent. → Test should not depend on each other. 🔵
  * Repeatable. → Tests should be repeatable in any environment. 🔵-🔵-🔵
  * Self-Validating. → You should be able to easily identify which tests passed and which failed. ✔
  * Timely. → Tests should be written in a timely manner. Unit tests should be written just before the production code that makes them fast. ⌚

## Classes

* 👌 Organization. → (Java) Public Static, Private Static, Private (Order stuff inside the class in this order)
* 👌 Step-down rule. → (Set of TO paragraphs) for public and their required private functions.
* 👌 Encapsulate utility functions inside the classes.
  * Can make them protected so they are exposed to tests.
  * Loosening encapsulation should always be a last resort.
  * Tests rule. 🤘
* 👌 Classes should be small. 🤏
  * Count responsibilities. Reasons to change.
  * Class name is given to show its responsibility.
  * The Single Responsibility Principle - Exactly one responsibility and one reason to change.
* 👌 Class names with `Processor`, `Manager`, `Super` often hints unfortunate aggregation of responsibilities.
  * A class's responsibility should be explainable in 25 words without using *if*, *and*, *or*, *but*.
* 👌 System with many small classes has no more moving parts than a system with very few large classes.
* 👌 High Cohesion.
  * Classes should have small number of instance variables.
  * Each method of class should manipulate one or more of the variables.
  * Methods and instance variables are co-dependent as a whole.
  * When cohesion is low break the class apart.
* 👌 Depend on abstractions and not concrete details.

### Python 🐍
* 👌 It is considered a good practice to avoid classes unless required.
  * For scripts that does some simple scraping / automation - Not required.
  * For an automation framework - Maybe Required.
  * Write a complex context manager - Maybe Required if you cannot use `@contextlib.contextmanager`.
* 👌 Avoid properties in classes unless you need to do some calculation.
* 👌 Meta classes - Avoid using unless you are writing something that needs special kind of classes.
  * You are writing an ORM - Maybe Required.
  * You are using an ORM - Maybe Required to use an already defined meta class. Don't define your own.

## Systems

* 👌 Separate **constructing** a system from **using** it. (Factory/DI)
  * Software systems should separate the startup process, when the application objects are constructed and the dependencies are "wired" together; from run-time logic that takes over after startup.
  * Don't mix startup code and run-time logic.
* 👌 Separation of Main
  * Move all aspects of construction to `main` or modules called by `main`.
* 👌 Factories
  * Abstract Factory Pattern allows handling when certain objects are created. In that case main can create an object of Abstract Factory implementation and pass it.
* 👌 Dependency Injection
  * Classes provide setter methods or constructor arguments to get dependencies.
* 👌 Test Drive the system architecture.
  * Start a software project with a naively simple but nicely decoupled architecture.
  * Expect changes.
  * An optimal system architecture consists of modularized domains of concern, each of which is implemented with POJOs. The different domains are integrated together with minimally invasive Aspects or Aspect-like tools. This architecture can be test driven just like the code.
* 👌 Optimize decision making
* 👌 Use standards wisely, when they add demonstrable value.
* 👌 Systems need Domain Specific Languages.
  * Can be a small scripting language or an API in standard language.
  * A good DSL minimizes the communication gap between a domain concept and the code that implements it.
* 👌 Use the simplest thing that can possibly work.

## Emergence

* 🔵 Kent Beck's four rules of simple design. (Given in order of importance)
  * 👌 Run all the tests.
    * System is comprehensively tested.
    * Pass all the tests all the time.
    * More tests we write more testable the system becomes. (Follow SRP and DIP)
    * Testable systems mostly have better designs.
  * 👌 Contains no duplication.
    * After tests are available cleaning up can happen. Since we can ensure that the system works after cleaning up because of tests.
    * Use TEMPLATE METHOD pattern.
  * 👌 Expresses the intent of the programmer.
    * Choose better names. One cannot be surprised when one hear a class or function name and then hear its responsibilities.
    * Small classes and small functions are easier to name.
    * When you are using standard design patterns, use their names.
    * Well written unit tests.
  * 👌 Minimizes the number of classes and methods.
    * Make classes and methods count lower but not to the level it becomes a dogma.
    * Be pragmatic.
    * This has the lowest priority of the four.

## Concurrency
* 🔵 Concurrency is a decoupling strategy - Decouple what gets done from when it gets done.
* Why? - Response time & throughput constraints.
* 👻 Concurrency always improve performance - sometimes improve performance when there is wait time that can be shared between multiple threads/processes.
* 👻 Design is same as single threaded - Decouple **what** and **when** has an huge effect on the system architecture.
* 👻🔴 Understanding concurrency issues is not important when working with containers (Web/EJB) or frameworks that takes care of things for you.
  * 👌 Understand what the container/framework does.
  * 👌 Understand how to guard against concurrent updates and possible deadlocks/etc.
* 👎 Concurrency incurs some overhead in performance and code.
* 👎 Correct concurrency can be complex even for simple problems.
* 👎 Concurrency bugs **aren't usually repeatable** (They get ignored as one time glitches/cosmic-rays😂)
* Concurrency require fundamental change in design strategy.
* 🔵 Concurrency Defense Principles
  * 👌 Keep your concurrent code separate from other code.
    * Concurrency related code has it's own life cycle of development/change/tuning.
    * Has different challenges, can be more complex than non concurrency related code.
    * Miswritten code can make it hard to debug. If you have concurrent code mixed with application logic it will be even harder to understand what's going on.
  * 👌 Limit scope of data
    * 👌 Use `synchronized` keyword to protect a critical section.
    * 👌 Limit critical sections.
    * 👌 Encapsulate and severely limit the access to any shared data.
  * 👌 Use copies - avoid data sharing by copying. Collect copies and merge might also be a good alternative.
    * Depending on the situation saving on avoiding locks on shared data will likely make up for creation and garbage collection overhead.
  * 👌 Independent threads - partition data to subsets than can be operated on by independent threads, maybe in different processors.
  * 👌 Know your library
    * Use thread safe collections. `ConcurrentHashMap vs HashMap`
    * Use executor framework for executing unrelated tasks.
    * Use non-blocking solutions.
    * Avoid non-thread safe classes.
    * 🔵 `ReentrantLock` - acquired in one method and released in another.
    * 🔵 `Semaphore` - lock with a count (waits until a permit is available on acquire).
    * 🔵 `CountDownLatch` - waits for number of events before releasing all threads waiting on it. Give a chance of stating at about the same time.
