def validaCPF(cpf):
    while cpf!=1:
        if cpf.isnumeric() and len(cpf)==11:
            valida=int(cpf[0])*10+int(cpf[1])*9+int(cpf[2])*8+int(cpf[3])*7+int(cpf[4])*6+int(cpf[5])*5+int(cpf[6])*4+int(cpf[7])*3+int(cpf[8])*2
            aux=(valida*10)%11
            if(aux==int(cpf[9])):
                valida=int(cpf[0])*11+int(cpf[1])*10+int(cpf[2])*9+int(cpf[3])*8+int(cpf[4])*7+int(cpf[5])*6+int(cpf[6])*5+int(cpf[7])*4+int(cpf[8])*3+int(cpf[9])*2
                aux=(valida*10)%11
                if(aux==int(cpf[10])):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False