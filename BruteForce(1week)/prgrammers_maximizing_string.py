from itertools import permutations

max_val = float("-inf")

def operation(op,num1,num2) :
    if op == "+" :
        return num1+num2
    elif op == "-" :
        return num1-num2
    elif op == "*" :
        return num1*num2
    
    
def cal(op,expression) :
    global max_val
    
    expression = expression.replace("+"," + ").replace("-"," - ").replace("*"," * ").split(" ")
       
    val = 0
  
    op_index = [0+i for i in range(len(op))]
    op_index = sorted(op_index, reverse=True)    
    op_compare = dict(zip(op,op_index))
    
    stack_op = []
    stack_num = []
    
    
    for s in expression :
        if s in op :
            if not stack_op :
                stack_op.append(s)
            else :
                stack_op_top = stack_op[-1]
                if op_compare[s] > op_compare[stack_op_top] :
                    stack_op.append(s)
                else :
                    while stack_op and op_compare[s] <= op_compare[stack_op[-1]]  :
                        stack_op_top = stack_op.pop()
                        num1 = stack_num.pop()
                        num2 = stack_num.pop()
                        result = operation(stack_op_top,num2,num1)
                        stack_num.append(result) 
                    stack_op.append(s) 
        else :
            stack_num.append(int(s))
    
     
    
    while stack_op :
        top = stack_op.pop()
        num1 = stack_num.pop()
        num2 = stack_num.pop()
        result = operation(top,num2,num1)
        stack_num.append(result)
    
        
    m = stack_num[0]
    max_val = max(abs(m),max_val)
            
def solution(expression):
    answer = 0
    
    operation = []
    
    for c in expression :
        if c == "+" or c == "-" or c == "*" :
            if c not in operation :
                operation.append(c)
    
    operation_subset = list(permutations(operation))
    
    for op in operation_subset :
        cal(op,expression)
    
    answer = max_val
    
    return answer