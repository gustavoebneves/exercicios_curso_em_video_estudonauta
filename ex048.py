idade = int(input('Insira sua idade: '))

if 9 >= idade >= 5:
    print('\033[36mMIRIM')
elif 14 >= idade > 9:
    print('\033[35mINFANTIL')
elif 19 >= idade > 14:
    print('\033[34mJÚNIOR')
elif 20 >= idade > 19:
    print('\033[34mSÊNIOR')
elif idade > 20:
    print('\033[33mMASTER')
