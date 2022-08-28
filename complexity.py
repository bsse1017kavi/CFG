import ast

flag = False
count = 0
current_func = ''

with open('whiletest.py') as f:
    tree = ast.parse(f.read())  # parse the file

for node in ast.walk(tree):  # walk the tree
    if isinstance(node, ast.FunctionDef):
        if not flag:
            current_func = str(node.name)
            flag = True
        else:
            print("Cyclometric Complexity for function " + current_func + " is: " + str(count+1))
            current_func = str(node.name)
            count = 0      

    if isinstance(node, ast.If) or isinstance(node, ast.While) or isinstance(node, ast.For):  # if the node is an If (or an If-else) 
        count+=1

print("Cyclometric Complexity for function " + current_func + " is: " + str(count+1))