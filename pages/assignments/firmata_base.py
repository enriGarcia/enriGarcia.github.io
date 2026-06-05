#!/usr/bin/env python3
"""
firmata_base.py
Código base auxiliar para conectar y desconectar de forma segura una placa Arduino UNO
que ejecuta StandardFirmata, utilizando la biblioteca pyFirmata.
"""

import sys
import time
import pyfirmata2 as pyfirmata

class ArduinoConnection:
    """
    Un administrador de contexto (context manager) para conectar y desconectar
    de forma segura una placa Arduino.
    
    Ejemplo de uso:
        from firmata_base import ArduinoConnection
        
        with ArduinoConnection(port='COM3') as board:
            # Tu código de pyFirmata aquí
            # ej. pin = board.get_pin('d:13:o')
            # pin.write(1)
    """
    def __init__(self, port='COM3'):
        self.port = port
        self.board = None
        self.iterator = None

    def __enter__(self):
        print(f"Intentando conectar al Arduino en el puerto '{self.port}'...")
        try:
            # Inicializar la conexión con el Arduino
            self.board = pyfirmata.Arduino(self.port)
            
            # Iniciar el hilo del iterador (Iterator) para evitar el desbordamiento
            # del búfer serial y manejar correctamente las lecturas analógicas/digitales
            self.iterator = pyfirmata.util.Iterator(self.board)
            self.iterator.start()
            
            # Permitir un breve tiempo para que la conexión se estabilice
            time.sleep(0.5)
            print("¡Conexión exitosa con el Arduino UNO!")
            return self.board
            
        except Exception as e:
            print("\n" + "="*60, file=sys.stderr)
            print("¡ERROR: Falló la conexión con el Arduino!", file=sys.stderr)
            print(f"Detalles: {e}", file=sys.stderr)
            print("="*60, file=sys.stderr)
            print("\nLista de verificación para solución de problemas en Windows:", file=sys.stderr)
            print("1. ¿Está el Arduino UNO conectado a tu computadora mediante el cable USB?", file=sys.stderr)
            print("2. ¿Es correcto el puerto COM? Verifica en el 'Administrador de dispositivos'", file=sys.stderr)
            print("   de Windows (bajo 'Puertos (COM y LPT)') y ajusta el parámetro 'port=' en tu código.", file=sys.stderr)
            print("3. ¿Has cerrado el 'Monitor Serie' del IDE de Arduino? Si está abierto,", file=sys.stderr)
            print("   estará bloqueando el puerto COM e impedirá que Python se conecte.", file=sys.stderr)
            print("4. ¿Has cargado el sketch 'StandardFirmata' en el Arduino usando el IDE de Arduino", file=sys.stderr)
            print("   (Archivo -> Ejemplos -> Firmata -> StandardFirmata)?", file=sys.stderr)
            print("="*60 + "\n", file=sys.stderr)
            sys.exit(1)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.board:
            print("\nCerrando la conexión con la placa Arduino...")
            try:
                # El método exit() cierra el puerto serial de manera segura.
                self.board.exit()
                print("Conexión con Arduino cerrada de forma segura.")
            except Exception as e:
                print(f"Advertencia: Error al cerrar la conexión: {e}", file=sys.stderr)

if __name__ == '__main__':
    # Prueba rápida cuando se ejecuta el script directamente
    print("Probando la plantilla ArduinoConnection...")
    with ArduinoConnection() as board:
        print("¡Conexión de prueba establecida con éxito!")
        try:
            # pyFirmata guarda el nombre del firmware en 'board.firmware'
            # y la versión en 'board.firmware_version' (en formato de tupla, ej. (2, 5))
            version_str = f"{board.firmware_version[0]}.{board.firmware_version[1]}"
            print(f"Firmware detectado: {board.firmware} (Versión v{version_str})")
        except Exception as e:
            print("No se pudieron obtener los detalles del firmware:", e)
        print("Saliendo del bloque de prueba...")
