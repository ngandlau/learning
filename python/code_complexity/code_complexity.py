import ast
from typing import Dict
from radon.complexity import cc_visit
from cognitive_complexity.api import get_cognitive_complexity
import typer
from rich.table import Table
from rich.console import Console

app = typer.Typer(add_completion=False)

def get_source_code(filename: str) -> str:
    with open(filename, 'r') as file:
        source_code = file.read()
    return source_code

def calculate_cyclomatic_complexity(source_code: str) -> Dict[str, int]:
    """Calculates Cyclomatic Complexity for each function in the source code"""
    functions = cc_visit(source_code)
    function_complexities = {func.name: func.complexity for func in functions}
    return function_complexities

def count_lines_of_code(node: ast.AST) -> int:
    start_line = node.lineno
    end_line = node.end_lineno
    num_lines = end_line - start_line + 1
    return num_lines

def count_number_of_function_arguments(node: ast.AST) -> int:
    return len(node.args.args)


def get_complexity_of_functions(filename):
    source_code = get_source_code(filename)
    tree = ast.parse(source_code)
    
    function_info = {}

    cyclomatic_complexities = calculate_cyclomatic_complexity(source_code)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            num_lines = count_lines_of_code(node)
            num_args = count_number_of_function_arguments(node)
            cognitive_complexity = get_cognitive_complexity(node)

            function_info[node.name] = {
                "lines": num_lines,
                "arguments": num_args,
                "cyclomatic_complexity": cyclomatic_complexities[node.name],
                "cognitive_complexity": cognitive_complexity,
            }

    return function_info

def make_table_from_dict(function_info) -> Table:
    table = Table()
    table.add_column('function')
    table.add_column('cognitive_complexity')
    table.add_column('cyclomatic_complexity')
    table.add_column('lines')
    table.add_column('arguments')

    for function_name, function_metrics in function_info:
        table.add_row(
            function_name, 
            str(function_metrics['cognitive_complexity']), 
            str(function_metrics['cyclomatic_complexity']), 
            str(function_metrics['lines']), 
            str(function_metrics['arguments'])
        )

    return table

def sort_by_metric(function_info, metric: str = 'cognitive_complexity'):
    return sorted(function_info.items(), key=lambda x: -x[1][metric])


@app.command()
def main(path: str, metric: str = 'cognitive_complexity'):
    function_info = get_complexity_of_functions(path)
    sorted_function_info = sort_by_metric(function_info, metric)
    # sorted_function_info = sorted(function_info.items(), key=lambda x: (-x[1]['cognitive_complexity'], -x[1]['cyclomatic_complexity'], -x[1]['lines'], -x[1]['arguments']))
    Console().print(make_table_from_dict(sorted_function_info))

if __name__ == "__main__":
    app()

