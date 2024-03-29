# Запускаем TTN
## Конфигурация
Терминал построен на Arduino Pro Mini (ATmega 328, 3.3V). Для правильной диагностики через COM порт необходимо корректно выставлять частоту в IDE.
Модем -- [AnyLink lora DP1276](http://www.eltech.spb.ru/news/radiomodul_dp1276_dlya_diapazona_433868915_mgc_s_dalnostyu_raboti_do_12_km_ot_anylink)
Тема работы с децибелами хорошо освещена в книге "И.П. Шелестов. Радиолюбителям. Полезные схемы. Книга 3", п. 6.1. Перевод величин из децибелов в абсолютные значения, стр. 206 (смотрим djvu с аналогичным названием).

What is RSSI and what does it mean for a WiFi network?

RSSI, or “Received Signal Strength Indicator”, is a measurement of how well your device can hear a signal from an access point or router. It’s a value that is useful for determining if you have enough signal to get a good wireless connection.

- Доступ к нашему тестовому устройству в TTN: [Device Overview](https://console.thethingsnetwork.org/applications/test_zond/devices/test_device)
- Готовим строчку для передачи Payload: [ASCII to Hex ...and other free text conversion tools](http://www.asciitohex.com/) 

## Разбираем код LMIC
- расположение текущих экспериментов: 'D:\iwork.GH\Arduino.projects\02 LoRa-test-APM\ttn-otaa\ttn-otaa.ino'
- Что такое макрос F? [The hidden Arduino Macro F() fixes random lock ups](https://www.baldengineer.com/arduino-f-macro.html).
[Why is the F() Macro Needed?](http://playground.arduino.cc/Learning/Memory)
- Что такое LMIC? Ответ находим в документации на "LMiC-v1.5" 2.4 The LMIC Struct
Instead of passing numerous parameters back and forth between API and callback functions, information about the protocol state can be accessed via a global LMIC structure as shown below. Определяется он через #define в oslmic.h: `#define DEFINE_LMIC  struct lmic_t LMIC`
- Что за цифирьки выводятся в логе "engineUpdate, opmode=0x..."? Ответ можем найти в файле `lmic.h`: MAC operation modes.
- Читаем дебаг строчку `"%lu: RXMODE_SINGLE, freq=%lu, SF=%d, BW=%d, CR=4/%d, IH=%d\n"`. Детали в `radio.c` ~590 строчка. Частично ответ находим в файле `lorabase.h`:
```
// Radio parameter set (encodes SF/BW/CR/IH/NOCRC)
enum _cr_t { CR_4_5=0, CR_4_6, CR_4_7, CR_4_8 };
enum _sf_t { FSK=0, SF7, SF8, SF9, SF10, SF11, SF12, SFrfu };
enum _bw_t { BW125=0, BW250, BW500, BWrfu };
```
По сути параметров читаем мануал Semtech ["LoRa Modem Designer’s Guide"](https://www.semtech.com/images/datasheet/LoraDesignGuide_STD.pdf).
	- CR = Chip (Coding) Rate (2.4 BW and Chip Rate)
	- SF = Spreading Factor
	- BW = Bandwidth (2.4 BW and Chip Rate)

и [Semtech Corporation LoRa® FAQ](http://www.semtech.com/wireless-rf/lora/LoRa-FAQs.pdf)
*20.) How do you choose the LoRa® Bandwidth (BW), Spreading factor (SF) and Coding Rate (CR)* ? LoRaWAN™ uses primarily the 125kHz BW setting but other proprietary protocols can utilize other BW settings. 
Changing the BW, SF, and CR changes the link budget and time on air, which results in a battery lifetime vs range tradeoff.
Please use the LoRa Modem Calculator to evaluate the tradeoffs.
	
- Еще раз смотрим на мануал по запуску LoRaWAN: [LoRaWAN IoT with Arduino Uno,
Dragino v1.3 & TheThingsNetwork](http://www.tamberg.org/chopen/2016/LoRaWANIoTWorkshop.pdf) Из мануала выше получаем ответ как же выцепить полученные на стороне Arduino данные (слайд 65 "Receiving data  on the Arduino")
- Что за время выводится в debug log? Ответ -- данные от функции `os_getTime()`. Детали по функции см. в "LMiC-v1.5"
2.2.5 ostime_t os_getTime()
Query absolute system time (in ticks).
```
ostime_t os_getTime () {
	return hal_ticks();
      }
```
Есть функция `sec2osticks()` (точнее, #define, определенный в `oslmic.h`), которая переводит секунды в тики ОС arduino.
Там же определена обратная функция `osticks2ms(os)`
- Каким образом напечатать в Serial содержимое буфера `uint8_t`? У нас тестовые данные на передачу лежат в таком виде ("Hello World").
	- The `uint8_t` is a unsigned integer on 8 bits. In Arduino, it's called a "byte". 
	- Смежный вопрос [How to send an int over uint8_t data?](http://stackoverflow.com/questions/24588234/how-to-send-an-int-over-uint8-t-data)
	- [Determine size of uint8_t* and convert to ASCII?](http://forum.arduino.cc/index.php?topic=37877.0)

В принципе, вариантов множество. Один из оптимальных ответов выглядит следующим образом:
```
 // Serial.write(mydata); // https://www.arduino.cc/en/Serial/write
 Serial.write("Simple Hello\n");
 Serial.write(mydata, strlen(mydata));
```


## Вывод в COM порт. Особенности
- [Русский текст в монитор порта. Сбой кодировки.](http://arduino.ru/forum/obshchii/russkii-tekst-v-monitor-porta-sboi-kodirovki)
- [Arduino Serial Monitor Pro (Ардуино Монитор Порта Про)](http://arduino.on.kg/serialMonitor)
- [Как отправлять русский текст в сериал порт](http://blog.iarduino.ru/page/kak-otpravlyat-russkiy-tekst-v-serial-port/)

## Шаги по запуску
- Для разводки используем пример [Build the cheapest possible node yourself](https://www.thethingsnetwork.org/labs/story/build-the-cheapest-possible-node-yourself) by Martijn Quaedvlieg.
- Используем библиотеку [LoraWAN-in-C library, adapted to run under the Arduino environment](https://github.com/matthijskooijman/arduino-lmic)
- Из директории `examples` берем скетч `ttn-otaa`
- Включаем вывод диагностических сообщений. Библиотека 'lmic/config.h': Установить `LMIC_DEBUG_LEVEL` в уровень 2 и раскомментировать строку `//#define LMIC_PRINTF_TO Serial`
- Добавим дополнительный диагностический вывод по проверке версии радиочипа
```
 // some sanity checks, e.g., read version number
    u1_t v = readReg(RegVersion);
    printf("%o\n", v);
```
- Проверяем, как устроен ресет радиомодема. У нас модем sx1276, макрос определен в `config.h`. Код из `\libraries\arduino-lmic-master\src\lmic\radio.c`
```
     671  void radio_init () {
     672      hal_disableIRQs();
     673  
     674      // manually reset radio
     675  #ifdef CFG_sx1276_radio
     676      hal_pin_rst(0); // drive RST pin low
     677  #else
     678      hal_pin_rst(1); // drive RST pin high
     679  #endif
```
Подобная ошибка обсуждается на форуме TTN: [HOPERF95W on Arduino MEGA - not working](https://www.thethingsnetwork.org/forum/t/hoperf95w-on-arduino-mega-not-working/718). Можно заглянуть еще в блок 'Pin mapping'
- Не до конца понятно, что такое floating состояние. Видимо, просто висящий конец. Но не понятно, как это осуществляется путем установки rst в 2. К сведению, полезная публикация, проливающая свет на вопрос плавающих входов: [Arduino Internal Pull-Up Resistor Tutorial. Make pushbuttons behave with one simple keyword]()https://www.baldengineer.com/arduino-internal-pull-up-resistor-tutorial.html). А также, видео [Floating Pins, Pull-Up Resistors and Arduino](https://programmingelectronics.com/floating-pins-pull-up-resistors-and-arduino/) и комиксы [AVR. Учебный курс. Устройство и работа портов ввода-вывода](http://easyelectronics.ru/avr-uchebnyj-kurs-ustrojstvo-i-rabota-portov-vvoda-vyvoda.html).
- Новая напасть. Используемый FTDI переходник [SparkFun FTDI Basic Breakout - 3.3V](https://www.sparkfun.com/products/9873) сильно греется при подключении платы радиомодуля. Последняя так и не заводится. Возможно, что не хватает питания, о этом есть отдельные комментарии по приведенной выше ссылке.
- Примеры терминальных скетчей различной функциональности на базе LMiC можно взять в этом репозитории: [Software for an RFM95W based TTN node](https://github.com/tijnonlijn/RFM-node). Там же лежит [Lightweight low power library for Arduino](https://github.com/tijnonlijn/RFM-node)
- Для оценки передаваемого объема данных полезно ознакомиться с Semtech LoRa Calculator и его производными. LoRaWAN != LoRa, поэтому лучше начать с этого форума: [LoRa Calculator with LoRaWAN](http://openlora.com/forum/viewtopic.php?t=914).
- Для конвертации ascii payload в hex можно использовать онлайн-ресурсы, например, 
[ASCII to Hex ...and other free text conversion tools](http://www.asciitohex.com/)
- Неплохая статья по диагностированию TCP соединений. [How to prepare TCP](https://habrahabr.ru/company/billing/blog/252819/)
- Хорошие [Protocol CheatSheets](http://packetlife.net/library/cheat-sheets/)
- [TCP Selective Acknowledgments (SACK)](http://packetlife.net/blog/2010/jun/17/tcp-selective-acknowledgments-sack/)
 


# Интерфейсы
- [Интерфейс JTAG? — Это очень просто!](https://habrahabr.ru/post/190012/)
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
- Детальный тред на TTN по запуску Node. [Over-the-air-activation OTAA with LMIC](https://www.thethingsnetwork.org/forum/t/over-the-air-activation-otaa-with-lmic/1921/7)
- Тред [Arduino LMIC library updated](https://www.thethingsnetwork.org/forum/t/arduino-lmic-library-updated/1295) by matthijs

## LmIc FAQ
Q: Каким образом можно изменить настройку диагностических сообщений библиотеки?
A: Библиотека 'lmic/config.h'. Установить `LMIC_DEBUG_LEVEL` в уровень 2 и раскомментировать строку `//#define LMIC_PRINTF_TO Serial`

Q: Что такое PIR?
A: PIR - Passive infrared sensor


# Arduiono & PIC
- [Arduino Pro Mini](http://arduino.ua/ru/hardware/ProMini)
- [Arduino Pro Mini — распиновка и характеристики](http://skproj.ru/arduino-pro-mini-raspinovka-i-harakteristiki/)
- [10 Ways to Destroy An Arduino](https://www.rugged-circuits.com/10-ways-to-destroy-an-arduino/)
- [Feeding power to Arduino: the ultimate guide](https://www.open-electronics.org/the-power-of-arduino-this-unknown/)
- Очень хорошая демонстрация, как отличается работа с портами от работы с регистром напрямую. СКОРОСТЬ!!!! [Tutorial: Arduino Port Manipulation](http://tronixstuff.com/2011/10/22/tutorial-arduino-port-manipulation/)
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
- [Pirio. LoRa PIR Sensor](http://allorafactory.com/pirio/) Accurate motion monitoring.
- [Пироэлектрический инфракрасный (PIR) датчик движения и Arduino](http://arduino-diy.com/arduino-piroelektricheskiy-infrakrasnyy-PIR-datchik-dvizheniya)


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