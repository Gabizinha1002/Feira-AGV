
const form = document.getElementById('opiniao-form');

form.addEventListener('submit', async function (e) {
            e.preventDefault();

            const opiniao = document.getElementById('opiniao').value;
            try {
                const response = await fetch('https://api.sheetmonkey.io/form/xfv8Kx1ihg6eHYj5tnAFop', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
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