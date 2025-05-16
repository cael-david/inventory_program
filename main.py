import webview
import os

def start_app():
    path = os.path.abspath("ui/index.html")
    window = webview.create_window("Stock Manager", path, width=1000, height=700)
    webview.start()

if __name__ == "__main__":
    start_app()
