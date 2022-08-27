import ast

count = 0

with open('whiletest.py') as f:
    tree = ast.parse(f.read())  # parse the file

for node in ast.walk(tree):  # walk the tree
    if isinstance(node, ast.If) or isinstance(node, ast.While) or isinstance(node, ast.For):  # if the node is an If (or an If-else) 
        count+=1

complexity = count+1
print(complexity)