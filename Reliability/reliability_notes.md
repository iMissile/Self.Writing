## Доп. материалы для расчета надежности восстанавливаемых устройств
- [Бауманки_нет. Лекции 'Надежность информационных систем'](http://baumanki.net/lectures/10-informatika-i-programmirovanie/350-nadezhnost-informacionnyh-sistem/)
- [Надежность восстанавливаемых контролируемых технических устройств](http://infotest.ru/info085.shtml)
- [8.4. Оценка надежности резервированных систем](http://www.bookasutp.ru/Chapter8_4.aspx). Графики, приведенные на рис. 8.21, иллюстрируют вероятность безотказной работы системы, в которой после отказа одного из элементов не выполняется его замена или ремонт. Если же замена элемента производится сразу, то понятие вероятности безотказной работы теряет значение, поскольку после замены вероятность отказа без замены элемента реализоваться не может. Актуальной становится длительность перехода на резерв, а также продолжительность выполнения горячей замены или восстановления после отказа. Поэтому для обслуживаемых систем автоматизации целью резервирования является обеспечение непрерывности процесса управления или увеличение коэффициента готовности, но не увеличение вероятности безотказной работы. По этим же характеристикам система с голосованием превосходит все остальные.
- [Б5.2 Методы расчета надежности резервированных систем](http://studopedia.org/2-55102.html)
- [Лекция 10. Тема: Расчет надежности восстанавливаемых систем (метод дифференциальных уравнений)](http://baumanki.net/lectures/10-informatika-i-programmirovanie/350-nadezhnost-informacionnyh-sistem/4738-10-raschet-nadezhnosti-vosstanavlivaemyh-sistem.html)

## Полезные расчетники
- [Как вычисляется среднее время до отказа и вероятность безотказной работы?](https://habrahabr.ru/company/nerepetitor/blog/254893/)
- [СКИТ. Расчет надежности](http://tvskit.narod.ru/stati/stati21/stati21.html)
- [ОСНОВЫ РАСЧЕТА РАСЧЕТА НАДЕЖНОСТИ ТЕХНИЧЕСКИХ СИСТЕМ ПО НАДЕЖНОСТИ ИХ ЭЛЕМЕНТОВ](http://www.obzh.ru/nad/4-5.html)
- [Reliability Characteristics for Two Subsystems in Series or Parallel or n Subsystems in m_out_of_n Arrangement](http://auroraconsultingengineering.com/doc_files/Reliability_series_parallel.doc)

## Reliability
- [MTBF — откуда берется «миллион часов MTBF»](https://geektimes.ru/post/122529/)

## Availability
- [Reliability and availability basics](http://www.eventhelix.com/RealtimeMantra/FaultHandling/reliability_availability_basics.htm)
- [System Reliability and Availability](http://www.eventhelix.com/RealtimeMantra/FaultHandling/system_reliability_availability.htm)
- [Failure Rates, MTBFs, and All That](http://www.mathpages.com/home/kmath498/kmath498.htm)
- [Infinite Parallel Redundancy](http://www.mathpages.com/home/kmath326/kmath326.HTM)
- [Mean Time Between Failures & Mean Time To Repair](http://world-class-manufacturing.com/KPI/mtbf.html)
- [MTBF online calculator](http://www.pixelbeat.org/docs/reliability_calculator/)


- [Mean-Time-Between-Failure (MTBF) OF Parallel System](http://www.transtutors.com/homework-help/industrial-management/reliability/mtbf-of-parallel-system.aspx)
- [ГОСТ 27.002-89. Надежность в технике. Основные понятия. Термины и определения](http://docs.cntd.ru/document/gost-27-002-89)

## Common
- [No MTBF](http://nomtbf.com/2015/10/popular-reliability-measures-and-their-problems/). A site devoted to the eradication of the misuse of MTBF : ISSN 2168-4375. 
	- [Popular Reliability Measures and Their Problems](http://nomtbf.com/2015/10/popular-reliability-measures-and-their-problems/)
- [Сравнение кластера надежности и "обычного" сервера](http://www.team.ru/server/stbl_compare.shtml)
- [High Availability Network Fundamentals](http://www.ciscopress.com/store/high-availability-network-fundamentals-9781587130175#largeCover) By Chris Oggerino. Стр 22, про расчет надежности


## Жесткие диски
- Seagate Knowledge base. [Hard disk drive reliability and MTBF / AFR](http://knowledge.seagate.com/articles/en_US/FAQ/174791en?language=en_US)
- [MTBF: What it Really Means?](http://www.enterprisefeatures.com/mtbf-what-it-really-means/). Posted on April 17, 2014 by Paul Rudo in Full Article Archiveю  Хорошая иллюстрация и описание.
- [Everything You Know About Disks Is Wrong](https://storagemojo.com/2007/02/20/everything-you-know-about-disks-is-wrong/) by Robin Harris on Tuesday, 20 February, 2007.
Update II: NetApp has responded. I’m hoping other vendors will as well.
*The industry is moving towards using AFR (Annual Failure Rate). The reason is that MTBF is really confusing, and AFR gives the consumer a better idea of what the number is. an AFR of 0.87% is equivalent to MTBF of 1,000,000. the equation is AFR = 1-exp(-8760/MTBF)*
- Весьма полезно и со ссылками на авторитеты. [Надежность жестких дисков: MTBF, AFR, UER. Почему не стоит использовать десктопные диски в аппаратных RAID'ах?](http://true-system.blogspot.ru/2013/04/mtbf-afr-uer-raid.html)
- Backblaze. [One Billion Drive Hours and Counting: Q1 2016 Hard Drive Stats](https://www.backblaze.com/blog/hard-drive-reliability-stats-q1-2016/)

## SSD
- [SSD reliability in the real world: Google's experience](http://www.zdnet.com/article/ssd-reliability-in-the-real-world-googles-experience/)
- [Facebook's SSD findings: Failure, fatigue and the data center](http://www.zdnet.com/article/facebooks-ssd-experience/)
- [Flash Reliability in Production: The Expected and the Unexpected](https://www.usenix.org/conference/fast16/technical-sessions/presentation/schroeder) by Bianca Schroeder, University of Toronto; Raghav Lagisetty and Arif Merchant, Google, Inc.
- [Как не заблудиться в SLC, MLC и TLC при выборе SSD](http://www.outsidethebox.ms/14571/)
	- Все производители SSD покупают NAND у вышеперечисленных компаний, поэтому в разных накопителях может стоять фактически одинаковая память, даже если ее марка отличается.

## Конденсаторы
- [Зависимость времени наработки на отказ электролитических конденсаторов от реальных условий их эксплуатации](https://ptelectronics.ru/stati/zavisimost-vremeni-narabotki-na-otkaz-elektroliticheskih-kondensatorov-ot-realnyih-usloviy-ih-ekspluatatsii/)
- [TEAPO catalog](
	※ **The estimated life is limited to 15 years, if it exceeds 15 years, take 15 years as standard.**(http://www.teapo.com/WebSiteFile/Download/Catalog.pdf)
- Illinois Capacitor [Capacitor Life Calculators](http://www.illinoiscapacitor.com/tech-center/life-calculators.aspx).
	- uF -- микрофарады.
	- D.F (%) -- [Dissipation Factor and ESR](http://www.illinoiscapacitor.com/pdf/papers/impendance_dissipation_factor_esr.pdf). [Dissipation factor
From Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Dissipation_factor)
	- Берем конденсаторы из [каталога](http://www.illinoiscapacitor.com/ic_search/_lytics_products.aspx?LEAD_STYLE_SHORT=Surface+Mount%7cLug+lead&HEADING_SHORT=High+Frequency%2f+Low+Z%2c+Low+ESR)

Operating conditions directly affect the life of an aluminum electrolytic capacitor. The ambient temperature has the largest effect on life. The relationship between life and temperature follows a chemical reaction formula called Arrhenius' Law of Chemical Activity. Simply put, the law says that life of a capacitor doubles for every 10 degree Celsius decrease in temperature (within limits).  
Voltage derating also increases the life of a capacitor, but to a far lesser extent, as compared to temperature deratings. Internal heating, caused by the applied ripple current, reduces the projected life of an aluminum electrolytic capacitor.
- [Capacitor uF - nF - pF Conversion Tool](http://www.remotemonitoringsystems.ca/uF-nF-pF.php). Easily convert between uF, nF and pF capacitors.

## Huawei 
- [Tecal RH2288 V2 V100R002C00 Reliability Prediction Report](www.huawei.com\ucmf\groups\entpublic\documents\enterprise_en_webasset\hw_259503.pdf)
- [Huawei Partner IT Product Manual — Server Section](http://www.huawei.com/ucmf/groups/entpublic/documents/enterprise_en_webasset/hw_327795.pdf)

