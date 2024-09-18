document.getElementById('matricula-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const formData = {
        nome: document.getElementById('nome').value,
        numero: document.getElementById('numero').value,
        curso: document.getElementById('curso').value,
        periodo: document.getElementById('periodo').value,
        cotas: document.getElementById('cotas').value
    };

    fetch('https://api.sheetmonkey.io/form/ig9CUs7w52dHRERb9qMuo3', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
});

function sucesso(){
    window.location.href = "./espera.html"
}