from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel, validator
from typing import List

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import smtplib
import re



"""
Declarando a instância do FastAPI.

A partir dessa variável nós criaremos os endpoints, as rotas, subiremos
a aplicação e etc.
"""
app = FastAPI()

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


## Modelo de e-mails
class Email(BaseModel): 
    destinatarios: List[str]
    assunto: str

    #Validando o e-mail usando re
    @validator('destinatarios')
    def valida_email(cls, v):
        if isinstance(v, list) and len(v) == 1:
            v = v[0]  # Obter o valor de e-mail da lista
            if not re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+').match(v):
                raise ValueError('O e-mail está inválido!')
            return v
        else:
            return v

@app.get("/")
def get_root():
    """
    End-point root do projeto, base, que será exibido quando acessar
    o endereço raiz do projeto. Ex: 127.0.0.1/
    """
    return {"mensagem": "On-line."}



@app.post("/enviar_email")
async def enviar_email(email: Email): ## Note que a função recebe por parâmetro o modelo Email
    print(email)
    """
    O método enviar_email é o end-point responsável por fazer todo processo do envio do e-mail.

    Busquei manter apenas o esqueleto para o programa funcionar, fique a vontade
    para desenvolver como preferir.
    """

    with open("mail.html") as f:
        body_html = f.read()
        """
        Lendo o arquivo HTMl que será o corpo do e-mail.
        Você pode editar corpo do e-mail ao seu critério no
        arquivo mail.html
        """

    """
    Esse bloco é responsável por armezenar dentro das variáveis
    os dados referente ao e-mail que será enviado.

    Quem enviou, a senha de segurança da Google, o assunto e quem
    receberá a mensagem (o destinatário).
    """
    remetente = '' # Insira seu e-mail aqui.
    senha_de_envio = '' # Insira a senha de segurança da Google.
    assunto = email.assunto
    destinatarios = email.destinatarios

    """
    Aqui declaramos a instância do MIME. Que é a 
    biblioteca responsável por enviar os dados codificados para
    o protocolo no qual o servidor do Gmail responde.
    """
    mensagem = MIMEMultipart() 
    mensagem['From'] = remetente
    mensagem['To'] = ", ".join(destinatarios)
    mensagem['Subject'] = assunto
    mensagem.attach(MIMEText(body_html, 'html')) # Corpo (body) do e-mail

    """
    Com a palavra reservada try, pediremos ao Python para que tente se conectar com o servidor do 
    Gmail criando uma instância do SMTPlib, informando o servidor e
    a porta (587), não devemos ter problemas com conexão.
    """
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.starttls() # Entrando no servidor
        server.login(remetente, senha_de_envio) # Efetuando a authenticação no servidor
        server.sendmail(remetente, destinatarios, mensagem.as_string()) # Enviando a mensagem
        server.quit() # Fechando o servidor

    # Caso ocorra algum erro durante o processo de envio do e-mail, o except será responsável por informar.
    except smtplib.SMTPAuthenticationError as ex: {
        "mensagem": ex
    }
    return JSONResponse(content={"mensagem": "E-mail enviado com sucesso!"})

# Tratando excessões HTTP e retornando para o cliente.
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"mensagem": exc.detail},
    )



