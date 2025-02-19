import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import yt_dlp
import os
from urllib.request import urlopen
from io import BytesIO
from PIL import Image, ImageTk
import threading
import re
from queue import Queue


class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.download_queue = Queue()  # Fila de downloads
        self.current_download = None  # Download atual
        self.running = True  # Controle de execução
        self.video_info = {}  # Informações do vídeo carregado
        self.setup_styles()  # Configura os estilos
        self.setup_ui()  # Configura a interface
        self.queue_thread = threading.Thread(
            target=self.process_queue, daemon=True
        )  # Thread para processar a fila
        self.queue_thread.start()  # Inicia a thread da fila

    def setup_styles(self):
        self.style = ttk.Style()
        self.root.configure(bg="#2D2D2D")  # Tema escuro

        # Cores do tema dark moderno
        self.colors = {
            "background": "#2D2D2D",
            "primary": "#7289DA",
            "secondary": "#424549",
            "text": "#000000",  # Texto preto
            "highlight": "#43B581",
            "entry_bg": "#424549",  # Fundo escuro para caixas de entrada
            "entry_fg": "#000000",  # Texto branco para caixas de entrada
        }

        # Configurações gerais
        self.style.configure("TFrame", background=self.colors["background"])
        self.style.configure(
            "TLabel",
            background=self.colors["background"],
            foreground=self.colors["text"],
        )
        self.style.configure(
            "TButton", background=self.colors["primary"], foreground=self.colors["text"]
        )
        self.style.configure(
            "Horizontal.TProgressbar",
            troughcolor=self.colors["secondary"],
            background=self.colors["highlight"],
            thickness=15,
        )

        # Configurações para ttk.Entry
        self.style.configure(
            "TEntry",
            fieldbackground=self.colors["entry_bg"],  # Fundo da caixa de entrada
            foreground=self.colors["entry_fg"],  # Cor do texto
            insertcolor=self.colors["entry_fg"],  # Cor do cursor
            padding=5,
        )  # Espaçamento interno

        # Configurações para ttk.Combobox
        self.style.configure(
            "TCombobox",
            fieldbackground=self.colors["entry_bg"],  # Fundo da caixa de seleção
            foreground=self.colors["entry_fg"],  # Cor do texto
            selectbackground=self.colors["primary"],  # Fundo do item selecionado
            selectforeground=self.colors["text"],  # Texto do item selecionado
            padding=5,
        )  # Espaçamento interno

        # Configurações para ttk.Treeview (fila de downloads)
        self.style.configure(
            "Treeview",
            background=self.colors["secondary"],  # Fundo da lista
            foreground=self.colors["text"],  # Texto dos itens
            fieldbackground=self.colors["secondary"],  # Fundo dos campos
            borderwidth=0,
        )  # Remove bordas

        self.style.map(
            "Treeview",
            background=[
                ("selected", self.colors["primary"])
            ],  # Fundo do item selecionado
            foreground=[("selected", self.colors["text"])],
        )  # Texto do item selecionado

        # Configurações para o cabeçalho do Treeview
        self.style.configure(
            "Treeview.Heading",
            background=self.colors["primary"],  # Fundo do cabeçalho
            foreground=self.colors["text"],  # Texto do cabeçalho
            padding=5,
        )  # Espaçamento interno

    def setup_ui(self):
        self.root.title("NextTube Downloader")
        self.root.geometry("1000x700")
        self.root.resizable(True, True)

        # Container principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Seção de fila de downloads
        queue_frame = ttk.Frame(main_frame)
        queue_frame.pack(fill="x", pady=10)

        ttk.Label(queue_frame, text="Fila de Downloads:", font=("Arial", 12)).pack(
            anchor="w"
        )
        self.queue_tree = ttk.Treeview(
            queue_frame, columns=("status", "progress"), selectmode="none", height=5
        )
        self.queue_tree.pack(fill="x", pady=5)
        self.queue_tree.heading("#0", text="Vídeo")
        self.queue_tree.heading("status", text="Status")
        self.queue_tree.heading("progress", text="Progresso")
        self.queue_tree.column("#0", width=400, stretch=True)
        self.queue_tree.column("status", width=100, anchor="center")
        self.queue_tree.column("progress", width=100, anchor="center")

        # Seção de entrada de URL
        url_frame = ttk.Frame(main_frame)
        url_frame.pack(fill="x", pady=10)

        ttk.Label(url_frame, text="URL do Vídeo:", font=("Arial", 12)).pack(side="left")
        self.url_entry = ttk.Entry(url_frame, width=50)
        self.url_entry.pack(side="left", expand=True, fill="x", padx=10)
        ttk.Button(url_frame, text="Carregar", command=self.load_video_info).pack(
            side="left"
        )

        # Seção de visualização do vídeo
        self.preview_frame = ttk.Frame(main_frame)
        self.preview_frame.pack(fill="x", pady=10)

        # Thumbnail do vídeo
        self.thumbnail_label = ttk.Label(self.preview_frame)
        self.thumbnail_label.pack(side="left", padx=10)

        # Informações do vídeo
        info_frame = ttk.Frame(self.preview_frame)
        info_frame.pack(side="left", fill="both", expand=True)

        self.title_label = ttk.Label(
            info_frame, text="Título: ", font=("Arial", 18, "bold")
        )
        self.title_label.pack(anchor="w")

        self.duration_label = ttk.Label(info_frame, text="Duração: ")
        self.duration_label.pack(anchor="w")

        self.channel_label = ttk.Label(info_frame, text="Canal: ")
        self.channel_label.pack(anchor="w")

        # Opções de download
        options_frame = ttk.Frame(main_frame)
        options_frame.pack(fill="x", pady=10)

        ttk.Label(options_frame, text="Resolução:").grid(row=0, column=0, sticky="w")
        self.resolution_var = tk.StringVar()
        self.resolution_selector = ttk.Combobox(
            options_frame, textvariable=self.resolution_var, state="readonly"
        )
        self.resolution_selector.grid(row=0, column=1, sticky="ew", padx=10)

        ttk.Label(options_frame, text="Formato:").grid(
            row=1, column=0, sticky="w", pady=5
        )
        self.format_var = tk.StringVar(value="Vídeo")
        ttk.Radiobutton(
            options_frame, text="Vídeo", variable=self.format_var, value="Vídeo"
        ).grid(row=1, column=1, sticky="w")
        ttk.Radiobutton(
            options_frame, text="Áudio", variable=self.format_var, value="Áudio"
        ).grid(row=1, column=2, sticky="w")

        ttk.Label(options_frame, text="Diretório:").grid(
            row=2, column=0, sticky="w", pady=5
        )
        self.directory_var = tk.StringVar()
        ttk.Entry(options_frame, textvariable=self.directory_var).grid(
            row=2, column=1, sticky="ew", padx=10
        )
        ttk.Button(options_frame, text="Procurar", command=self.select_directory).grid(
            row=2, column=2
        )

        # Controles de download
        control_frame = ttk.Frame(main_frame)
        control_frame.pack(fill="x", pady=10)

        self.progress_bar = ttk.Progressbar(
            control_frame, orient="horizontal", mode="determinate"
        )
        self.progress_bar.pack(fill="x", pady=5)

        self.status_label = ttk.Label(
            control_frame, text="", foreground=self.colors["highlight"]
        )
        self.status_label.pack()

        self.download_button = ttk.Button(
            control_frame, text="Adicionar à Fila", command=self.add_to_queue
        )
        self.download_button.pack(side="left", padx=5)

        self.clear_button = ttk.Button(
            control_frame, text="Limpar Fila", command=self.clear_queue
        )
        self.clear_button.pack(side="left", padx=5)

        # Configurar expansão de colunas
        options_frame.columnconfigure(1, weight=1)

    def is_youtube_url(self, url):
        return "youtube.com" in url or "youtu.be" in url

    def load_video_info(self):
        url = self.url_entry.get()
        if not url or not self.is_youtube_url(url):
            messagebox.showerror("Erro", "Por favor, insira um URL válido do YouTube!")
            return

        def fetch_info():
            try:
                ydl_opts = {"quiet": True, "skip_download": True}
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=False)
                    self.video_info = info

                    # Atualizar UI
                    self.root.after(0, self.update_video_info)

                    # Carregar thumbnail
                    thumbnail_url = info.get("thumbnail", "")
                    if thumbnail_url:
                        self.load_thumbnail(thumbnail_url)

            except Exception as e:
                self.root.after(0, lambda: messagebox.showerror("Erro", str(e)))

        threading.Thread(target=fetch_info, daemon=True).start()
        self.status_label.config(
            text="Carregando informações do vídeo...", foreground="white"
        )

    def load_thumbnail(self, thumbnail_url):
        try:
            image_data = urlopen(thumbnail_url).read()
            image = Image.open(BytesIO(image_data))
            image.thumbnail((200, 200))
            photo = ImageTk.PhotoImage(image)
            self.thumbnail_label.config(image=photo)
            self.thumbnail_label.image = photo
        except Exception as e:
            self.thumbnail_label.config(text="Thumbnail não disponível")

    def update_video_info(self):
        self.title_label.config(text=f"Título: {self.video_info.get('title', '')}")

        # Formatação da duração
        duration = self.video_info.get("duration", 0)
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        self.duration_label.config(
            text=f"Duração: {hours:02}:{minutes:02}:{seconds:02}"
        )

        self.channel_label.config(text=f"Canal: {self.video_info.get('uploader', '')}")

        # Atualizar opções de resolução
        formats = self.video_info.get("formats", [])
        resolutions = sorted(
            {f.get("height", 0) for f in formats if f.get("vcodec") != "none"},
            reverse=True,
        )
        self.resolution_selector["values"] = resolutions
        if resolutions:
            self.resolution_selector.current(0)

    def select_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_var.set(directory)

    def add_to_queue(self):
        if not self.video_info:
            messagebox.showerror("Erro", "Carregue as informações do vídeo primeiro!")
            return

        url = self.url_entry.get()
        save_path = self.directory_var.get()
        format_type = self.format_var.get()
        resolution = self.resolution_var.get()

        if not url or not save_path:
            messagebox.showerror("Erro", "Preencha todos os campos obrigatórios!")
            return

        item = {
            "url": url,
            "save_path": save_path,
            "format": format_type,
            "resolution": resolution,
            "title": self.video_info.get("title", "Desconhecido"),
            "status": "Pendente",
            "progress": 0,
        }

        self.download_queue.put(item)
        self.update_queue_display()

    def process_queue(self):
        while self.running:
            if not self.download_queue.empty() and not self.current_download:
                item = self.download_queue.get()
                self.current_download = item
                self.root.after(0, self.update_queue_display)

                download_thread = threading.Thread(
                    target=self.download_video, args=(item,), daemon=True
                )
                download_thread.start()
            threading.Event().wait(0.5)

    def download_video(self, item):
        try:
            ydl_opts = {
                "outtmpl": os.path.join(item["save_path"], "%(title)s.%(ext)s"),
                "progress_hooks": [lambda d: self.progress_hook(d, item)],
            }

            if item["format"] == "Vídeo":
                if item["resolution"]:
                    ydl_opts["format"] = (
                        f"bestvideo[height<={item['resolution']}][ext=mp4]+bestaudio/best"
                    )
                else:
                    ydl_opts["format"] = "bestvideo+bestaudio/best"
            else:
                ydl_opts["format"] = "bestaudio/best"
                ydl_opts["postprocessors"] = [
                    {
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }
                ]

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([item["url"]])

            item["status"] = "Concluído"
            item["progress"] = 100
        except Exception as e:
            item["status"] = f"Erro: {str(e)}"
        finally:
            self.current_download = None
            self.root.after(0, self.update_queue_display)
            self.root.after(0, self.process_next)

    def progress_hook(self, d, item):
        if d["status"] == "downloading":
            percent_str = re.sub(r"\x1b\[[0-9;]*m", "", d.get("_percent_str", "0%"))
            percent_clean = re.sub(r"[^0-9.]", "", percent_str)

            try:
                item["progress"] = float(percent_clean)
            except ValueError:
                item["progress"] = 0

            item["status"] = "Baixando"
            self.root.after(0, self.update_queue_display)

    def update_queue_display(self):
        for child in self.queue_tree.get_children():
            self.queue_tree.delete(child)

        for item in list(self.download_queue.queue):
            self.queue_tree.insert(
                "",
                "end",
                text=item["title"],
                values=(item["status"], f"{item['progress']:.1f}%"),
            )

        if self.current_download:
            self.queue_tree.insert(
                "",
                "end",
                text=self.current_download["title"],
                values=(
                    self.current_download["status"],
                    f"{self.current_download['progress']:.1f}%",
                ),
                tags=("current",),
            )
            self.queue_tree.tag_configure("current", background="#e0e0e0")

    def clear_queue(self):
        while not self.download_queue.empty():
            self.download_queue.get()
        self.current_download = None
        self.update_queue_display()

    def on_closing(self):
        self.running = False
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
