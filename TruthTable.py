#Truth Table Generator - www.101computing.net/truth-table-generator/

def truthTable(expression,inputs=2):
  print("Boolean Expression:")
  print("  X = " + expression.upper())
  expression = expression.lower()
  
  #replace Boolean Operators with bitwise operators
  expression = expression.replace("and","&")
  expression = expression.replace("xor","^")
  expression = expression.replace("or","|")
  expression = expression.replace("not","~")
  
  print("\nTruth Table:")
  if inputs==2:
    print("  -------------")
    print("  | A | B | X |")
    print("  -------------")
    
    for a in range(0,2):
      for b in range(0,2):
        x = eval(expression)
        print("  | " + str(a) + " | " + str(b) + " | " + str(x) + " |" )
        print("  -------------")
        
  elif inputs==3:
    print("  -----------------")
    print("  | A | B | C | X |")
    print("  -----------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          x = eval(expression)
          print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(x) + " |" )
          print("  -----------------")
    
  elif inputs==4:
    print("  ---------------------")
    print("  | A | B | C | D | X |")
    print("  ---------------------")
    
    for a in range(0,2):
      for b in range(0,2):
        for c in range(0,2):
          for d in range(0,2):
            x = eval(expression)
            print("  | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(d) + " | " + str(x) + " |" )
            print("  ---------------------")

##############################################

def shift(num, shift_by, direction):
    if direction == "left":
        result = num << shift_by
        print(f"{num} << {shift_by} = {result}")
        return result
    elif direction == "right":
        result = num >> shift_by
        print(f"{num} >> {shift_by} = {result}")
        return result
    else:
        print("Invalid direction. Please choose either 'left' or 'right'.")


##############################################

expression = "A AND NOT (B XOR C)"
truthTable(expression, 3)

num = 5
shift_by = 3

# Perform left shift
result = shift(num, shift_by, "left")

# Multiply by 2^n
multiplied = num * (2 ** shift_by)

# Check if they are equal
print(result == multiplied)  

num = 40
shift_by = 3

# Perform right shift
result = shift(num, shift_by, "right")

# Divide by 2^n
divided = num // (2 ** shift_by)

# Check if they are equal
print(result == divided)  


