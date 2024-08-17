Descrição

Este script Python foi criado para fins educacionais e demonstra como limpar o terminal após a leitura de um arquivo e exibição dos dados. O arquivo date.txt deve conter linhas no formato email;senha, e o script processa essas linhas, exibe o progresso com uma barra de progresso e, após a leitura, limpa o terminal.
Funcionalidade

    Leitura do Arquivo: O script lê o arquivo date.txt, que deve estar no mesmo diretório que o script. Cada linha é dividida em email e senha, que são armazenados em uma lista.

    Ordenação e Exibição: A lista de emails e senhas é ordenada e exibida no terminal com uma barra de progresso.

    Limpeza do Terminal: Após a leitura e exibição dos dados, o terminal é limpo. O script detecta automaticamente o sistema operacional e usa o comando apropriado (cls para Windows e clear para Linux).

    Tratamento de Erros: Caso o arquivo date.txt não seja encontrado, o script exibe uma mensagem de erro.

Uso

    Prepare o Arquivo: Crie um arquivo chamado date.txt no mesmo diretório que o script. O arquivo deve conter linhas no formato email;senha.

    Execute o Script: Execute o script com Python. O terminal exibirá uma barra de progresso e, após a conclusão, será limpo.
