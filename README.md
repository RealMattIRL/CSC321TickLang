Tick is a minimal timed‑event scripting language designed for sequencing actions with precise timing. Programs execute strictly from top to bottom, making Tick suitable for simple and predictable timed behaviors.

Overview:
A Tick program is written as a sequence of commands, for example:

ping
wait 2
signal 5
flash

Each command executes in order. The "wait n" command advances the internal clock by n ticks. The language has no variables, no loops, and no branching, keeping behavior simple and easy to reason about.

Repository Structure:
CSC321TickLang/
main.py (entry point for running Tick programs)
pyproject.toml (project metadata)
uv.lock (dependency lock file)
src/ (core language implementation)
Parser.py
ParserOut.py
TempAST.py
Token.py
Lexer and helpers
tests/ (test suite)
valid.tick
valid2.tick
invalid.tick
testLexer.py
testParser.py
.idea/ (IDE configuration)

Language Features:
Supported commands:

wait n : delay the next action by n ticks (n must be non‑negative)

ping : emit a "ping" event

beep : emit a "beep" event

signal n : emit a numeric signal (n must be non‑negative)

flash : emit a "flash" event

Execution model:

Linear, top‑to‑bottom execution

Only integers allowed

No variables

No loops

No conditionals

No functions

Error handling:
The interpreter stops when encountering:

Negative wait times

Negative signal values

Unknown commands

Invalid or missing arguments

Running Tick Programs:
From the project root, run:

python3 main.py path/to/program.tick

Example:

python3 main.py tests/valid.tick
