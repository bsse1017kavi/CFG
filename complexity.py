import ast, astunparse, os

with open('whiletest.py') as f:
    tree = ast.parse(f.read())  # parse the file

def visit_FunctionDef(tree):
    for node in ast.walk(tree):
      if isinstance(node,ast.FunctionDef) :
        func_name = node.name 
        code = astunparse.unparse(node)
        try:
            with open("temp.py", "w") as f:
                f.write(code)
            with open('temp.py') as f1:
                tree1 = ast.parse(f1.read())
                printComplexity(tree1, func_name)
            f.close()
            f1.close()
            
        except FileNotFoundError:
          print("The 'docs' directory does not exist")

def printComplexity(tree, func_name):
    count = 0
    for node in ast.walk(tree):  # walk the tree  
        if isinstance(node, ast.If) or isinstance(node, ast.While) or isinstance(node, ast.For):  # if the node is an If (or an If-else) 
            count+=1

    print("Cyclomatic Complexity for function " + func_name + " is: " + str(count+1))

visit_FunctionDef(tree)

os.remove("temp.py")