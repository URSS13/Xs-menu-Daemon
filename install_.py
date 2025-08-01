#! usr/bin/python3
# -*- coding: utf-8 -*-
import os, sys,subprocess,tqdm,re

user_ = os.getlogin()
repo_ = os.getcwd()

def preparacion_():
    try:
        subprocess.run(['mkdir', '-p', '.local/bin/'], check=True)
        subprocess.run(['mkdir', '-p', '.config/autostart/'], check=True)
        subprocess.run(['cp', '-v', f'{repo_}/xs_menu_.py', f'/home/{user_}/.local/bin/xsmenu'], check=True)
    except:
        print('no se pudo crear el fichero de installacion...')
        sys.exit()
    try:
        with open('prueba.desktop', 'w') as desktop_file_:
            desktop_file_.writelines(["[Desktop Entry]\n","Name=Xsmenu\n","Comment=X11 simple menu Daem\n",
            f"Exec=/home/{user_}/.local/bin/xsmenu\n","Terminal=false\n","Type=Application\n",
            "X-MATE-Autostart-Delay=15"])
    except:
        subprocess.run(['rm', f'/home/{user_}/.local/bin/xsmenu'])
        print('Error!, no se pudo generar el .desktop')
        sys.exit()

def pip_install_():
    try:
        subprocess.run(['pip', 'install', '-r', f'{repo_}/requirements.txt'], check=True)
        return True
    except:
        print('Error! pip no pudo instalar las dependencias')
        sys.exit()

def herramientas_install_():
    try:
        dmenu_ = subprocess.run(['which', 'dmenu'],capture_output=True, check=True).stdout.decode()
        xclip_ = subprocess.run(['which', 'xclip'], capture_output=True, check=True).stdout.decode()
        pass
    except:
        print("Ups! el comando which no existe")
    try:
        check_ = [re.sub("\n","",dmenu_.split('/')[-1]), re.sub("\n", "", xclip_.split('/')[-1])]
        if "dmenu" in check_:
            print("dmenu comprobado!")
            pass
        else:
            print('dmenu no esta instalado\nse instalara dmenu')
            subprocess.run(['sudo', 'apt', 'install', 'dmenu'],check=True)
        if "xclip" in check_:
            print("xclip check!")
            pass
        else:
            print('xclip no esta instalado\nse instalara xclip')
            subprocess.run(['sudo', 'apt', 'install', 'xclip'],check=True)
            pass
    except:
        print('Error! no se pudo comprobar las herramientas')

def path_():
    try:
        with open('.zshrc', 'a') as xs_source_:
            xs_source_.write('\n'+'export PATH="$HOME/.local/bin/:$PATH"')
            pass
    except:
        try:
            with open('.shrc', 'a') as xs_source_:
                xs_source_.write('\n'+'export PATH="$HOME/.local/bin/:$PATH"')
                pass
        except:
            print("Error! no se pudo exportar el path")
            sys.exit()

if __name__ == '__main__':
    install_ = os.chdir(f'/home/{user_}/')
    ficheros_ = preparacion_()
    dependecias_ = pip_install_()
    comprobacion_ = herramientas_install_()
    exportar_ = path_()
    print('recarga el archivo .(shell)rc')
    print('Reinicia la pc para ver los cambios...(xsmenu -h ó --help para mas informacion.)')
    sys.exit()
