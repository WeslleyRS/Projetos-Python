print ('Hello, World!') # O mais importante é se livrar da maldição logo de cara LOL

apresentasao = input ('Olá, seja Bem-Vindo ao meu primeiro sistema. aqui irei abordar algumas variaveis basicas, então coletarei alguns dos seus dados tudo bem ?')

maioridade = input ('Para o inicio da coleta de informações preciso saber se você é maior de idade, você possuí mais de 18 anos ?')

nome = input ('Para começar coletarei as informações padrões para que eu possa falar com você de uma maneira mais adequada, então, Qual é o seu Nome ?')

nomeconfirma = input (f'Resposta captada com sucesso, para confirmar, seu nome é {nome} correto ?')

nasçimento = input (f'Agora preciso que me forneça sua data de nasçimento {nome}:')

confirmasao = input (f'Agora para finalizar nossa informações coletada preciso que verifique se as seguinte informações estão corretas: Seu nome é {nome} e você nasceu em {nasçimento}, correto ?')

if nasçimento >= '2005':
    print (f'Seu acesso foi aprovado com sucesso {nome}!')
else:
    print ('Seu acesso foi negado, sinto muito...')

# o codigo está pronto, sei que muitos viram que possui uma falha de segurança no software, a questão da idade, o usuario pode mentir para o sistema e obter acesso.
# como este a um script inicial que desenvolvi não irei me preocupar com isso pois ele n saira de lugar algum, porem desde já devemos sempre nos atentar as falhas de segurança em nossos codigos :)