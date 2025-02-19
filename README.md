# NextTube Downloader 🚀🎥

O **NextTube Downloader** é uma aplicação em Python com interface gráfica feita em Tkinter que permite baixar vídeos e áudios do YouTube de forma prática e intuitiva!

## 📋 Visão Geral

Este projeto oferece uma interface moderna com tema dark e funcionalidades que incluem:
- **Carregamento de Informações do Vídeo:** Exibe título, duração, canal e thumbnail do vídeo.
- **Fila de Downloads:** Gerencie múltiplos downloads com status e progresso em tempo real.
- **Opções de Download:** Escolha entre baixar o vídeo em diferentes resoluções ou apenas o áudio (com conversão para MP3).
- **Interface Amigável:** Layout moderno com cores personalizadas e controles intuitivos.

## 🛠 Tecnologias e Bibliotecas Utilizadas

- **Python 3**  
- **Tkinter:** Para a interface gráfica.  
- **yt-dlp:** Realiza o download dos vídeos e extração de informações.  
- **Pillow (PIL):** Manipulação e exibição das thumbnails.  
- **Threading & Queue:** Para processamento assíncrono e gerenciamento da fila de downloads.

## 🚀 Como Executar

### Pré-requisitos

- **Python 3.6+**  
- Instale as dependências necessárias utilizando o `pip`:

```bash
pip install yt-dlp Pillow
```

> **Atenção:** Para baixar apenas o áudio e convertê-lo para MP3, o [FFmpeg](https://ffmpeg.org/) precisa estar instalado e configurado no seu sistema.

### Passos

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nexttube-downloader.git
   cd nexttube-downloader
   ```

2. **Execute a aplicação:**

   ```bash
   python nome_do_seu_script.py
   ```

   *Substitua `nome_do_seu_script.py` pelo nome do arquivo que contém o código.*

## 📌 Funcionalidades

- **Interface Intuitiva:** Utiliza um design moderno com tema dark e cores personalizadas.  
- **Suporte a Vídeo e Áudio:** Baixe vídeos em diferentes resoluções ou extraia o áudio em MP3.  
- **Gerenciamento de Downloads:** Adicione vídeos a uma fila e monitore o progresso de cada download em tempo real.  
- **Download Assíncrono:** Utiliza multithreading para que a interface permaneça responsiva enquanto os downloads acontecem.

## 💡 Personalização

Você pode customizar diversos aspectos do projeto:
- **Estilos e Cores:** Modifique as configurações no método `setup_styles` para adaptar o tema ao seu gosto.
- **Opções de Download:** Ajuste as opções de formato e resolução conforme necessário.

## 🤝 Contribuições

Contribuições são bem-vindas! Se você deseja melhorar o projeto, sinta-se à vontade para abrir *issues* ou enviar *pull requests*.  
Veja também as [Diretrizes de Contribuição](CONTRIBUTING.md) para mais detalhes.

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

Aproveite e boa utilização! Se tiver alguma dúvida ou sugestão, entre em contato! 😄✌️
