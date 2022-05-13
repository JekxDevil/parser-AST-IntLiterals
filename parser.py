import ast


class NumLiteralVisitor(ast.NodeVisitor):
    list_literals: list[ast.Constant]

    def __init__(self):
        self.list_literals = []

    def visit_Constant(self, node: ast.Constant) -> None:
        if (not isinstance(node, ast.Module) and not isinstance(node.value, bool) and
                isinstance(node.value, (int, float, complex))):
            self.list_literals.append(node)
        self.generic_visit(node)

    def __str__(self):
        text = f'Found {len(self.list_literals)} numeric literals.\n'
        for el in self.list_literals:
            text += f'Line {el.lineno}: {el.value}\n'
        return text


def main():
    filename = input('Type the file name path: ')
    try:
        with open(filename, encoding='utf-8') as file:
            code = file.read()
        node = ast.parse(code)
        literals = NumLiteralVisitor()
        literals.visit_Constant(node)
        print(literals)
    except FileNotFoundError:
        print(f'Sorry, the file "{filename}" does not exist. Program termination.')


if __name__ == '__main__':
    main()
