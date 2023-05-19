from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from pydantic import BaseModel, validator
from typing import List

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib
import re



"""
Criando uma instância do FastAPI.

A partir dessa variável nós criaremos os endpoints, as rotas, subiremos
a aplicação e etc.
"""
app = FastAPI()


## Modelo de e-mails
class Email(BaseModel): 
    para: List[str]
    assunto: str

    #Validando o e-mail usando re
    @validator('email', pre=True, check_fields=False)
    def valida_email(cls, v):
        if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+').match(v):
            raise ValueError('O e-mail está inválido!')
        return v
    

@app.get("/")
def get_root():
    """
    End-point root do projeto, base, que será exibido quando acessar
    o endereço raiz do projeto. Ex: 127.0.0.1/
    """
    return {"200": "On-line."}



@app.post("/enviar_email")
async def enviar_email(email: Email): ## Note que a função recebe por parâmetro um e-mail do modelo Email
    """
    Aqui é o end-point responsável por fazer todo processo do envio do e-mail,
    Busquei manter apenas o esqueleto para o programa funcionar, fique a vontade
    para desenvolver authenticação e aplicar em seu negócio.

    Com tempo, pretendo trazer uma atualização refatorando esse projeto.
    """

    with open("mail.html") as f:
        body_html = f.read()
        """
        Lendo o arquivo HTMl que será o body do e-mail.
        Você pode editar corpo do e-mail ao seu critério no
        arquivo mail.html
        """

    """
    Esse bloco é responsável por armezenar dentro das variáveis
    os dados referente ao e-mail que será enviado.
    Quem enviou, a senha de segurança da Google, o assunto e quem
    receberá a mensagem.
    """
    remetente = 'youscraphere@gmail.com' # Insira seu e-mail aqui.
    senha_de_envio = 'oxzlvbxidlbmuyzp' # Insira a senha de segurança da Google.
    assunto = email.assunto
    destinatario = email.para

    """
    Aqui é a instância do MIME que será a 
    biblioteca responsável por enviar os dados ao 
    servidor do gmail. 
    """
    mensagem = MIMEMultipart() 
    mensagem['From'] = remetente
    mensagem['To'] = ", ".join(destinatario)
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(body_html, 'html')) # Corpo (body) do e-mail

    """
    Pediremos ao Python para que tente se conectar com o servidor do 
    Gmail criando uma instância do SMTPlib, informando o servidor e
    a porta (587), não devemos ter problemas com conexão.
    """
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.starttls() # Entrando no servidor
        server.login(remetente, senha_de_envio) # Efetuando a authenticação no servidor
        server.sendmail(remetente, destinatario, mensagem.as_string()) # Enviando a mensagem
        server.quit() # Fechando o servidor

    # Caso ocorra algum erro durante o processo, o except será responsável por informar.
    except smtplib.SMTPAuthenticationError as ex: {
        "400": ex
    }
    return JSONResponse(content={"message": "E-mail enviado com sucesso!"})

# Tratando excessões HTTP e retornando para o cliente.
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )



