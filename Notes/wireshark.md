# DPDK и пожелания известных лиц
- [EcoNAT](https://www.rdp.ru/products/econat.html) — ориентированный на операторов продукт, способный решить вопрос нехватки адресов IPv4 при сохранении существующей IPv4 инфраструктуры и в перспективе плавной миграции на IPv6.
- [DPDK](http://dpdk.org/). DPDK is a set of libraries and drivers for fast packet processing.
It is designed to run on any processors. The first supported CPU was Intel x86 and it is now extended to IBM POWER and ARM.
It runs mostly in Linux userland. A FreeBSD port is available for a subset of DPDK features.
- [Что такое Intel DPDK?](https://sdnblog.ru/what-is-intel-dpdk/)
- [DPDK Packet Capture (PDUMP)](https://www.napatech.com/dpdk-packet-capture-pdump/)
- [Data Plane Development Kit (DPDK) Packet Capture Framework](https://software.intel.com/en-us/articles/dpdk-packet-capture-framework)
- [Positioning PF_RING ZC vs DPDK](http://www.ntop.org/pf_ring/positioning-pf_ring-zc-vs-dpdk/). Posted February 16, 2017

# Dynatrace Video
- [Dynatrace AI, Fullstack Monitoring Demo at AWS Sydney](https://www.youtube.com/watch?v=CSf89W2iNJQ). Опубликовано: 11 апр. 2017 г.
- [Why we love Dynatrace AppMon 7](https://www.youtube.com/watch?v=Jgwb_kmCbrY) Опубликовано: 5 апр. 2017 г.

# Packetbeat
- [Packetbeat - Lightweight Shipper for Network Data](https://www.elastic.co/products/beats/packetbeat)
Know what’s going on across your applications by tapping into data traveling over the wire. Packetbeat is a lightweight network packet analyzer that sends data to Logstash or Elasticsearch.
- [Попробуйте Packetbeat](http://bulimov.ru/it/try-packetbeat/). Вчера в блоге Elasticsearch появилась отличная новость - проект Packetbeat, развиваемый до этого энтузиастами, присоединился к Elastic. Я уже довольно давно слежу за этим проектом, и теперь, когда можно не беспокоиться о его будущем, хочу о нем рассказать. Packetbeat это такой инструмент мониторинга, который работает как анализатор сетевых пакетов, парсит различные протоколы (сейчас поддерживаются HTTP, MySQL, Postgresql, Redis, Thrift-RPC), получает нужные данные, и отсылает их либо напрямую в Elasticsearch, либо в Redis, из которого данные будет забирать Logstash и класть их все в тот же Elasticsearch.
- [M/Monit 3.7.0](https://mmonit.com/)
Easy, proactive monitoring of Unix systems, network and cloud services. Conduct automatic maintenance and recovery and execute meaningful causal actions in error situations.

# Moloch
- [Moloch is a large scale, open source, full packet capturing, indexing, and database system.](http://molo.ch/)
Moloch is not meant to replace Intrusion Detection Systems (IDS). Moloch augments your current security infrastructure by storing and indexing network traffic in standard PCAP format, while also providing fast indexed access. Moloch is built with an intuitive UI/UX which reduces the analysis time of suspected incidents.
	- 

# Эксперименты с Wireshark
- [How to filter by IP address in Wireshark?](http://stackoverflow.com/questions/4043406/how-to-filter-by-ip-address-in-wireshark).
If you only care about that particular machine's traffic, use a capture filter instead, which you can set under Capture -> Options.
- [Wireshark Sample Captures](https://wiki.wireshark.org/SampleCaptures)

# SQL
- [How can I decode SQL Server traffic with wireshark?](http://stackoverflow.com/questions/2023589/how-can-i-decode-sql-server-traffic-with-wireshark)
- [DRDA: Unraveling the DB2 Decodes](http://thenetworkguy.typepad.com/nau/2009/06/drda-unraveling-the-db2-decodes.html)
- [Understanding the DRDA protocol in DB2 using Wireshark](https://www.ibm.com/developerworks/community/blogs/dylanskillsharing/entry/understanding_the_drda_protocol_in_db2_using_wireshark?lang=en)
- [Microsoft Message Analyzer](https://www.microsoft.com/en-us/download/details.aspx?id=44226) enables you to capture, display, and analyze protocol messaging traffic; and to trace and assess system events and other messages from Windows components.
- [Decoding (encrypted) MySQL traffic with Wireshark](http://databaseblog.myname.nl/2014/07/decoding-encrypted-mysql-traffic-with.html)

# Shark
- [TShark - консольная версия программы Wireshark](https://zyxel.ru/kb/2037/)
- [Анализ сетевого трафика на сервере с помощью tshark](https://habrahabr.ru/company/selectel/blog/233837/)

- [MonitoringScape](https://bigpanda.io/monitoringscape/) is your guide to the new, exciting world of modern monitoring. Keep in mind that this is a community resource, so your comments and suggestions are very welcome.

# PCAP
- [Win10Pcap: WinPcap for Windows 10 (NDIS 6.x driver model)](http://www.win10pcap.org/)
	- [How to use Win10Pcap](http://www.win10pcap.org/howto/). Simply install Win10Pcap on your Windows PC, either before or after your favorited WinPcap-compatible applications (e.g. Wireshark).
- [libtins - packet crafting and sniffing library](http://libtins.github.io/)
- [15 Best Free Packet Crafting Tools](http://resources.infosecinstitute.com/15-best-free-packet-crafting-tools/). POSTED IN GENERAL SECURITY, HACKING, PENETRATION TESTING ON JANUARY 4, 2017
- [Dev Dungeon. Packet Capture, Injection, and Analysis with Gopacket](http://devdungeon.com/content/packet-capture-injection-and-analysis-gopacket)

# APM
- [AppDynamics vs Dynatrace: Battle of the Enterprise Monitoring Giants](http://blog.takipi.com/appdynamics-vs-dynatrace-battle-of-the-enterprise-monitoring-giants/)