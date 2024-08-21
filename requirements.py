import subprocess
import sys
from tkinter import *
from tkinter import messagebox

# 包及其版本列表
packages = [
    "aenum==3.1.15",
    "aiohttp==3.9.5",
    "aiosignal==1.3.1",
    "altgraph==0.17.4",
    "annotated-types==0.7.0",
    "attrs==24.2.0",
    "certifi==2024.7.4",
    "charset-normalizer==3.3.2",
    "configparser==7.0.0",
    "DateTime==5.5",
    "Deprecated==1.2.14",
    "et-xmlfile==1.1.0",
    "frozenlist==1.4.1",
    "future==1.0.0",
    "greenlet==3.0.3",
    "idna==3.7",
    "keyboard==0.13.5",
    "line-bot-sdk==3.11.0",
    "multidict==6.0.5",
    "numpy==2.0.1",
    "openpyxl==3.1.5",
    "packaging==24.1",
    "pandas==2.2.2",
    "pefile==2023.2.7",
    "pillow==10.4.0",
    "pip==24.0",
    "pydantic==2.8.2",
    "pydantic_core==2.20.1",
    "pyinstaller==6.9.0",
    "pyinstaller-hooks-contrib==2024.7",
    "pyodbc==5.1.0",
    "pystray==0.19.5",
    "python-dateutil==2.9.0.post0",
    "pytz==2024.1",
    "pywin32-ctypes==0.2.2",
    "requests==2.31.0",
    "setuptools==72.1.0",
    "six==1.16.0",
    "SQLAlchemy==2.0.32",
    "typing_extensions==4.12.2",
    "tzdata==2024.1",
    "urllib3==2.2.2",
    "watchdog==4.0.1",
    "wrapt==1.16.0",
    "yarl==1.9.4",
    "zope.interface==7.0.1",
    "instaloader==4.13"
]
def install_package(package):
    """安装单个包"""
    print(f"正在安装 {package}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def show_top_level_messagebox(title, message):
    top = Tk()
    top.withdraw()  # 隐藏主窗口
    top.attributes('-topmost', True)  # 设置为最顶层
    messagebox.showinfo(title, message, master=top)
    top.destroy()  # 销毁临时窗口

def install_packages():
    error_shown = False
    try:
        installed_packages = set()
        for package in packages:
            if package not in installed_packages:
                install_package(package)
                installed_packages.add(package)
        show_top_level_messagebox("成功", "所有套件已成功安装")
    except subprocess.CalledProcessError as e:
        if not error_shown:
            show_top_level_messagebox("错误", "安装套件时发生错误")
            error_shown = True
    except Exception as e:
        if not error_shown:
            show_top_level_messagebox("错误", "安装套件时发生错误")
            error_shown = True
if __name__ == "__main__":
    install_packages()