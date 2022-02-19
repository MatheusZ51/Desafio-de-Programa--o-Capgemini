senha = str(input("Digite sua senha: ")).strip()
t = len(senha)
c = 6-t
flag = 0
l, u, p, d = 0, 0, 0, 0

if t>=6:
    print("1-Sua senha tem o número mínimo de caracters necessario (possui {} caracters)".format(t))
else:
    print("1-Você deve adicionar {} caracters para fortalecer sua senha".format(c))
if (len(senha) >= 6):
    for i in senha:
        if (i.islower()):
            l+=1
        if (i.isupper()):
            u+=1
        if (i.isdigit()):
            d+=1
        if(i=='@'or i=='$' or i=='_' or i=='#' or i=='%' or i=='^' or i=='&' or i=='!' or i=='*' or i=='(' or i==')' or i=='-' or i== '+' or i=='{' or i=='}' or i=='[' or i==']'):
            p+=1
if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(senha)):
    print("2-Sua senha é forte!")
else:
    print("2-sua senha não é forte, ela deve conter no mínimo: ")
    print("6 caracters")
    print("1 digito")
    print("1 letra maiúscula")
    print("1 letra minúscula")
    print("1 caracter especial (os caracteres especiais são: !@#$%^&*()[]{}-+")
