const btn = document.getElementById('btn');
const dst = document.getElementById('dst');
const ast = document.getElementById('ast');
const github = document.getElementById('gitbtn');
const label = document.getElementById('label');
const cloud = document.getElementById('cloud');
const msg = document.getElementById('notificacao');
const mensagemErr = document.getElementById('mensagem-err');
const mensagem = document.getElementById('mensagem-ok');


github.addEventListener('mouseover', () => {
    label.classList.replace('label-off', 'label-on');
    cloud.classList.replace('label-off', 'label-on');
})

github.addEventListener('mouseleave', () => {
    label.classList.replace('label-on','label-off');
    cloud.classList.replace('label-on', 'label-off');
})

btn.addEventListener("click", enviarEmail);

async function enviarEmail() {
    var destinatario = dst.value;
    var assunto = ast.value;

    if (destinatario === '' || assunto === '') {
        alert('Os campos não podem ficar em branco.')
    } else {
        var dados = {
            destinatarios: [destinatario],
            assunto: assunto
        };
    
    
    fetch('http://localhost:8080/enviar_email', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        })
        .then(response => response.json())
        .then(data => {

            msg.classList.remove('is-danger');

            if (data.detail) {
                mensagem.remove();
                msg.classList.add('is-danger');
                mensagemErr.innerHTML = data.detail[0].msg;               
            }

            msg.classList.replace('label-off', 'label-on');
            msg.classList.add('is-primary');
            mensagem.classList.remove("desactivated");
            mensagem.innerHTML = data.mensagem;
            setTimeout(() => {
                msg.classList.replace('label-on', 'label-off');
                window.location.reload()
            }, 5000);
        })
        .catch(err => {
            const msg = document.getElementById('notificacao');
            var mensagem = document.getElementById('mensagem');
            msg.classList.replace('label-off', 'label-on');
            msg.classList.add('is-danger');
            mensagem.innerHTML = err;
    
            setTimeout(() => {
                msg.classList.replace('label-on', 'label-off');
            }, 5000);
        });
    }
}

async function getStatusDaAPI() {
    await fetch('http://localhost:8080/', {    
        method: 'GET',    
        withCredentials: false,    
        crossorigin: true,         
      })
    .then(r => r.json())
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
    .catch(error => {
        var p = document.createElement("p");
        var erro = document.getElementById('sts')
        p.append(error)
        erro.append(p)
    })
}

getStatusDaAPI()

