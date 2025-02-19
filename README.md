<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NextTube Downloader - README</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #121212;
            color: #ffffff;
            padding: 20px;
        }
        h1, h2, h3 {
            color: #00d4ff;
        }
        code {
            background: #333;
            padding: 5px;
            border-radius: 5px;
            font-family: monospace;
        }
        pre {
            background: #1e1e1e;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }
        a {
            color: #00d4ff;
        }
    </style>
</head>
<body>
    <h1>🚀 NextTube Downloader 🎥</h1>
    <p>O <strong>NextTube Downloader</strong> é uma aplicação em Python com interface gráfica feita em Tkinter que permite baixar vídeos e áudios do YouTube de forma prática e intuitiva!</p>
    
    <h2>📋 Visão Geral</h2>
    <ul>
        <li><strong>Carregamento de Informações do Vídeo:</strong> Exibe título, duração, canal e thumbnail do vídeo.</li>
        <li><strong>Fila de Downloads:</strong> Gerencie múltiplos downloads com status e progresso em tempo real.</li>
        <li><strong>Opções de Download:</strong> Escolha entre baixar o vídeo em diferentes resoluções ou apenas o áudio (com conversão para MP3).</li>
        <li><strong>Interface Amigável:</strong> Layout moderno com cores personalizadas e controles intuitivos.</li>
    </ul>
    
    <h2>🔧 Tecnologias e Bibliotecas Utilizadas</h2>
    <ul>
        <li><strong>Python 3</strong></li>
        <li><strong>Tkinter:</strong> Para a interface gráfica.</li>
        <li><strong>yt-dlp:</strong> Realiza o download dos vídeos e extração de informações.</li>
        <li><strong>Pillow (PIL):</strong> Manipulação e exibição das thumbnails.</li>
        <li><strong>Threading & Queue:</strong> Para processamento assíncrono e gerenciamento da fila de downloads.</li>
    </ul>
    
    <h2>🚀 Como Executar</h2>
    <h3>Pré-requisitos</h3>
    <p>Instale as dependências necessárias utilizando o <code>pip</code>:</p>
    <pre><code>pip install yt-dlp Pillow</code></pre>
    <p><strong>Atenção:</strong> Para baixar apenas o áudio e convertê-lo para MP3, o <a href="https://ffmpeg.org/" target="_blank">FFmpeg</a> precisa estar instalado e configurado no seu sistema.</p>
    
    <h3>Passos</h3>
    <ol>
        <li><strong>Clone o repositório:</strong></li>
        <pre><code>git clone https://github.com/seu-usuario/nexttube-downloader.git
cd nexttube-downloader</code></pre>
        <li><strong>Execute a aplicação:</strong></li>
        <pre><code>python nome_do_seu_script.py</code></pre>
        <p><em>Substitua <code>nome_do_seu_script.py</code> pelo nome do arquivo que contém o código.</em></p>
    </ol>
    
    <h2>📌 Funcionalidades</h2>
    <ul>
        <li><strong>Interface Intuitiva:</strong> Utiliza um design moderno com tema dark e cores personalizadas.</li>
        <li><strong>Suporte a Vídeo e Áudio:</strong> Baixe vídeos em diferentes resoluções ou extraia o áudio em MP3.</li>
        <li><strong>Gerenciamento de Downloads:</strong> Adicione vídeos a uma fila e monitore o progresso de cada download em tempo real.</li>
        <li><strong>Download Assíncrono:</strong> Utiliza multithreading para que a interface permaneça responsiva enquanto os downloads acontecem.</li>
    </ul>
    
    <h2>💡 Personalização</h2>
    <p>Você pode customizar diversos aspectos do projeto:</p>
    <ul>
        <li><strong>Estilos e Cores:</strong> Modifique as configurações no método <code>setup_styles</code> para adaptar o tema ao seu gosto.</li>
        <li><strong>Opções de Download:</strong> Ajuste as opções de formato e resolução conforme necessário.</li>
    </ul>
    
    <h2>🤝 Contribuições</h2>
    <p>Contribuições são bem-vindas! Se você deseja melhorar o projeto, sinta-se à vontade para abrir <em>issues</em> ou enviar <em>pull requests</em>.</p>
    <p>Veja também as <a href="CONTRIBUTING.md" target="_blank">Diretrizes de Contribuição</a> para mais detalhes.</p>
    
    <h2>📄 Licença</h2>
    <p>Este projeto está licenciado sob a <a href="LICENSE" target="_blank">MIT License</a>.</p>
    
    <hr>
    <p>Aproveite e boa utilização! Se tiver alguma dúvida ou sugestão, entre em contato! 😄✌️</p>
</body>
</html>
