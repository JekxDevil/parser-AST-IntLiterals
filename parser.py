from ast import NodeVisitor, Constant, Module, parse


class NumLiteralVisitor(NodeVisitor):
    """Numeric Literal Visitor inherits from NodeVisitor defined in ast to traverse all nodes in code"""
    list_literals: list[Constant]

    def __init__(self):
        """Initializing list holding Numeric Literals as ast.Constants"""
        self.list_literals = []

    def visit_Constant(self, node: Constant) -> None:
        """override of superclass method, meant to traverse only constants"""
        if (not isinstance(node, Module) and not isinstance(node.value, bool) and
                isinstance(node.value, (int, float, complex))):
            self.list_literals.append(node)
        self.generic_visit(node)

    def __str__(self):
        """print literals found and stored in list in format"""
        text = f'Found {len(self.list_literals)} numeric literals.\n'
        for el in self.list_literals:
            text += f'Line {el.lineno}: {el.value}\n'
        return text


def main():
    filename = input('Type the file name path: ')
    try:
        with open(filename, encoding='utf-8') as file:
            code = file.read()
        node = parse(code)
        literals = NumLiteralVisitor()
        literals.visit_Constant(node)
        print(literals)
    except FileNotFoundError:
        print(f'Sorry, the file "{filename}" does not exist. Program termination.')


if __name__ == '__main__':
    main()
