import sys
from TempLexer import TempLexer
from Parser import Parser
from ParserOut import ParseOut

def main():
    if len(sys.argv) != 3 or sys.argv[1] != "parse":
        print("Usage: tick parse <file>")
        sys.exit(1)

    filepath = sys.argv[2]
    try:
        with open(filepath, 'r') as f:
            source = f.read()
    except FileNotFoundError:
        print(f"Error: file not found: {filepath}")
        sys.exit(1)

    try:
        tokens = TempLexer(source).tokenize()
        ast    = Parser(tokens).parse()
        ParseOut(ast)
    except SyntaxError as e:
        print(f"Parse error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()