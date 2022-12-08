print("\nSe existe 1 pasta DADOS, digite 2. Se existe 3 pastas DADOS, digite 4. Sempre digite o número sucessor de pastas existentes.\n")
nump=int(input("Qual o número da pasta dessa vez? "))
while nump<=1000:    
    i=1
    while i<1000:
        opcao=int(input("=========MENU=========\n1-Cadastrar\n2-Ler\n3-Deletar\n4-Atualizar\n5-Sair\nDigite a opção: "))
        print("======================")
        if opcao==1:
            nome=input("\n======================\nDigite seu nome: ")
            arquivo = open('Nome.txt', 'w')
            arquivo.write("Nome: %s" %nome)
            arquivo.close()
                
            cpf=input("Digite seu CPF: ")
            arquivo = open('CPF.txt', 'w')
            arquivo.write("CPF: %s" %cpf)
            arquivo.close()
                
            email=input("Digite seu email: ")
            arquivo = open('Email.txt', 'w')
            arquivo.write("Email: %s" %email)
            arquivo.close()
                
            senha=input("Digite sua senha: ")
            arquivo = open('Senha.txt', 'w')
            arquivo.write("Senha: %s" %senha)
            arquivo.close()
                
            user=input("Digite seu usuário: ")
            arquivo = open('Usuário.txt', 'w')
            arquivo.write("Usuário: %s" %user)
            arquivo.close()
                
            conf=int(input("1-Sim\n2-Não\nConfirmar os dados? "))
            if conf!=1:
                print("Refaça seus dados!")
                arquivo = open('Nome.txt', 'w')
                arquivo.close()
                arquivo = open('CPF.txt', 'w')
                arquivo.close()
                arquivo = open('Email.txt', 'w')
                arquivo.close()
                arquivo = open('Senha.txt', 'w')
                arquivo.close()
                arquivo = open('Usuário.txt', 'w')
                arquivo.close()
            if conf==1:
                print("Dados confirmados!")
                
        if opcao==2:
            arquivo = open('Nome.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('CPF.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('Email.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('Senha.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('Usuário.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
        
        if opcao==3:
            arquivo = open('Nome.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('CPF.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('Email.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('Senha.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('Usuário.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            delet1=int(input("1-Nome\n2-CPF\n3-Email\n4-Senha\n5-Usuário\n6-Todos os dados\nQual campo você deseja deletar? "))
            if delet1==1:
                arquivo = open('Nome.txt', 'w')
                arquivo.write("Nome: SEM NOME!")
                arquivo.close()
                
            elif delet1==2:
                arquivo = open('CPF.txt', 'w')
                arquivo.write("CPF: SEM CPF!")
                arquivo.close()
                
            elif delet1==3:
                arquivo = open('Email.txt', 'w')
                arquivo.write("Email: SEM EMAIL!")
                arquivo.close()
                
            elif delet1==4:
                arquivo = open('Senha.txt', 'w')
                arquivo.write("Senha: SEM SENHA!")
                arquivo.close()
                
            elif delet1==5:
                arquivo = open('Usuário.txt', 'w')
                arquivo.write("Usuário: SEM USUÁRIO!")
                arquivo.close()
            #=====================================================================   
            elif delet1==6:
                arquivo = open('Nome.txt', 'w')
                arquivo.write("Nome: SEM NOME!")
                arquivo.close()
                
                arquivo = open('CPF.txt', 'w')
                arquivo.write("CPF: SEM CPF!")
                arquivo.close()
                
                arquivo = open('Email.txt', 'w')
                arquivo.write("Email: SEM EMAIL!")
                arquivo.close()
                
                arquivo = open('Senha.txt', 'w')
                arquivo.write("Senha: SEM SENHA!")
                arquivo.close()
                
                arquivo = open('Usuário.txt', 'w')
                arquivo.write("Usuário: SEM USUÁRIO!")
                arquivo.close()
                
            else:
                print("Digite uma opção válida!")
                
        if opcao==4:
            arquivo = open('Nome.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('CPF.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('Email.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('Senha.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            arquivo = open('Usuário.txt', 'r')
            primeira_linha = arquivo.readline()
            print(primeira_linha)
            
            atu1=int(input("1-Nome\n2-CPF\n3-Email\n4-Senha\n5-Usuário\n6-Todos os dados\nQual campo você deseja atualizar? "))
            if atu1==1:
                nome=input("\n======================\nDigite seu novo nome: ")
                arquivo = open('Nome.txt', 'w')
                arquivo.write("Nome: %s" %nome)
                arquivo.close()
                
            elif atu1==2:
                cpf=input("Digite seu novo CPF: ")
                arquivo = open('CPF.txt', 'w')
                arquivo.write("CPF: %s" %cpf)
                arquivo.close()
                
            elif atu1==3:
                email=input("Digite seu novo email: ")
                arquivo = open('Email.txt', 'w')
                arquivo.write("Email: %s" %email)
                arquivo.close()
            
            elif atu1==4:
                senha=input("Digite sua nova senha: ")
                arquivo = open('Senha.txt', 'w')
                arquivo.write("Senha: %s" %senha)
                arquivo.close()
                
            elif atu1==5:
                user=input("Digite seu novo usuário: ")
                arquivo = open('Usuário.txt', 'w')
                arquivo.write("Usuário: %s" %user)
                arquivo.close()
            #=====================================
            elif atu1==6:
                nome=input("\n======================\nDigite seu novo nome: ")
                arquivo = open('Nome.txt', 'w')
                arquivo.write("Nome: %s" %nome)
                arquivo.close()
                
                cpf=input("Digite seu novo CPF: ")
                arquivo = open('CPF.txt', 'w')
                arquivo.write("CPF: %s" %cpf)
                arquivo.close()
                
                email=input("Digite seu novo email: ")
                arquivo = open('Email.txt', 'w')
                arquivo.write("Email: %s" %email)
                arquivo.close()
                
                senha=input("Digite sua nova senha: ")
                arquivo = open('Senha.txt', 'w')
                arquivo.write("Senha: %s" %senha)
                arquivo.close()
                
                user=input("Digite seu novo usuário: ")
                arquivo = open('Usuário.txt', 'w')
                arquivo.write("Usuário: %s" %user)
                arquivo.close()
                
            else:
                print("Digite uma opção inválida")
                
        elif opcao==5:
            sair=int(input("1-Sim\n2-Não\nDeseja sair? "))
            if sair==2:
                print("Voltando ao menu...")
            elif sair==1:
                confs=int(input("======================\n1-Sim\n2-Não\nDeseja salvar os dados antes de sair? "))
                if confs==1:
                    import os
                    os.mkdir('Dados %i' %nump)
                    import os
                    os.rename('Nome.txt', 'Dados %i/Nome.txt' %nump)
                    os.rename('CPF.txt', 'Dados %i/CPF.txt' %nump)
                    os.rename('Email.txt', 'Dados %i/Email.txt' %nump)
                    os.rename('Senha.txt', 'Dados %i/Senha.txt' %nump)
                    os.rename('Usuário.txt', 'Dados %i/Usuário.txt' %nump)
                    nump=nump+1
                    print("Dados salvos!")
                else:
                    print("Saindo e apagando...")
                    
                    arquivo = open('Nome.txt', 'w')
                    arquivo.close()
                
                    arquivo = open('CPF.txt', 'w')
                    arquivo.close()
                
                    arquivo = open('Email.txt', 'w')
                    arquivo.close()
                
                    arquivo = open('Senha.txt', 'w')
                    arquivo.close()
                
                    arquivo = open('Usuário.txt', 'w')
                    arquivo.close()