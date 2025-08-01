#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys, subprocess, time, re, pickle, argparse, threading, signal
from pynput import keyboard

#                        ██╗  ██╗███████╗      ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
#                        ╚██╗██╔╝██╔════╝      ████╗ ████║██╔════╝████╗  ██║██║   ██║
#                         ╚███╔╝ ███████╗█████╗██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
#                         ██╔██╗ ╚════██║╚════╝██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
#                        ██╔╝ ██╗███████║      ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
#                        ╚═╝  ╚═╝╚══════╝      ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝
#      ==> Simple D***** para X , genera un historial (maximo 10 fragmentos) del portapapeles, despliega un menu 
#                        para seleccionar y pegar el historial se reinicia en cada sesion <==      
#                                            ***** MX *****
""" Variables Globales"""
indice = 0
sistem_os = os.uname()
version = sistem_os[3]
ruta_ = os.getcwd()
menu_buffers_ = os.path.isfile(f'{ruta_}/.xs_historial_.pickle') 
sistem_parcer = sistem_os[0],version.split(' ')[3],sistem_os[1]
k_ontrol_ = keyboard.Controller()

def historial_buffers_():
    global ruta_
    if menu_buffers_ == False:
        with open(f"{ruta_}/.xs_historial_.pickle", 'wb') as buffer_:
            subprocess.call(['notify-send', 'Historial activo...'])
    else:
        pass

"""              ==> Hilo monitor a la escucha del portapapeles, mantiene historial de copias,
                            lanza el despliege del menu de seleccion y pegado <==                   """

def Xs_menu_Daemon_():
    global indice
    while True:
        time.sleep(1.5)
        buffer_ = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True).stdout.decode()
        if buffer_ != "":
            with open(f"{ruta_}/.xs_historial_.pickle", 'rb+') as pickle_:
                try:
                    buffer__ = pickle.load(pickle_)
                    b = busqueda_(buffer__, buffer_)
                    if b == True:
                        pass
                    else:
                        indice += 1
                        index  = [indice, buffer_]
                        buffer__.append(index)
                        buffer_fit_ = control_t_(buffer__)
                        with open(f"{ruta_}/.xs_historial_.pickle", 'wb') as pickle_:
                            pickle.dump(buffer_fit_, pickle_)
                except:
                    indice += 1
                    index  = [indice, buffer_]
                    menu_ = [index]
                    with open(f"{ruta_}/.xs_historial_.pickle", 'wb') as pickle_:
                        pickle.dump(menu_, pickle_)
        else:
            pass

def control_t_(buffer__):
    if len(buffer__) >= 11:
        del(buffer__[0])
        return buffer__
    else:
        return buffer__

def busqueda_(buffer__, buffer_):
    for row in buffer__:
        if buffer_ in row:
            b = True
        else:
            b = False
    return b

"""              ==>  Deserializacion del archivo.pickle, formateo, presentacion, selección,
                                decodificación,carga y pegado del buffer. <==           """

def formato_menu_(buffer_):
    expande_ = list()
    for lista_ in reversed(buffer_):
        l =":".join([str(lista_[0]), lista_[1]])
        expande_.append(re.sub("\n","", l))
    f = "\n".join(expande_)    
    return f

def carga_el_buffer_(buffer_, selec_):
    try:
        for row in buffer_:
            if selec_ in row:
                b = row
            else:
                pass
        return b
    except:
        subprocess.call(['notify-send', 'Ups! ocurrio un error...'])

def expand_buffers_():
    with open(f"{ruta_}/.xs_historial_.pickle", 'rb') as pickle_:
        try:
            buffer_ = pickle.load(pickle_)
            expande_ = formato_menu_(buffer_)
            dmenu_ = subprocess.Popen(['dmenu', '-l', '20','-p', 'pegar'],stdin=subprocess.PIPE,
            stdout=subprocess.PIPE).communicate(input=expande_.encode())
            try:
                selec_ = int(list(bytearray(dmenu_[0]).decode('utf-8').partition(":"))[0])
                buffer_cargado = carga_el_buffer_(buffer_, selec_)[1]
                pegar = subprocess.Popen(['xclip','-selection', 'clipboard', '-i'],
                stdin=subprocess.PIPE).communicate(input=buffer_cargado.encode())
                try:
                    k_ontrol_.press(keyboard.Key.ctrl)
                    k_ontrol_.press('v')
                    k_ontrol_.release('v')
                    k_ontrol_.release(keyboard.Key.ctrl)
                except:
                    subprocess.call(['notify-send', 'Error! al precionar'])
            except:
                pass
        except:
            colibri = subprocess.call(['notify-send', 'Historial vacio...'])

"""                     ==> Eliminacio  del historial y salida del sistema <==                         """

def apagado_(*_):
    try:
        dev_null.close()
        stdin_cierre.close()
        os.remove(f"{ruta_}/.xs_historial_.pickle")
        os.kill(os.getpid(),signal.SIGINT)
        sys.exit()
    except FileNotFoundError:
        sys.exit()

#                                    """ ==> Parser Xs-menu <== """

Xs_menu_parcer = argparse.ArgumentParser(
    prog = """      Xs-menu""",
    formatter_class = argparse.RawDescriptionHelpFormatter,
    add_help = False,
    description = """          simple X menu D""",
    epilog = "Echo por Xivalva_z",
)
Xs_menu_parcer.add_argument("-v", "--version", action=("version"), version=("Xs-menu 0.0.1"), help=("version"))
Xs_menu_parcer.add_argument("-h", "--help", action=("help"), help=("""<ctrl>+<Alt>+m, despliega el menu de opciones,
selecciona con las teclas arriba, Abajo y preciona enter para pegar.
Cierra el servicio con <ctrl>+ñ """))
Xs_menu_parcer.add_argument("-azul", help=("color azul"))
config_ = Xs_menu_parcer.add_subparsers(title="configuracion",dest="config", help=" otra ayuda")
config_.add_parser("color",)
xs_config_ = Xs_menu_parcer.parse_args()

if __name__ == '__main__':
    dev_null= open(os.devnull, 'w')
    sys.stdout = dev_null
    sys.stderr = dev_null
    stdin_cierre =  open(os.devnull, 'r')
    sys.stdin = stdin_cierre
    historial_buffers_()
    monitor = threading.Thread(name="Xs-menu_Daemon_", target=Xs_menu_Daemon_)
    monitor.start()
    hotkeys_cntrol_ = keyboard.GlobalHotKeys({'<Ctrl>+<Alt>+m': expand_buffers_, '<Ctrl>+ñ': apagado_})
    hotkeys_cntrol_.start()
    signal.signal(signal.SIGTERM, apagado_)

#                                       ==> xivalvaz@proton.me <==