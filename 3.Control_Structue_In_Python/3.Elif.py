operand_1=int(input('Enter Operand1: '))
operand_2=int(input('Enter Operand2: '))
operator=input('Enter the Operator (+,-,*,%): ')

#if (Test Expression : )
    #statement
#eleif(Test Expressn: )
    #statement
#....
#else
    #Statement
#Statement

if operator=='+':
    print(operand_1+operand_2)
elif operator=='-':
    print(operand_1-operand_2)
elif operator=='*':
    print(operand_1*operand_2)
elif operator=='/':
    print(operand_1/operand_2)
else:
    print('None')

print('Thanks')