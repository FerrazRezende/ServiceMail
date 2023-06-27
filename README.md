# **ServiceMail**

### *API de envio de e-mail feito em FastAPI (Python)*
---
<br>

# **Introdução**
Olá, seja bem-vindo! Este é um projeto simples, aberto, com um objetivo didático e de uso livre. Apresentamos o ServiceMail, uma API desenvolvida para facilitar o envio de e-mails, permitindo que você utilize dados recebidos por meio do método POST.

Neste tutorial, você aprenderá como instalar, configurar e utilizar a API, desfrutando de suas funcionalidades de envio de e-mail de forma prática e eficiente.

Vamos começar!


## **Sumário**
---
<ol>
<li><b>Configuração:</b>
    <ol>
    <li>Configurando a conta do Gmail;</li>
    <li>Inserindo informações da conta na aplicação.</li>
    </ol>
</li>
<li><b>Instalação:</b>
    <ol>
    <li>Instalando com pip;</li>
    <li>Instalando com Docker.</li>
    </ol>
</li>
<li><b>O modelo de e-mail:</b>
    <ol>
    <li>Métodos da classe e-mail;</li>
    <li>Validação de e-mail;</li>
    </ol>
</li>
<li><b>Mail.html:</b>
    <ol>
    <li>O arquivo mail.html.</li>
    </ol>
</li>
<li><b>Rotas:</b>
    <ol>
    <li>Rota root;</li>
    <li>Rota /enviar_email</li>
    </ol>
</li>
<li><b>Testando a API:</b>
    <ol>
    <li>Testando no /docs do FastAPI;</li>
    <li>Testando no PostMan.</li>
    </ol>
</li>
<li><b>Consumindo API:</b>
    <ol>
    <li>Consumindo API com JS.</li>
    </ol>
</li>
<li><b>DockerFile</b></li>
<li><b>Considerações finais</b></li>
</ol>

----
<br>

# **Configuração**
## **Configurando a conta do Gmail**

O servidor ao qual a aplicação se conecta para enviar e-mails é o servidor do Gmail (587). Devido à política do Google em relação ao [gerenciamento de apps e serviços de terceiros com acesso à sua conta](https://support.google.com/accounts/answer/3466521?hl=pt-BR), **é necessário seguir alguns passos para que a aplicação consiga se conectar corretamente com a sua conta**: 

### **1° Passo**
Entre em "Gerenciar sua Conta do Google":

<img src="https://i.ibb.co/MPmVJqH/5.png">

<br>

No canto lateral esquerdo, clique em "Segurança":

<img src="https://i.ibb.co/vVKdPY6/10.png">

<br>

> Na próxima etapa você precisará ativar a verificação em duas etapas.

<br>

Com a verificação em duas etapas ativada, pesquise por senha de apps.

<br>

<img src="https://i.ibb.co/GVrmgRx/image.png">

<br>

Selecione o app 'Mail':

<img src="https://i.ibb.co/cLWj37P/12.png">

<br>

Em dispositivo, selecione "Outro Dispositivo" para escolher um nome personalizado para esta senha.

<br>

<img src="https://i.ibb.co/wyw2kTb/image.png">

<br>

> Não se preocupe com a confidencialidade desta senha; ela não concede acesso à sua conta do Google e pode ser excluída a qualquer momento.

<br>

<img src="https://i.ibb.co/9cXs4WT/image.png">
<br>
<br>

## Inserindo a senha gerada na aplicação:

Abra o arquivo main.py e procure por "senha_de_envio" na linha 87:

<img src="https://i.ibb.co/X8pkdBB/image.png">

<br> 

Ficará assim: 

<img src="https://i.ibb.co/dD7SwfB/image.png">

<br>

## **Feito essas etapas, você estará pronto para iniciar a instalação!**

<br>

# **Instalação**
## **Instalando com pip**

Para iniciar a instalação com o pip, primeiro você precisa criar um ambiente virtual do Python. Isso pode ser feito seguindo os passos abaixo:

No terminal, dentro da pasta do projeto, digite o seguinte comando:

``` Python
python -m venv venv 
```

Sendo o último **"venv"**, o nome do nosso ambiente virtual. 

Será criado um diretório com o nome do ambiente virtual.

<img src="https://i.ibb.co/5FKr1n0/image.png">
<br>

Com o diretório criado, inicie o ambiente virtual:

No Linux/Mac:

``` Python
. venv/bin/activate
```
No Windows:
``` Python
. venv/Scripts/activate
```

Deverá ficar assim: 

<img src="https://i.ibb.co/VmS3Z14/image.png">

<br>

Com o ambiente virtual ativado, digite o seguinte comando no terminal:

```
pip install -r requirements.txt
```

O comando acima irá instalar os pacotes descritos no arquivo "requirements.txt"

<img src="https://i.ibb.co/nsBCfJw/image.png">
<img src="https://i.ibb.co/N93KKNP/image.png">
<br>
<hr>

## **Instalando com Docker**

Para instalar usando o Docker, o processo é simplificado. Faremos a instalação da imagem do projeto por meio de um Dockerfile. 

<img src="https://i.ibb.co/bdTS8qF/image.png">

O processo de instalação no Docker é padronizado independentemente do Sistema Operacional, por isso tendo o [Docker](https://docs.docker.com/get-docker/) instalado em seu computador, execute o seguinte comando no terminal:

```
docker build -t usuario/nome_da_imagem:1v0 .
```

**Substitua "usuario/nome_da_imagem" pelo seu nome de usuário e pelo nome da imagem que preferir. No meu caso, usarei** "matheusferraz/servicemail:1v2."

Certifique-se de incluir o ponto "." no final do comando para que a imagem seja construída a partir do Dockerfile no diretório atual em que o terminal está localizado.

<img src="https://i.ibb.co/T0XMhhX/image.png">
<img src="https://i.ibb.co/4FJLGnm/image.png">

<br>

Com a imagem criada, execute-a na porta 8080: 

```
docker run -d -p 8080:80 matheusferraz/servicemail:1v2
```

<img src="https://i.ibb.co/M9kdVXk/image.png">

<br>

Feito isso, será possível acessar a API através do link: *_localhost:8080_*, a resposta deverá ser algo como:

<img src="https://i.ibb.co/0VJnn23/image.png">

<hr>

<br>

# **O modelo de E-mail**

## **Os métodos da classe E-mail**

Para controlar os dados que chegam na API, usaremos um modelo do [Pydantic](https://fastapi.tiangolo.com/tutorial/sql-databases/?h=pydantic#use-pydantics-orm_mode). Este modelo será responsável para receber os destinatários e o assunto do e-mail.

```python
class Email(BaseModel): 
    destinatarios: List[str]
    assunto: str
```

O método 'destinatarios' é responsável por receber os e-mails dos destinatários.
> Devido a ser do tipo Lista (List), é possível disparar o mesmo e-mail para múltiplos destinatários.

O método 'assunto' define o assunto do e-mail enviado.

## **Validação de e-mail**

Para evitar que erros sejam provocados intencionalmente, prejudicando a segurança da API, inseri uma [validação](https://docs.pydantic.dev/latest/usage/validators/) para os e-mails recebidos no campo destinatários.

``` python
    @validator('destinatarios')
    def valida_email(cls, v):
        if isinstance(v, list) and len(v) == 1:
            v = v[0]  # Obter o valor de e-mail da lista
            if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+').match(v):
                raise ValueError('O e-mail está inválido!')
            return v
```
>A função validator é um [decorator](https://pythoniluminado.netlify.app/decoradores) fornecido pelo Pydantic que permite adicionar validações personalizadas aos campos de uma classe de modelo.

No código fornecido, o decorator @validator é usado para aplicar a validação ao campo "destinatarios". Os argumentos fornecidos ao decorador são:

<ul>
    <li>
        def valida_email(cls, v): Este é o método que realiza a validação do e-mail. Ele recebe dois parâmetros: cls, que se refere à própria classe, e v, que é o valor do campo 'destinatarios'.
    </li>
    <br>
    <li>
        A condição if isinstance(v, list) and len(v) == 1 verifica se o valor do campo destinatarios é uma lista com apenas um elemento. Se essa condição for verdadeira, o código prossegue com a validação do primeiro elemento da lista como um endereço de e-mail.
        <br><br>
        No entanto, se a condição não for atendida, o código simplesmente retorna o valor original sem fazer nenhuma modificação. Portanto, essa implementação não valida múltiplos e-mails, apenas considera o primeiro elemento da lista, se houver, como um possível endereço de e-mail a ser validado.
    </li>
    <br>
    <li>
        v = v[0]: Se o valor do campo 'destinatarios' for uma lista com um único elemento, essa linha extrai o valor do e-mail da lista e o atribui à variável 'v'. Isso é feito porque o código espera um único valor de e-mail para validar.
    </li>
    <br>
    <li>
        if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+').match(v) utiliza uma expressão regular para verificar se o valor do e-mail (v) corresponde ao padrão esperado.
        <br><br>
        A expressão regular valida o formato básico de um endereço de e-mail, verificando se ele contém letras, números, pontos, traços e sublinhados nos locais corretos. Se o valor não corresponder ao padrão, a condição if not será verdadeira, indicando que o e-mail está inválido.
        <br><br>
        Portanto, se o valor do e-mail não corresponder ao padrão definido pela expressão regular, será levantada uma exceção ValueError com a mensagem 'O e-mail está inválido!'. Isso significa que o e-mail fornecido não está em um formato válido de acordo com o padrão definido na expressão regular.
    </li>
    <br>
    <li>
        return v: Se o valor de e-mail passar por todas as validações anteriores, ele é considerado válido e é retornado pelo método.
    </li>
    <br>

> Por enquanto a validação não funciona para múltiplos e-mails.

<hr>
<br>

# **Mail.html**

## **O arquivo mail.html**
<img src="https://i.ibb.co/hBMf6VW/image.png" width="200">

>O arquivo mail.html é o corpo do e-mail, contendo o conteúdo que os destinatários receberão.

A função principal de um arquivo HTML como corpo de e-mail é permitir a criação de um layout personalizado, que pode incluir texto formatado, imagens, links e até mesmo elementos interativos, como botões e formulários. Ao utilizar HTML, é possível controlar a aparência visual do e-mail, como fontes, cores, tamanhos de texto e alinhamento.

Abrindo o arquivo, você verá que os estilos estão sendo aplicados diretamente em suas respectivas tags, isso é porque a tag < style > **não é recomendada para ser usada diretamente no corpo do e-mail HTML**, a sua aplicação direta em e-mails pode não ser suportada corretamente por todos os clientes de e-mail.

 Há a opção de usar arquivos externos caso eles estejam hospedados em um servidor acessível e que os URLs estejam corretos e funcionais. Assim você consegue carregar estilos e imagens.
 ___
<br>

# **Rotas**

## **Rota root ("/")**

Get_root é uma rota GET que está configurada para a raiz ("/") do aplicativo.

Quando um cliente faz uma solicitação GET para a raiz da aplicação , a função get_root() é acionada. Ela retorna um dicionário contendo um único par chave-valor: {"mensagem": "On-line."}.

>Essa rota é útil para checar o status da API caso ela esteja rodando em um **servidor**.

<br>

## **Rota /enviar_email**
A rota "enviar_email" é responsável por receber os dados na requisição POST feita pelo cliente e enviar o e-mail com base nos dados recebidos. Pode-se observar que ela recebe o modelo "E-mail" como parâmetro, que são exatamente os parâmetros que serão passados ao consumir a API.

```python
async def enviar_email(email: Email):
```

Abaixo dessa função está toda a lógica por trás da API.

> É boa prática que a aplicação seja [refatorada](https://engsoftmoderna.info/cap9.html) para melhorar o desempenho.

<hr>
<br>

# **Testando a API**

> É importante saber que para testar a API, o servidor precisa estar em execução com a rota "/" devolvendo o resultado {"mensagem": "On-line"} na requisição GET.

<br>

## **Testando no /docs do FastAPI**
Uma das funcionalidades do FastAPI, é a documentação pronta que ele oferece. Para acessar no localhost acesse: localhost:8080/docs

<img src="https://i.ibb.co/pr4Jq8J/Whats-App-Image-2023-06-04-at-20-33-25.jpg">

<br>

Ao clicar em "Try it out" deveremos preencher o "Request body" com as informações que queremos colocar no e-mail.

<img src="https://i.ibb.co/RDHHkYk/image.png">

### Por fim, clicamos em "Execute" para fazer o envio do e-mail, no caso de sucesso, veremos a seguinte mensagem: 
<img src="https://i.ibb.co/drk6j9Y/image.png">

<hr>
<br>

## **Testando com Postman**

[Postman](https://www.postman.com/) é uma ferramenta de desenvolvimento de API que permite aos desenvolvedores testar, documentar e colaborar no desenvolvimento de APIs. Ele oferece uma interface gráfica intuitiva para enviar solicitações HTTP para APIs, realizar testes automatizados, organizar solicitações em coleções, gerar documentação interativa e facilitar a colaboração entre equipes de desenvolvimento.

> Para se aprofundar melhor na ferramenta Postman, recomendo que assista à videos no youtube e leia a [documentação](https://learning.postman.com/docs/introduction/overview/).

Apenas para testar a nossa API, o nosso uso será bem superficial:

<img src="https://i.ibb.co/ypf5qFf/image.png" width=550>

<br>

### **Caso o corpo do e-mail esteja preenchido corretamente e a API esteja online, a resposta que deve retornar do Postman é:**

<img src="https://i.ibb.co/KDw5kPv/image.png" width=550>

```
{
    "message": "E-mail enviado com sucesso!"
}
```

<hr>
<br>

# **Consumindo a API**

## **Consumindo a API com js**

Não adianta apenas testar com Postman ou com o /docs, a verdadeira aplicabilidade da API será no ambiente web. 

Os arquivos que eu usei para consumir essa API estarão presentes na pasta 'src'.

<img src="https://i.ibb.co/jLxtr73/image.png">

> Novamente, é importante certificar-se que o servidor está ligado e a API está online.

<img src="https://i.ibb.co/5sZw74L/image.png" width="60%">
<br>

Essa é a página contida nos arquivos index.html e script.js, os campos dos formulários são os parametros que a nossa api recebe.

Caso a API esteja offline, o 'Status da API' será:

<img src="https://i.ibb.co/Xs1QLFN/image.png" width="60%">
<br><br>

## Como funciona:

No HTML já está escrito como se o Status estivesse offline: 

```html
    <h2>Status da API:</h2>
    <div class="icon-text">
      <span class="icon has-text-danger" id="clr">
        <i id="icon" class="fas fa-ban"></i>
      </span>
      <span id="sts">Offline</span>
    </div>
```

No JavaScript, a função getStatusDaApi() é a responsável por alterar o conteúdo da div:
```javascript
async function getStatusDaAPI() {
    await fetch('http://localhost:8080/', {    
        method: 'GET',    
        withCredentials: false,    
        crossorigin: true,         
      })
```

> Para que fosse possível fazer essa solicitação com as duas aplicações rodando no localhost da minha máquina, foi necessário configurar um crossorigin no arquivo main.py.

```python
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1:5500",  # A origem do cliente
    "http://localhost:5500"  # Outra origem do cliente (se necessário)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
> A variável 'origins' é uma lista com as origens das requisições da nossa API.

<br>

A parte responsável por editar o conteúdo da div é: 

```javascript
    .then(data => {
        var icon = document.getElementById('icon');
        var span1 = document.getElementById('clr');
        var sts = document.getElementById('sts');
        
        if (data.mensagem) {
            icon.classList.replace('fa-ban','fa-check-square');
            span1.classList.replace('has-text-danger', 'has-text-success');
            sts.innerHTML = data.mensagem
        } 
    })
```

e caso a função fetch não consiga retornar os dados solicitados por algum erro, ele será exibido abaixo do status graças a função catch:

```javascript
    .catch(error => {
        var p = document.createElement("p");
        var erro = document.getElementById('sts')
        p.append(error)
        erro.append(p)
    })
```
<hr>
<br>

### A função enviarEmail() contém toda a lógica responsável para o programa fazer o envio do e-mail e retornar o sucesso ou não, porém a função fetch é a responsável por enviar os dados para a API:

```javascript
        fetch('http://localhost:8080/enviar_email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
              },
            body: JSON.stringify(dados)
        })
```

## Verificações do lado do cliente:

Para não tomar muito tempo fiz uma verificação simples:

Verificamos se os campos foram preenchidos:

```javascript
async function enviarEmail() {
    btn.addEventListener("click", () => {
        var destinatario = dst.value;
        var assunto = ast.value;

        if (destinatario === '' || assunto === '') {
            alert('Os campos não podem ficar em branco.')
        } else
```

E com isso, será emitido um alerta que impedirá o cliente de continuar com a ação:

<img src="https://i.ibb.co/6W3Xw06/image.png" width="70%">
<hr>

# E-mail inválido
Caso o e-mail esteja inválido, aparecerá uma notificação informando.

<img src="https://i.ibb.co/TgXtR6Z/image.png" width="60%">

E após 5 segundos, a página será atualizada:

A parte do código que corresponde a esse retorno é esse aqui:

```javascript
            if (data.detail) {
                mensagem.remove();
                msg.classList.add('is-danger');
                mensagemErr.innerHTML = data.detail[0].msg;               
            }
```

# E-mail válido:

Caso o e-mail seja válido e o campo 'Assunto' esteja preenchido, o retorno será exibido da seguinte forma:

<img src="https://i.ibb.co/D7xF0LS/image.png" width="60%">

E a parte que corresponde é: 

```javascript
            msg.classList.replace('label-off', 'label-on');
            msg.classList.add('is-primary');
            mensagem.classList.remove("desactivated");
            mensagem.innerHTML = data.mensagem;
```

Depois, a página será atualizada. Isso foi necessário porque a notificação de 'e-mail inválido' era exibida mesmo em caso de sucesso. Essa foi a solução mais rápida que eu encontrei e a parte do código responsável é: 

```javascript
            setTimeout(() => {
                msg.classList.replace('label-on', 'label-off');
                window.location.reload()
            }, 5000);
```

<hr>

<br>

# **Dockerfile**

Para facilitar o deploy da API e a instalação para testes, fiz um dockerfile responsável por criar a imagem da API. 

Para isso, execute o seguinte comando no terminal:

```
docker build -t nome_de_usuario/nome_da_imagem .
```

<ul>
    <li>
        "-t nome_de_usuario/nome_da_imagem": Aqui, estamos definindo uma tag para a imagem que será construída. A opção "-t" significa "tag" e permite que você defina um nome e um rótulo para a imagem.
    </li>
    <br>
    <li>
        O ":" é usado para separar a tag da imagem, fornecendo uma versão ou identificador específico. A tag é opcional, mas comumente usada para diferenciar versões ou configurações da imagem. Sem especificar uma tag, o Docker usa a tag padrão "latest".
    </li>
    <br>
    <li>
        ".": Esse ponto representa o contexto do build. Ele especifica que o Dockerfile e todos os arquivos necessários para a construção da imagem estão localizados no diretório atual.
    </li>
</ul>
<br>

> No meu caso ficará: docker build -t matheusferraz/servicemail:1v2 .

Posteriormente, para rodar a imagem no docker, escreva:

```
docker run -d -p 8080:80 docker.io/nome_de_usuario/nome_da_imagem
```

<ul>
    <li>
        "-d": Essa opção faz com que o contêiner seja executado em segundo plano, em modo "detached" (desvinculado), o que significa que ele será executado em segundo plano sem bloquear o terminal.
    </li>
    <br>
    <li>
        "-p 8080:80": Aqui, estamos mapeando a porta 8080 do host para a porta 80 do contêiner. Isso permite que o serviço dentro do contêiner seja acessado através da porta 8080 no host.
    </li>
    <br>
    <li>
        "docker.io/nome_de_usuario/nome_da_imagem": Isso especifica o nome da imagem a partir da qual o contêiner será criado. O Docker procurará essa imagem localmente e, se não a encontrar, fará o download dela a partir do repositório chamado "docker.io" (que é o repositório padrão).
    </li>
</ul>

<br>

Optei por deixar um dockerfile devido as suas principais vantagens, que são: A reprodutibilidade, automatização, versionamento, portabilidade, eficiência de armazenamento e compartilhamento. 

Ele permite criar imagens de contêiner de forma consistente, automatizada e portátil, garantindo a configuração correta do ambiente de execução. E também facilita o deploy em serviços de hospedagem.
<hr>
<br>

# **Considerações finais**

O ServiceMail, é um software totalmente livre e gratuito e é especialmente adequado para fins educacionais e de estudo da linguagem Python. 

As aplicabilidades de uma API de e-mail são:

<ul>
    <li>
        Comunicação com usuários: A API de e-mail permite que empresas enviem comunicações automatizadas, como confirmações de cadastro e notificações importantes, para seus usuários, garantindo uma comunicação eficiente e informando sobre eventos relevantes.
    </li>
    <br>
    <li>
        E-mail marketing: A API de e-mail é essencial para plataformas de e-mail marketing, permitindo o envio de campanhas personalizadas em grande escala, segmentando contatos, gerenciando templates de e-mail e monitorando estatísticas de entrega, oferecendo uma maneira eficaz de promover produtos e serviços.
    </li>
    <br>
    <li>
        Alertas e notificações em tempo real: A API de e-mail possibilita o envio de alertas e notificações em tempo real para aplicativos e sistemas, sendo útil para monitorar servidores, detectar fraudes, relatar erros e atualizar status, garantindo que informações importantes sejam comunicadas instantaneamente.
    </li>
    <br>
    <li>
        Integração com aplicativos e serviços: A API de e-mail pode ser integrada a aplicativos e serviços, como e-commerce e suporte ao cliente, permitindo o envio automático de e-mails de confirmação de pedidos, atualizações de entrega e respostas a consultas de clientes, proporcionando uma melhor experiência do usuário.
    </li>
    <br>
    <li>
        Automação de processos de negócios: A API de e-mail é usada para automatizar processos de negócios relacionados à comunicação por e-mail, como acompanhar correspondências com clientes em um sistema de CRM, facilitando a organização, registro e análise das interações com os clientes.
    </li>
</ul>
<br>

<<<<<<< HEAD
## Obrigado por ter chegado até aqui, caso tenha alguma dúvida ou problema com a API sinta-se livre para entrar em contato aqui pelo GitHub, Discord: Matheus Ferraz#3474, ou [Twitter](https://twitter.com/__mtsfrz__)!
=======
## Obrigado por ter chegado até aqui, caso tenha alguma dúvida ou problema com a API sinta-se livre para entrar em contato aqui pelo GitHub, Discord: Matheus Ferraz#3474, ou [Twitter](https://twitter.com/__mtsfrz__)
>>>>>>> 05fe703a9a75478b38f19920060b0867dbd814be
