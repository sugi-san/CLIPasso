# フォルダリセット関数
import os
import shutil
def reset_folder(folder):
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    os.makedirs(folder, exist_ok=True)

# 動画再生
from IPython.display import display, HTML
from IPython.display import HTML

def display_mp4(path):
    from base64 import b64encode
    mp4 = open(path,'rb').read()
    data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
    display(HTML("""
    <video width=700 controls>
        <source src="%s" type="video/mp4">
    </video>
    """ % data_url))

