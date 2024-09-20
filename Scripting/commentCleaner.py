import ast

def comment_out_non_methods(code):
    module = ast.parse(code)
    new_lines = []
    for node in module.body:
        if isinstance(node, ast.FunctionDef):
            new_lines.append(code.splitlines()[node.lineno-1:node.end_lineno])
        else:
            new_lines.append(['# ' + line for line in code.splitlines()[node.lineno-1:node.end_lineno]])
    return '\n'.join(line for lines in new_lines for line in lines)

# Example usage:
code = """
def foo():
    return 42

"""
print(comment_out_non_methods(code))