---
layout: page
title: Instalación de hardware y software para las prácticas.
description: Instalación de hardware y software para el microcontrolador.
---
> Este tutorial es para usuarios de Windows.

# Índice
- [Lista de materiales](#lista-de-materiales)
- [Instalación del software](#instalación-del-software)
- [Cableado del circuito base](#cableado-del-circuito-base)


# Lista de materiales
[Volver al Índice](#índice)

| Cantidad | Dispositivo | Descripción |
|---|---|---|
| 1 | ATmega328P-PU | Microcontrolador AVR RISC 8-bit 20 Mhz |
| 1 | Grabador USBasp | Grabador de microcontroladores AVR 8-bit |
| 1 | Protoboard | |
| 1 | Regulador L7805CV | Regulador de voltaje 5.0V 1A |
| 4 | Capacitor cerámico 0.1uF 50V | Código: 104 |
| 1 | Capacitor electrolítico 470uF 25V | Tolerancia ± 20% |
| 1 | Capacitor electrolítico 220uF 25V | Tolerancia ± 20% |
| 4 | Capacitor electrolítico 1uF 25V | Tolerancia ± 20% |
| 10 | Resistencia de 330Ω 1/4W | Código: naranja, naranja, café, oro |
| 5 | Resistencia de 1kΩ 1/4W | Código: café, negro, rojo, oro |
| 5 | Resistencia de 10kΩ 1/4W | Código: café, negro, naranja, oro |
| 4 | Resistencia de 220Ω 1/4W | Código: rojo, rojo, café, oro| 
| 3 | Potenciómetros de 10kΩ | Tipo preset horizontal de 10 mm |
| 3 | Push button (microswitch) | Tipo push, 2 terminales |
| 2 | Transistores BC547 | Transistor NPN |
| 2 | Metros de alambre para protoboard | Calibre AWG 22 |
| 10 | Led de 5mm difuso | Color rojo|
| 1 | Dip-switch de 4 vías | |
| 2 | Display de 7 segmentos ánodo común | Color rojo fondo negro |
| 1 | Pantalla LCD alfanumérica 16x2 | 16 pines |
| 1 | Sensor de temperatura LM35 | Encapsulado TO-92|
| 2 | Sensores CNY70 | Sensor reflectivo óptico |
| 2 | Controlador de motor L293D | Puente-H Doble |
| 1 | CI Max232 | Circuito integrado para comunicación serial |
| 1 | Módulo Bluetooth Serial UART | BT_BOARD V1.02 |
| 1 | Receptor Bluetooth USB para PC | Requerido para la PC |
| 2 | Motores de CD | Voltaje de 6V a 12V DC|
| 1 | Elminador de voltaje 12V 1.5A | Fuente de alimentación | 


# Instalación del software
[Volver al Índice](#índice)

1. Ejecutar Windows Update antes de iniciar la instalación.
2. Descargar e instalar [Atmel Studio 7](http://www.microchip.com/mplab/avr-support/atmel-studio-7), preferentemente usando el instalador _web_. 
3. Descargar [Codevision AVR](http://www.hpinfotech.ro/cvavreval.zip).
4. Descomprimir el archivo descargado `cvavreval.zip` e iniciar el instalador `CodeVisionAVR.msi`
5. En tal caso de que CodeVisionAVR no inicie, puede ser problema del Antivirus instalado. Cheque la siguiente [información](http://www.hpinfotech.ro/cvavr_download.html#wb_Text1).
6. Descargar el controlador [Zadig](http://zadig.akeo.ie/downloads/zadig-2.3.exe) de la tarjeta Usbasp.
7. Inserte la tarjeta Usbasp al puerto USB de la computadora.
8. Ejecute el archivo descargado `zadig-2.3.exe`. En el menú elija la opción `Options>List All Devices`
9. Deje las opciones como se muestran en la imagen:
![Opciones de Zadig](https://raw.githubusercontent.com/enriGarcia/microcontroladores/master/images/zadigOptions.png)
10. Seleccione `Replace Driver`.
11. Descargue el software para grabación [Extreme Burner AVR](
http://digital-wizard.net/files/extreme_burner_avr_v1.4.3_setup.exe) y ejecute el archivo descargado `extreme_burner_avr_v1.4.3_setup.exe`
12. Con la tarjeta Usbasp conectada, inicie Extreme Burner AVR. En el menú seleccione `Settings>Programming Mode>ISP`. Después elija `Erase>Chip Erase`. Extreme Burner AVR tratará de borrar el microcontrolador, y al no encontrarlo mostrará varios errores pero al menos habrá reconocido a la tarjeta Usbasp. 
![Reconocimiento de la tarjeta Usbasp](https://raw.githubusercontent.com/enriGarcia/microcontroladores/master/images/extremeUsbasp.png)
13. Ahora el software estará completamente instalado y funcionará correctamente.


# Cableado del circuito base
[Volver al Índice](#índice)
El circuito base es lo mínimo necesario para comenzar a realizar las prácticas, después de ejecutar estos pasos usted podrá grabar su microcontrolador sin problemas.

## Conexión de la fuente de alimentación
1. Conecte el siguiente diagrama:

![Circuito de alimentación](https://raw.githubusercontent.com/enriGarcia/microcontroladores/master/images/sourceCircuit.png)

2. Conecte su fuente de alimentación. Con un multímetro cheque que realmente `Vcc` tenga el valor de `5.0V`. Si no es así, revise sus conexiones.

## Conexión de la tarjeta Usbasp
1. Desconecte la fuente de alimentación. Complete el circuito anterior de acuerdo al siguiente diagrama, a este circuito lo llamamos _Circuito base_:

![Circuito base](https://raw.githubusercontent.com/enriGarcia/microcontroladores/master/images/baseCircuit.png)

2. Los pines del conector de 10-pin de la tarjeta Usbasp tienen las siguientes señales, tenga cuidado al conectar, guíese por la muesca del conector.

![Descripción de pines](https://raw.githubusercontent.com/enriGarcia/microcontroladores/master/images/usbaspPinout.png)

3. Revise de nuevo sus conexiones. Conecte de nuevo la fuente de alimentación e inicie Extreme Burner AVR. En el menú seleccione `Chip>ATmega328P`. Después elija `Erase>Chip Erase`. Extreme Burner AVR borrará la memoria del microcontrolador:

![Borrado con éxito](https://raw.githubusercontent.com/enriGarcia/microcontroladores/master/images/eraseSucces.png)

4. Ha completado con éxito la conexión del circuito base.

![Circuito base en protoboard](https://raw.githubusercontent.com/enriGarcia/microcontroladores/master/images/imgProto.jpg)


<!-- Note: this is how to write a comment in HTML. Everything in here won't show up on your webpage.-->

<!--
To increase the size of the title, use fewer # in front of the paper title.
To decrease the size of the title, use more #. 
To remove the italics, remove the * before and after the description
To remove the underline from the title, remove the <u> tags (<u> and </u>)
-->
