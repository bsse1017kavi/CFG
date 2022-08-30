import ast, astunparse, os

def calculate_LOC(inputFile):
    loc = 0
    number_of_commented_lines = 0
    number_of_blank_lines = 0

    f = open(inputFile)
    for line in f:
        loc += 1

        processed_line = line.strip()

        if processed_line == "":
            number_of_blank_lines += 1

        elif processed_line.startswith('#'):
            number_of_commented_lines += 1

    f.close()

    print('Total lines (LOC): ' + str(loc))
    print('Commented lines: ' + str(number_of_commented_lines))
    print('Blank lines: ' + str(number_of_blank_lines))
    print('Executable lines(ELOC): ' + str(loc - (number_of_commented_lines + number_of_blank_lines)))

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

print('---------------Cyclomatic Complexities---------------')

with open('whiletest.py') as f:
    tree = ast.parse(f.read())  # parse the file

visit_FunctionDef(tree)
os.remove("temp.py")

print('\n')

print('---------------Summary about Lines of Code---------------')
calculate_LOC('whiletest.py')