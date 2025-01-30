def begruessung(name):  # SyntaxError: expected '('
    print(
        "Hallo, " + name  # NameError: name 'Name' is not defined. Did you mean: 'name'?
    )  # IndentationError: expected an indented block after function definition on line 1


def addiere_zahlen(a, b):  # SyntaxError: expected ':'
    ergebnis = a + b
    return (
        ergebnis  # NameError: name 'ergebis' is not defined. Did you mean: 'ergebnis'?
    )


def subtrahiere_zahlen(a, b):
    return a - b  # NameError: name 'c' is not defined ,  should be 'b'


def main():  # SyntaxError: expected ':'
    zahl1 = int(input("Gib eine Zahl ein: "))  #  convert to integer
    zahl2 = int(input("Gib eine weitere Zahl ein: "))  #  convert to integer

    summe = addiere_zahlen(
        zahl1, zahl2
    )  # Error: 'zahl1' and 'zahl2' are strings, not integers
    print(
        "Die Summe ist: ", summe
    )  # TypeError: can only concatenate str (not "int") to str. instead of "+"" we put ","

    differenz = subtrahiere_zahlen(
        zahl1, zahl2
    )  # Error: 'zahl1' and 'zahl2' are strings, not integers
    print(
        "Die Differenz ist: ", differenz
    )  # TypeError: can only concatenate str (not "int") to str. instead of "+"" we put ","

    begruessung("Max")


if __name__ == "__main__":  # Syntax error: Use '==' for comparison, not '='
    main()
