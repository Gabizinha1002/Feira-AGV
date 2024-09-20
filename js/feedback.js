const form = document.getElementById('opiniao-form');
form.addEventListener('submit', async function (e) {
    e.preventDefault();

    // Coletar os dados do formulário
    const nome = document.getElementById('nome').value;
    const opiniao = document.getElementById('opiniao').value;

    // Enviar os dados para o Google Sheets via Sheet Monkey
    try {
        const response = await fetch('https://api.sheetmonkey.io/form/xfv8Kx1ihg6eHYj5tnAFop', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                nome: nome,
                opiniao: opiniao
            }),
        });

        if (response.ok) {
            document.getElementById('mensagem-sucesso').style.display = 'block';
            form.reset();
        } else {
            alert('Ocorreu um erro ao enviar sua opinião.');
        }
    } catch (error) {
        alert('Erro de conexão, tente novamente.');
    }
});