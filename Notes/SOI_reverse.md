# Open-source monitoring
- CMDB
	- [i-doit](https://www.i-doit.org)
	- [iTop](http://www.combodo.com)
	- [iTop ITSM & CMDB по русски](http://itop-itsm.ru/)
	- [CMDBuild](http://cmdbuild.org). CMDBuild is a web environment in which you can configure custom solutions for IT Governance, or more generally for asset management.
- [Alerta monitoring system](http://alerta.readthedocs.io/en/latest/index.html)
The alerta monitoring system is a tool used to consolidate and de-duplicate alerts from multiple sources for quick ‘at-a-glance’ visualisation. With just one system you can monitor alerts from many other monitoring tools on a single screen.
- [Zabbix](http://www.zabbix.com)
	- [Использование Zabbix для мониторинга критических систем](https://xakep.ru/2014/08/13/using-zabbix/). Журнал «Хакер»	 13.08.2014
	- [Настройка Zabbix SNMP traps](http://va0816.blogspot.ru/2013/06/zabbix-snmp-traps.html)
	- [Zabbix 2.4 прием SNMP трапов - как это работает!](http://software-radar.com/article/zabbix-24-%D0%BF%D1%80%D0%B8%D0%B5%D0%BC-snmp-%D1%82%D1%80%D0%B0%D0%BF%D0%BE%D0%B2-%D0%BA%D0%B0%D0%BA-%D1%8D%D1%82%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0%D0%B5%D1%82)
- [Observium -- Network monitoring with intuition](http://observium.org/)
Observium is a low-maintenance auto-discovering network monitoring platform supporting a wide range of device types, platforms and operating systems including Cisco, Windows, Linux, HP, Juniper, Dell, FreeBSD, Brocade, Netscaler, NetApp and many more. Observium focuses on providing a beautiful and powerful yet simple and intuitive interface to the health and status of your network.
- NeDi. REDISCOVER YOUR NETWORK!](http://www.nedi.ch/)


# SOI Service modelling

## Service Priority
Priority indicates the importance of a service to the business.
Priority applies to the Dashboard, where you can sort services by this value. Priority is not used in any impact calculations, and all services have no priority value by default. List of predefined values:
- None (0)
- Low (7)
- Medium (8)
- High (9)
- Critical (10)

## Impact
Impact indicates how much a CI affects a service and related CIs.
The following factors determine impact:
- CI severity
- CI significance
- Propagation type and policy

Impact provides IT personnel with a good understanding of what fault conditions really mean to the services that CIs support.

CA SOI calculates the impact by multiplying severity by significance. Significance is a number from 1 (lowest) to 10 (highest), and severity ranges from 0 (Normal) to 4 (Down). Therefore, the highest possible impact is 40. Consider an application with a severity of 4 and a significance of 4. The resulting impact is 16.

Note: When a custom propagation policy connects CIs, you can define complex rules for changing the severity value. For more information, see Define Custom Propagation Policy.

Consider the following items:
- If you change the significance of an item, the impact changes after a new alert is received.
- Priority is used in the calculation of impact instead of significance in the following situations:
	- The service is a top-level service
	- The significance of the parent relationship is zero

The following table defines the impact ranges:

Impact		Color		Description
0		Green		Operational
1-10		Yellow		Slightly Degraded
11-20		Orange		Moderately Degraded
21-30		Red		Severely Degraded
31-40		Burgundy	Down