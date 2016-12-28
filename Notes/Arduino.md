# Интерфейсы
- [Обзор шины SPI и разработка драйвера ведомого SPI устройства для embedded Linux (Часть первая, обзорная)](https://habrahabr.ru/post/123145/)
	- Что это за статья?
Эта статья представляет собой компиляцию информации из различных источников, вольный перевод некоторых частей документации, а также мои собственные комментарии, дополнения и описания возникших проблем.
	- Для кого эта статья?
В первую очередь, для новичков, каковым являюсь и я. На форумах по embedded Linux очень часто можно встретить вопрос: «А как на этой плате работать с SPI?». Именно на него я и попытаюсь дать ответ. В качестве примера, я приведу код написанный для работы с моим тестовым SPI устройством.
Существует четыре режима работы SPI устройств. Как правило, именно они вызывают больше всего путаницы у новичков. Данные четыре режима представляют собой комбинацию двух бит: CPOL & CPHA
![SPI modes Oscilogramm](https://habrastorage.org/getpro/habr/post_images/b3f/cc5/435/b3fcc5435f56489815c50fbb7581049e.png)

# Запуск LoRaWAN на Arduino Pro Mini и AnyLink lora модема
- [Pro Mini node working plus 2 updated LMIC library versions w/examples](https://www.thethingsnetwork.org/labs/story/pro-mini-node-working-plus-2-updated-lmic-library-versions-wexamples)
- [LoraWAN-in-C library, adapted to run under the Arduino environment](https://github.com/matthijskooijman/arduino-lmic)
- [dlarue/LoRa-LMIC-1.51 forked from things4u/LoRa-LMIC-1.51](https://github.com/things4u/LoRa-LMIC-1.51)
- А тут есть примерчики: [Software for an RFM95W based TTN node](https://github.com/tijnonlijn/RFM-node)
- [Что такое DevEUI?](http://lorawan.lace.io/sp_faq/deveui/)
- [Что такое Over-the-Air Activation — активация «по воздуху»?](http://lorawan.lace.io/sp_faq/otaa/)
При нахождении end-node в зоне покрытия сети возможна активация «по воздуху» (OTAA), которая происходит путем отправки конечным узлом запроса на присоединение (join-request) и получения разрешение на подключение (join-accept). Для успешного прохождения процедуры активации OTAA оператор сети LoRaWAN должен внести запись в специальную таблицу маршрутизации, в которой идентификатор приложения AppEUI будет соответствовать приложению на сервере (App Server) сервис-провайдера.
- [Что такое DevAddr?](http://lorawan.lace.io/sp_faq/devaddr/)
DevAddr — 32-битный (четырехбайтный) сетевой адрес для адресации пакетов на сетевом уровне, имеет уникальное значение в пределах сети оператора (можно провести аналогию c MAC адресом, который тоже обеспечивает адресацию на 2 уровне модели OSI в сетях Ethernet, но способ получения DevAddr при OTAA сходен с получением динамического IP адреса, получаемого от DHCP сервера в TCP/IP сетях). Старшие 7 бит DevAddr содержат адрес сети оператора NwkID, это значение должно быть уникальными для находящихся рядом сетей и для сетей, имеющих перекрывающиеся зоны покрытия. Чаще всего, для обозначения DevAddr, используют четырехбайтную последовательность, например: 02:D1:D2:01, в которой старший байт является адресом сети NwkID (если снова проводить аналогию, то адрес сети оператора NwkID аналогичен трехбайтному коду изготовителя сетевого оборудования в MAC адресах в Ethernet сетях).
- [Методика расчета температуры по сопротивлению термометров сопротивления](http://temperatures.ru/pages/raschet_temperatury)

# Arduiono & PIC
- [Знакомство с Arduino](http://atroshin.ru/ru/content/znakomstvo-s-arduino)
- [Последовательный порт - TTL и RS232](http://atroshin.ru/ru/content/posledovatelnyy-port-ttl-i-rs232)
- [Alternatives to Standard Arduino IDE: Which One To Choose?](https://www.intorobotics.com/alternatives-standard-arduino-ide-one-choose/)
- [Почему я не люблю Arduino](http://microsin.net/programming/avr/why-i-hate-arduino.html)
- [Arduion homepage](https://www.arduino.cc/)
- [AVR. Учебный курс. Устройство и работа портов ввода-вывода](http://easyelectronics.ru/avr-uchebnyj-kurs-ustrojstvo-i-rabota-portov-vvoda-vyvoda.html)
- [Виртуальный COM порт для Windows 7](http://answit.com/virtualnyiy-com-port-dlya-windows-7/)
	- [Advanced Virtual COM Port](http://www.advancedvirtualcomport.com/)
	- [VIRTUAL SERIAL PORTS EMULATOR](http://www.eterlogic.com/Products.VSPE.html)
- [Программирование Ардуино](http://arduino.ua/ru/prog/)
Язык программирования устройств Ардуино основан на C/C++ и скомпонован с библиотекой AVR Libc и позволяет использовать любые ее функции. Вместе с тем он прост в освоении, и на данный момент Arduino — это, пожалуй, самый удобный способ программирования устройств на микроконтроллерах.
- [Программируем Arduino на чистом Си](https://habrahabr.ru/post/247663/)
- [Я презираю Arduino](https://geektimes.ru/post/255760/)
- [Arduino Pro Mini](http://arduino.ru/Hardware/ArduinoBoardProMini) или [тут](http://arduino-diy.com/arduino-pro-mini)
- [Arduino Pro Mini (Eng)](https://www.arduino.cc/en/Main/ArduinoBoardProMini)
- [Интерфейс I2C](http://robocraft.ru/blog/communication/780.html)
- [Описание шины I2C](http://www.itt-ltd.com/reference/ref_i2c.html)
- [Термистор и Arduino](http://arduino-diy.com/arduino-thermistor)
- [:: Shield Pin Usage ::](http://playground.arduino.cc/Main/ShieldPinUsage)
- [Moteino](https://lowpowerlab.com/guide/moteino/) is a low cost low-power open-source wireless Arduino compatible development platform based on the popular ATmega328p chip used in traditional Arduinos, making it 100% compatible with the Arduino IDE (programming environment).
- [RFM69HW transceiver](https://lowpowerlab.com/shop/rfm69hw)
- LowPowerLab/RFM69 [RFM69 library for RFM69W, RFM69HW, RFM69CW, RFM69HCW (semtech SX1231, SX1231H)](https://github.com/LowPowerLab/RFM69)
- [Smallest expected node](https://www.thethingsnetwork.org/forum/t/smallest-expected-node/568/17)
Are you using an RFM96W? The IBM LMIC library does not support the 433 Mhz band.
The error you're getting either implies the SPI bus in not working (don't cross-connect mosi/miso, but follow the connections as on the wiki), or the RFM96W has another version identifier than the RFM95W (=SX1276).
- COOL! [Adafruit RFM69HCW and RFM9X LoRa Packet Radio Breakouts. Radio transceiver modules for long distance data communication](https://learn.adafruit.com/adafruit-rfm69hcw-and-rfm96-rfm95-rfm98-lora-packet-padio-breakouts?view=all#rfm9x-test)
- [RFM96 LoRa radio. Arduino Library](http://www.airspayce.com/mikem/arduino/RadioHead/)
These radios have really excellent code already written, so rather than coming up with a new standard we suggest using existing libraries such as AirSpayce's Radiohead library which also suppors a vast number of other radios
This is a really great Arduino Library, so please support them in thanks for their efforts!
RadioHead RFM9x Library example
To begin talking to the radio, you will need to download the RadioHead library. You can do that by visiting the github repo and manually downloading or, easier, just click this button to download the zip corresponding to version 1.59
Note that while all the code in the examples below are based on this version you can visit the RadioHead documentation page to get the most recent version which may have bug-fixes or more functionality
- [LoRa FeatherWing IOX for Adafruit Feather](http://syncchannel.blogspot.ru/2016/03/lora-featherwing-iox-for-adafruit.html). Once I am done developing boards for the RFM95/96(W) modules, I may turn to a more sophisticated LoRaWAN module, such as the MicroChip RN2903.
- [Lo-Ra - Сообщество разработчиков LoRaWAN LPWAN](http://lo-ra.ru/forum/)


## Проблемы с выводом в Serial
- [Getting Started with the Arduino Leonardo and Micro](https://www.arduino.cc/en/Guide/ArduinoLeonardoMicro). The Leonardo and Micro boards use an ATmega32U4 to offer you more functionalities compared to Uno. In this guide we explain you how to get the board up and running and which are the differences with Uno.
	- Separation of USB and serial communication. On the Leonardo and Micro, the main Serial class refers to the virtual serial driver on the board for connection to your computer over USB. It's not connected to the physical pins 0 and 1 as it is on the Uno and earlier boards. To use the hardware serial port (pins 0 and 1, RX and TX), use Serial1. (See the Serial reference pages for more information.)
- [Serial](https://www.arduino.cc/en/Reference/Serial)
- УРА-А-А!! Проблема с Serial для Pro mini решена!!! Необходимо выставлять правильный тип процессора и частоту в настройках IDE. [Topic: Problem with Serial on Arduino Pro 328 3.3V 8MHz](http://forum.arduino.cc/index.php/topic,46458.0.html)
- [Arduino Pro Micro, get data out of Tx pin?](http://arduino.stackexchange.com/questions/1471/arduino-pro-micro-get-data-out-of-tx-pin)
- [Topic: Arduino pro mini send garbage to serial output](http://forum.arduino.cc/index.php?topic=182136.0)
- Sparkfun
	- [Using the Arduino Pro Mini 3.3V](https://learn.sparkfun.com/tutorials/using-the-arduino-pro-mini-33v)
	- [SparkFun FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/products/9873)
	- [SparkFun USB to serial UART Boards Hookup Guide](https://learn.sparkfun.com/tutorials/sparkfun-usb-to-serial-uart-boards-hookup-guide)
	- COOL! [Serial Communication](https://learn.sparkfun.com/tutorials/serial-communication)
- [Software Serial on arduino pro mini](https://www.thethingsnetwork.org/forum/t/software-serial-on-arduino-pro-mini/3684)
- [Introducing Pro Trinket. Trinket's got a big sister in town - the Pro Trinket 5V!](https://learn.adafruit.com/introducing-pro-trinket/overview)

# Arduino IDE
- [Русский текст в монитор порта. Сбой кодировки.](http://arduino.ru/forum/obshchii/russkii-tekst-v-monitor-porta-sboi-kodirovki)
- [Arduino Serial Monitor Pro (Ардуино Монитор Порта Про)](http://arduino.on.kg/serialMonitor)
- [Как отправлять русский текст в сериал порт](http://blog.iarduino.ru/page/kak-otpravlyat-russkiy-tekst-v-serial-port/)

# Электроника
- [ATmega328](http://www.atmel.com/ru/ru/devices/ATMEGA328.aspx)
- [Чем отличаются друг от друга ATmega328, ATmega328P, ATmega328PU?](http://microsin.net/programming/avr/difference-between-atmega328p-and-atmega328.html)
- COOL! [Полупроводниковая электроника. Электроника для начинающих*  tutorial](https://geektimes.ru/post/253938/). В статье разобраны принципы работы основных полупроводниковых устройств. Описание функционирования изложено с позиции физики. Статья содержит вводное описание терминов, необходимых для понимания материала широкому кругу читателей.
- [Основы на пальцах. Часть 1](http://easyelectronics.ru/osnovy-na-palcax-chast-1.html). Довелось мне однажды преподавать электронику в одной шараге. Нетривиально занятие, скажу я вам. :) Дабы облегчить усвоение материала я вводил ряд упрощений. Совершенно бредовых и антинаучных, но более менее наглядно показывающих суть процесса. Методика «канализационной электрики» успешно показала себя в полевых испытаниях, а посему будет использована и тут. Хочу лишь обратить внимание, что это всего лишь наглядное упрощение, справедливое для общего случая и конкретного момента, чтобы понять суть и к реальной физике процесса не имеющая практически никакого отношения. Зачем оно тогда? А чтобы проще запомнить, что к чему и не путать напряжение и ток и понимать как на все это влияет сопротивление, а то я от студентов такого наслушался…

## IoT
- [Создание интеллектуальных датчиков с использованием сервисов Bluemix Business Rules, Watson IoT Platform и Insights for Weather](https://www.ibm.com/developerworks/ru/library/bpm/1604_siddiqui-bluemix-trs/)
- [OpenLoRa](http://openlora.com/forum/)
- [Lora-net/LoRaMac-node](https://github.com/Lora-net/LoRaMac-node). Reference implementation and documentation of a LoRa network node. The LoRaWAN stack API documentation can be found at: [http://stackforce.github.io/LoRaMac-doc/](http://stackforce.github.io/LoRaMac-doc/)
- [IBM LMIC v1.5 (LoRaWAN in C) adapted to run under the Arduino environment](https://github.com/tftelkamp/arduino-lmic-v1.5)
- [LoraWAN-in-C library, adapted to run under the Arduino environment](https://github.com/matthijskooijman/arduino-lmic)
- COOL! [Port of LMIC-1.5 library tp Atmega 328 and ESP6822, including alternative AES encription library](https://github.com/things4u/LoRa-LMIC-1.51). This library implements the LoRaWAN stack for a LoRa network. It contains the full LoRa stack and works on Teensy platform, ESP8266 and the Ardino Atmega328.
The Library is a port of LMIC-1.5 LoRa library to Arduino/Atmega 328 and the ESP8266, and especially the AES functions are a melt of two existing libraries:
- [Serial Peripheral Interface (SPI)](https://ru.wikipedia.org/wiki/Serial_Peripheral_Interface) — последовательный периферийный интерфейс, шина SPI) — последовательный синхронный стандарт передачи данных в режиме полного дуплекса, предназначенный для обеспечения простого и недорогого высокоскоростного сопряжения микроконтроллеров и периферии. SPI также иногда называют четырёхпроводным (англ. four-wire) интерфейсом.
- [Gateway IMST IC880A / RBPI](https://www.thethingsnetwork.org/forum/t/gateway-imst-ic880a-rbpi/134)
- [TheThingsNetwork/lora_gateway](https://github.com/TheThingsNetwork/lora_gateway). Driver/HAL to build a gateway using a concentrator board based on Semtech SX1301 multi-channel modem and SX1257/SX1255 RF transceivers.
- [TheThingsNetwork/packet_forwarder](https://github.com/TheThingsNetwork/packet_forwarder). A LoRa packet forwarder is a program running on the host of a LoRa gateway that forwards RF packets receive by the concentrator to a server through a IP/UDP link, and emits RF packets that are sent by the server.
- COOL! [Building your LoRa devices](http://cpham.perso.univ-pau.fr/LORA/LoRaDevices.html)
- COOL! [From zero to LoRaWAN in a weekend](https://github.com/ttn-zh/ic880a-gateway/wiki)
- [iC880A - LoRaWAN Concentrator 868MHz](http://www.wireless-solutions.de/products/radiomodules/ic880a)
- [LoRa Modems and Modules](https://www.loriot.io/lora-end-nodes.html). Our aim is to support all the LoRaWAN compliant modems in the LoRa ecosystem. We suggest using either the manufacturer's stack or adapting the IBM's LMiC implementation of the LoRaWAN end device protocol.
- [Address Space in LoRaWAN](https://www.thethingsnetwork.org/wiki/LoRaWAN/Address-Space)
- [IEEE Guidelines for 64-bit Global Identifier (EUI-64)](http://standards.ieee.org/develop/regauth/tut/eui64.pdf)
- [A Closer Look at LoRaWAN and The Things Network](https://www.rs-online.com/designspark/a-closer-look-at-lorawan-and-the-things-network)
- [The Things Network with the Moteino and RN2483](https://github.com/lukastheiler/ttn_moteino)
- COOL! [LoRaWAN IoT with Arduino Uno, Dragino v1.3 & TheThingsNetwork](http://www.tamberg.org/chopen/2016/LoRaWANIoTWorkshop.pdf)
- [How to build your first TTN node: Arduino + RN2483](https://www.thethingsnetwork.org/forum/t/how-to-build-your-first-ttn-node-arduino-rn2483/1574)
- [Make one or more Things as a PoC for LoRa](https://github.com/things4u/LoRa-Thing)

- E32-TTL-100
	- [tienfuc/E32-TTL](https://github.com/tienfuc/E32-TTL/blob/master/E32-TTL.ino)
	- [Topic: Need Wire Diagram/Sample Code for E31-TTL-100 // AX5043 868MHz Transciever](http://forum.arduino.cc/index.php?topic=384828.0)

