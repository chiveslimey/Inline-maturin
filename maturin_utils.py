import subprocess
import os
from pathlib import Path

def run(cmd: str, **kwargs) -> subprocess.CompletedProcess:
    '''
    シェルコマンドを実行する関数
    '''
    return subprocess.run(cmd, shell = True, check = True, **kwargs)

def build_maturin_project(name: str) -> None:
    '''
    RustのクレートをPythonのモジュールとして読み込む関数
    '''

    # カレントディレクトリを指定された名前のディレクトリに変更
    # maturin buildはソースディレクトリで実行しなければならないため
    os.chdir('./' + str(name))

    # ビルドとwheelのインストール
    run("maturin build --verbose")
    for p in Path("./target/wheels").iterdir():
        run(f"pip install {p}")
      
    os.chdir('..')

    return 
