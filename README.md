# Projeto Integrador - Fiberblu

Desenvolvimento do Projeto Integrador do Curso de Técnico em Desenvolvimento de Sistemas para a Internet Integrado ao Ensino Médio do IFC - Campus Araquari.

Alunos: [Larissa Cristina Bileski](github.com/larissabileski) e [Vinicius Henrique da Silva](github.com/viniihds). 

Professores: [Marco André Mendes](github.com/marcoandre).

Links do projeto:

-   [Documentação](github.com/larissabileski/pi-larissaevinicius.git)
-   [Backend](https://github.com/viniihds/backend-fiberblu)
-   [Web](https://github.com/viniihds/web-fiberblu.git)
-   [Mobile](https://github.com/larissabileski/mobile-fiberblu)

# Situação Problema

O sistema será desenvolvido para a empresa Fiberblu. Presente há 28 anos no mercado, é o maior comercio de tanques de fibra na região Sul do país. O dono, Odair, o gerente comercial, Ednilson, a diretora financeira, e os representantes da empresa, são os principais funcionários e os que terão acesso ao sistema.

Atualmente a empresa funciona da seguinte forma: o representante anota o pedido em uma planilha. Em seguida, o pedido é enviado por email e depois cadastrado no sistema. O sistema emite o relatório do pedido e avisa a equipe de estoque. No dia do carregamento, o sistema fatura o pedido, desconta do estoque e é emitido o boleto. Atualmente, no sistema utilizado, não há como fazer o pedido direto no sistema.  Além disso, o sistema também não emite o boleto diretamente para o cliente, nem avisa se o boleto está vencendo ou se foi pago.

Notamos a falta de alguns recursos no atual software utilizado pela empresa, como por exemplo: O sistema não envia nem notifica o cliente em relação ao boleto, seja para avisar sobre o prazo do pagamento ou eventual vencimento. Outra dificuldade que percebemos foi que o sistema não tem uma opção para fazer pedidos. O cliente faz o pedido por uma planilha, envia por e-mail, e os administradores do sistema precisam registrar o pedido.

# Descrição da proposta

No sistema desenvolvido, será possível: acessar o relatório de vendas, cadastrar novas vendas, controlar o estoque, gerenciar ganhos e despesas, cota de representantes, emitir boletos após o faturamento dos pedidos e enviar mensagens automáticas.

O acesso ao sistema será restrito ao dono, ao gerente comercial, ao diretor financeiro e aos representantes da empresa.

O dono terá acesso a todas as ações do software. 

O gerente comercial terá acesso ao relatório e histórico de vendas, ao cadastro de novas vendas, ao controle de estoque e ao controle de ganhos e despesa. 

O diretor fincanceiro terá acesso ao relatório e histórico de vendas, ao gerenciamento de ganhos e despesas e as emissões de boletos. 

Por fim, os representantes terão acesso ao estoque, ao cadastro de novas vendas e aos pedidos efetuados no sistema.

# Regras de negócio

- **RN01 - Requisito do Cliente**: Apenas pessoas jurídicas podem efetuar pedidos.
- **RN02 – Inserir Produtos no Pedido**: Para inserir um produto no pedido, é necessário que o produto esteja cadastrado no sistema e que a quantia comprada seja acima de zero.
- **RN03 - Valor Minimo do Pedido**: Só serão efetuados pedidos acima de R$ 1.000,00.
- **RN04 - Cadastro do Pedido**: Para o pedido ser cadastrado no sistema, ele deve ser realizado por um representante da empresa ou pelo gerente comercial. 
- **RN06 - Controle do Estoque**: O produto é descontado do estoque apenas no dia do carregamento.
- **RN07 - Envio do Pedido**: O pedido só é enviado após o faturamento do pedido.
- **RN08 - Relatório de Vendas**: Só terão acesso ao relatório de vendas o dono, o gerente comercial e o diretor financeiro.
- **RN09 - Cota para Representantes Novos**: A cota para novos representantes é de 50 peças por mês.
- **RN10 - Cota para Representantes Antigos**: Para representantes antigos a cota é de 15% a mais do que o vendido no mesmo mês do ano anterior.
- **RN11 - Produto em Estoque**: Para o pedido ser efetuado, a quantidade de produtos selecionados pelo cliente deve estar em estoque. 
  
# Requisitos funcionais

**Entradas:**
- **RF01 - Registro de Usuário**: O usuário deve ser cadastrado pela sua função, para ter acesso a determinadas telas.
  - **Dados necessários:** nome, email, telefone, login, senha e nível de permissão. 
  - **Usuários:** todos os níveis de usuário.
- **RF02 - Registro de Produto**: No cadastro do produto deverá ser informado o código do produto, sua cor, material, tamanho e valor.
  - **Dados necessários:** código do produto, cor, material, tamanho e valor.
  - **Usuários:** gerente comercial.
- **RF03 - Registro do Cliente**: No cadastro do cliente deverá ser informado os dados do cliente.
  - **Dados necessários:** CNPJ do cliente, nome, email, telefone e endereço.
  - **Usuários:** gerente comercial.
  
**Processos:**
- **RF04 - Autenticação de Usuário**: O usuário deve ter o acesso ao sistema autenticado, para verificação das telas disponiveis para acesso conforme sua função.
  - **Dados necessários:** login, senha e nível de permissão. 
  - **Usuários:** todos os níveis de usuário.
- **RF05 - Registro de Pedido**: O pedido deve ser cadastrado identificando o CNPJ da empresa, produtos selecionados, valor do pedido e vendedor que efetuou o pedido.
  - **Dados necessários:** CNPJ da empresa, produtos selecionados, valor do pedido, quantidade e vendedor que efetuou o pedido.
  - **Usuários:** representantes da empresa.

**Saídas:**
- **RF06 - Relatório e histórico de vendas**: Após cada pedido efetuado, o sistema deve manter um relatório da venda, e inclui-la no histórico de vendas.
  - **Dados necessários:** código do pedido, valor do pedido, horário que o pedido foi enviado para a entrega, cliente e vendedor que efetuou o pedido.
  - **Usuários:** gerente comercial.

# 6. Requisitos não funcionais

- **RNF01 - Segurança**: O software terá diferentes tipos de acesso para cada tipo de login, tendo as permissões ideais a função de cada um.
- **RNF02 - Atuação**: O sistema deve ser capaz de lidar com o número necessário de usuários sem qualquer degradação no desempenho.
- **RNF03 - Escalabilidade**: O sistema deve ser capaz de aumentar ou diminuir conforme necessário.
- **RNF04 - Disponibilidade**: O sistema deve estar disponível quando necessário.
- **RNF05 - Manutenção**: O sistema deve ser fácil de manter e atualizar.
- **RNF06 - Portabilidade**: O sistema deve ser capaz de rodar em diferentes plataformas com alterações mínimas.
- **RNF07 - Confiabilidade**: O sistema deve ser confiável e atender aos requisitos do usuário.
- **RNF08 - Usabilidade**: O sistema deve ser fácil de usar e entender.
- **RNF09 - Compatibilidade**: O sistema deve ser compatível com outros sistemas.
- **RNF10 - Conformidade**: O sistema deve cumprir todas as leis e regulamentos aplicáveis.
- **RNF11 - Navegadores homologados**: Navegadores homologados: o sistema deverá ser homologado para os navegadores Google Chrome e Mozilla Firefox. 
- **RNF012 - Tecnologia Front-end**: Para a exibição em front-end, o software utilizará o CSS3 e o HTML5, além dos frameworks Vue.js para conteúdo HTML responsivo e React Native para mobile.
- **RNF13 - Tecnologia Back-end**: O software será desenvolvido utilizando o framework Django, gerando uma API Rest com o Django Rest Framework.
- **RNF14 - Forma de uso do software**: O sistema por fazer parte de um ambiente interno, provavelmente será utilizado de acordo com as horas de trabalho da empresa, mas estará ativo 24 horas por dia em 7 dias por semana.
- **RNF15 - Desempenho**: Para a utilização correta e com uma qualidade e eficiência melhor, é recomendado que se use o Sistema Operacional mais atualizado.
- **RNF16 - Autenticação**: Para realizar o acesso ao sistema é necessário ter um usuário de autenticação criado pelo administrador, além da possibilidade de solicitar um envio de redefinição de senha.
- **RNF17 - Legais**: O sistema deve atender às exigências da LGPD (Lei Geral da Proteção de Dados).

