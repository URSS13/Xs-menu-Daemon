# 🚀Xsimple-menu_Daemon para X11
!(IMGs/Xsmenu.png)
## ✨Descripción

Este script es un **Daemon para X11** que monitorea los cambios en el portapapeles y los registra en un historial .pickle Permite al usuario acceder a fragmentos de texto previamente copiados desplegando un menú de opciones a seleccionar y pegar.

## 🎨Características

- **Monitoreo en tiempo real**: Captura automáticamente los cambios en el portapapeles.
- **🌈 Historial de portapapeles**: Almacena un máximo de 10 fragmentos de texto.
- **🎯 Interfaz de usuario intuitiva**: Despliega un menú accesible mediante '<Ctrl>+<Alt>+m' para seleccionar el texto a pegar.
- **🔥 Ligero y eficiente**: Diseñado para consumir pocos recursos del sistema.

## 📦 Dependecias
- **📚 librerias**:
						pynput, (os, sys, subprocess, time, re, pickle, argparse, threading, signal) Libreria standar python3
- **⚙️ Herramientas**:
						xclip, dmenu, nohup

## 🛠️ Instalación

El proyecto incluye un script de instalación que se ejecuta con el interprete de python3, Actualmente ha sido probado en distribuciones basadas en Debian. aunque no a sido probado con gestores diferentes a Mate, no deberia presentar problemas en entornos como XFCE, KDE, etc. 

1. 🐍PYTHON INSTALL.PY

   Clona el repositorio y ejecuta el script de instalación:
   ```bash ó zsh
   git clone https://github.com/Urss13/tu_repositorio.git
   cd Xs_menu
   chmod +x install.py
   chmod +x xs_menu_.py
   python install.py
   ```
   El servicio se instalara en ~/.local/bin/, puede ver la combinacion de teclas para su uso con 
   ```xsmenu -h ó --help
   ```
   Asegúrate de que tu configuracion de hotkeys no tenga conflictos con los atajos establecidos para Xsmenu.
   el servicio se iniciara automaticamente al iniciar sesión gracias al archivo xsmenu.desktop creado en
   ~/.config/autostart, puede ejecutarlo manualmente eliminando el mismo archivo.
   ```bash ó zsh
   nohup xsmenu  &> dev/null/ &
   ```
   O integrarlo con algun servicio de hotkeys como sxhkd

2. ⚙️ INSTALACIÓN MANUAL
   Clona el repositorio:

   ```bash ó zsh
   git clone https://github.com/Urss13/tu_repositorio.git
   pip install requirements.txt
   sudo apt install xclip
   sudo apt install dmenu
   mkdir -p ~/.local/bin/
   mkdir -p ~/.config/autostart/
   cd Xs_menu
   chmod +x xs_menu.py
   cp xs_menu_.py ~/.local/bin/xsmenu
   cd ~/.config/autostart/
   nano xsmenu.desktop
   ```
   Añada las siguientes lineas:
   [Desktop Entry]
   Name=Xsmenu
   Comment=X11 simple menu Daemon
   Exec=/home/{tu usuario}/.local/bin/xsmenu
   Terminal=false
   Type=Application
   X-Mate-Autostart-Delay=15
   Reemplace {tu usuario} con el correspondiente y X-Mate- con el entorno que estés utilizando,
   guarde los cambios y cierre el archivo.
   ```bash ó zsh
   cd
   nano ~/.zshrc
   ```
   Añada la siguiente linea:
   export PATH="$HOME/.local/bin/:$PATH"
   guarde cambios y cierre.
   ```bash ó zsh
   source ~/.zshrc
   ```
   Reinicie pc ó sesion para ver los cambios.
   ## 🚀Futuras mejoras:
   Eliminar las dependencias del script y terminar la opción de perzonalizacion.
   Debe de entenderse que, en principio el script fue echo para Evitar la Fatiga.
