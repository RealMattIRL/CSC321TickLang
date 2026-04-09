Tick — A Minimal Timed‑Event Scripting Language
Tick is a tiny, timeline‑driven scripting language built for sequencing actions with precise timing.
Programs execute linearly from top to bottom, making Tick ideal for simple, predictable timed behaviors.

Overview
A Tick program reads like a timeline:

Code
ping
wait 2
signal 5
flash
Each command fires at a specific moment, with wait n advancing the internal clock.
The language is intentionally minimal—no variables, loops, or branching—so behavior is always easy to reason about.

Repository Structure
Code
CSC321TickLang/
│
├── main.py               # Entry point for running Tick programs
├── pyproject.toml        # Project metadata
├── uv.lock               # Dependency lock file
│
├── src/                  # Core language implementation
│   ├── Parser.py
│   ├── ParserOut.py
│   ├── TempAST.py
│   ├── Token.py
│   └── Lexer + helpers
│
├── tests/                # Test suite for lexer, parser, and sample programs
│   ├── valid.tick
│   ├── valid2.tick
│   ├── invalid.tick
│   ├── testLexer.py
│   └── testParser.py
│
└── .idea/                # IDE configuration (PyCharm)
Language Features
Supported Commands
Command	Description
wait n	Delay next action by n ticks (non‑negative integer)
ping	Emit a "ping" event
beep	Emit a "beep" event
signal n	Emit a numeric signal (non‑negative integer)
flash	Emit a "flash" event

Execution Model
Linear, top‑to‑bottom execution

Only integers allowed

No variables

No loops

No conditionals

No functions

Error Handling
The interpreter halts on:

Negative wait times

Negative signal values

Unknown commands

Invalid or missing arguments

Running Tick Programs
From the project root:

Code
python3 main.py path/to/program.tick
Example:

Code
python3 main.py tests/valid.tick
