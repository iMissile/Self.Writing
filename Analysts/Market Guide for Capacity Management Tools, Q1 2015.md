
[Source](http://www.gartner.com/technology/reprints.do?id=1-29LHXB4&amp;ct=150206&amp;st=sb "Permalink to Market Guide for Capacity Management Tools")

# Market Guide for Capacity Management Tools

IT infrastructure capacity management tools should be used as part of the capacity and performance management process. These tools may also be used in an ad hoc fashion by less mature organizations, but it is difficult to extract the full value of the tool without clear process objectives and ownership.

It is common to build on domain-specific, performance-gathering tools. Hence, capacity management tools include functionality to analyze data from a variety of sources to produce utilization trends, and forecast reports for a certain scope of the IT infrastructure. The more advanced tools are able to provide information on performance-constraining factors and performance optimization automation or advice for the scope of the infrastructure covered by the tool.

Thus, IT infrastructure-capacity-planning tools can generate infrastructure-capacity-related reports, are able to perform historical data analysis and capacity-related analytics, and have IT and business scenario-planning abilities. In this research, some of the tools from the vendors covered have the breadth and depth of this functionality and some have limited capabilities across this spectrum of capabilities. This research is not a comprehensive list of capabilities or vendors, it is a representative sample of vendors in this market.

These tools are distinguished by the breadth of their capabilities in terms of their integration with data from a variety of domain-specific tools (e.g., real-time performance-monitoring tools); by their ability to provide forecasts, advice and automation for a wide variety of different types of infrastructure components; by the depth of their analysis of the underlying factors contributing to the performance of the infrastructure; and their support for what-if scenarios and their integration with online analytical processing (OLAP) business-reporting tools.

The rising need to invest in capacity management skills and tools1 has a number of drivers. Digitalization produces pressure for high-performing infrastructures that are agile and are capable of deploying new services rapidly and cost-competitively. At the same time, in-house data center costs are being compared with infrastructure as a service (IaaS) and cloud service providers. This is forcing a rethinking of the older buy-more-hardware-when-needed philosophies that used little more than in-house, Excel-based tools to gather limited historical utilization data to forecast future capacity needs.

In these conditions, homegrown tools quickly become a liability, as the enterprise's dependence on individuals and poorly documented Excel scripts are exposed. This may happen when events such as acquisitions, rapid growth or critical new projects demanding rapid deployment, and an elastic infrastructure occur.

Investment in capacity management processes and tools helps alleviate these issues and provide considerable competitive advantage. Vendors are seizing the opportunity offered by end-users' difficulties in grappling with the demands of agile methods and digitalized businesses to show how their tools can reduce costs and risk and enhance performance.

Although storage and network functionality is often less advanced than server capacity management, an established set of vendors and tools covers all or most of the infrastructure software and hardware components and provides good trending and forecasting functionality. These may be extended with good modeling and planning capabilities, sometimes with additional tools from other vendors. The established vendors are focused on ensuring that they can import data from a wide variety of sources and vendors and bring this data together to present helpful information to decision makers on forecasting demand, optimizing the environment, and planning for additional capacity and investment.

Specialist vendors offer in-depth functionality for a part of the infrastructure, such as the virtual server and storage area network (SAN) environments. These vendors offer more-detailed and effective optimization of their chosen environments and may also offer advice or automatic optimization in near-real time. As organizations increase the proportion of the infrastructure that's virtualized, and introduce private and hybrid clouds, these vendors see their chosen segments of the infrastructure growing in importance.

Segmentation is also opening up opportunities for IT operations analytics (ITOA) vendors to make more targeted use of the log file and performance information to provide specific utilization forecasting and performance optimization advice. Although ITOA vendors have their advocates in the capacity-planning field, there is a lack of comprehensive and well-supported, capacity-planning add-ons that provide the same degree of guaranteed support, appropriate functionality and comparable capacity-focused user interface functionality. This prohibits the consideration of ITOA tools in this market. This is likely to change in the next year or so.

Although many of the tools in the guide provide some network capacity management functionality, deeper functionality is usually found in specific network performance monitoring and diagnostic (NPMD) tools, that can be used for in-depth capacity and performance management in this area (see the "Magic Quadrant for Network Performance Monitoring and Diagnostics").

The IT infrastructure capacity management tool market includes:

* General tools with wide applicability across all or nearly all of the IT infrastructure estate
* Tools targeted at specific subsegments of the infrastructure, such as the virtual server estate or database performance optimization

In this first edition of the Capacity Management Tools Market Guide, generalist ITOA vendors have not been included. Gartner expects general ITOA vendors to eventually target this space more specifically. This will require the release of toolkits or adapters that serve the capacity and performance management needs of infrastructure leaders precisely. They may be produced by the vendor or the user community; however, they must be generally available and supported so that they may be relied on by infrastructure leaders to provide products that are regularly updated to meet their changing infrastructure technology needs. Although such toolkits are not widely in use, we expect to see them emerge into wider use during the next one to two years.

_The vendors listed in this Market Guide do not imply an exhaustive list. This section is intended to provide more understanding of the market and its offerings._

Many vendors were not evaluated that also provide infrastructure-monitoring and related functionality that may be used to a greater or lesser extent to forecast capacity requirements and optimize performance. Those not evaluated include AccelOps, AppFirst, Blue Elephant, Centerity, Centreon, Circonus, Datadog, eG Innovations, Fujitsu, GroundWork, Heroix, HP, Interlink Software, Ipswitch, Kaseya, LogicMonitor, LogMatrix, ManageEngine, Nagios, ServiceNow, NEC, Opsview, OP5, Oracle, Paessler, ScienceLogic, Scout, Server Density, ServersCheck, SevOne, Spiceworks, Tango/04 Computing Group, Zabbix and Zenoss.

Vendors such as Microsoft are building platforms for collecting and storing performance data that can be used for capacity analytics using Microsoft's own capacity analytics tools (yet to be launched) or with other third-party analytics tools. Thus, Microsoft is not included as a vendor in this Market Guide, although all the vendors considered do make use of data from Microsoft tools and utilities.

The following vendors2 are representative of the range of capabilities available in this space.

### Allen Systems Group

Allen Systems Group (ASG) is a privately held company headquartered in Naples, Florida. It employs around 1,000 staff and has development locations in North America and Europe. Product development for its capacity management products takes place in Bethlehem, Pennsylvania. Its total revenue in 2013 was more than $276 million.

ASG's capacity management product, Perfman, is targeted at the mainframe and distributed system server environments. Its key value proposition is providing broad functionality by gathering data across a wide range of environments, which is summarized and analyzed for trending, forecasting and modeling. Perfman Analyst module provides modeling and limited what-if analysis capabilities on the data collected for physical and virtual environments.

Infrastructure data (e.g., CPU usage, memory and disk input/output [I/O]) is collected from the platform it monitors. For example, on Unix (AIX, HP/UX, etc.) it collects data using sar, iostat and other operating system utilities; on Windows, it uses the performance counters in the registry; and, on VMware, it uses VMware Infrastructure (VI) to collect data in an agentless manner. It also uses scripting to generate and automate infrastructure performance reports. Perfman Portal is a customizable Web interface that is used for reporting and displaying summarized data, reports and service forecasts. This user interface is available as a thin client, thick client, Web client and a mobile client. On the mainframe, Perfman uses the Systems Management Facility (SMF) records or integrates with its mainframe performance monitor product (TMON) to collect data. Perfman does not support cloud environments. Most of Perfman's installed base is on the mainframe.

ASG mainly sells this product through its direct sales force and has one base license for all the Perfman modules.

**Strengths:**

* For many enterprises, Perfman has the required capacity management functionality at a comparatively low price.
* It is easy to install and easy to use.

**Challenges:**

### BMC Software

BMC Software was acquired in September 2013 by a private equity group led by Bain Capital and Golden Gate Capital. Its headquarters is in Houston, Texas, with approximately 6,000 people worldwide. BMC's TrueSight Capacity Optimization product development takes place in Milan (Italy); Lexington, Massachusetts; and Pune (India).

The TrueSight Capacity Optimization tool has multidimensional analytics capability (e.g., OLAP), for mainframe and distributed systems, and a diverse set of forecasting algorithms that can be applied across various infrastructure components and services, with OpenStack support recently released. This enables it to model various business (what-if) and IT scenarios (P2V, V2V and virtual to cloud [V2C], etc.) and assess their impact on the service, infrastructure and applications. It also has the capability to generate automated reports, including showback and chargeback, identifying the optimal workload placements in a physical and virtual environment using a "tree-map" visual interface.

TrueSight Capacity Optimization integrates with cloud management platform technologies, such as Cloud Life Cycle Management (CLM) from BMC to extend CLM's capacity and workload placement visibility into private and public cloud environments. Furthermore, it has out-of-the-box integration with various monitoring tools to collect data to improve infrastructure efficiency and identify underutilized infrastructure. It is also used for forecasting infrastructure resources for budgetary reasons and can produce periodic (monthly or quarterly) reports that identify risks and recommended actions.

TrueSight Capacity Optimization can also be integrated with discovery tools, service catalogs and configuration management databases (CMDBs), where organizations have implemented them, to identify and manage service capacity, and where a service can go across infrastructure (server, storage and network, etc.) and applications. The product has standard views that can be customized for different roles, such as capacity planners, infrastructure administrators, cloud and storage managers, service managers, operations managers, business owners or financial managers.

BMC licenses its TrueSight products in four different configurations.

**Strengths:**

* Highly flexible integration to collect data from heterogeneous physical, virtual and cloud environments.
* Good regression modeling and forecasting capabilities.

**Challenges:**

* Although TrueSight is integrated with a wide range of data sources, if the data source is not part of a standard connector, users have to learn and write Perl scripts. Comma-separated values (CSV) format integration (as used by spreadsheets) may require customized integration.
* Users may need to become proficient in the BIRT-based report graphical designer for automated and highly customized, user-specific reports.

### CA Technologies

CA Technologies is a Nasdaq listed company headquartered in New York, New York, with a worldwide presence and development resource in Framingham, Massachusetts; Austin, Texas; and India. It has 13,000 employees globally, with revenue of more than $4.5 billion.

The CA Capacity Management solution (CCM) is a heterogeneous capacity management tool targeted at distributed systems, including physical, virtual and cloud environments. It collects data from a wide variety of sources, including infrastructure performance data from existing monitoring tools and CMDBs, as well as application performance management (APM) data. This is stored in its capacity management repository to perform what-if analysis and modeling. It supports physical, virtual and cloud environments, including Microsoft and VMware, with workload placement summaries that highlight the areas of improvement and risk. It provides trend analysis for physical and virtual servers and heat-map-based reporting.

The CCM also has the ability to include data center infrastructure management (DCIM) data for managing power, space and cooling capacity, as part of its converged capacity management capabilities. Its P2V, V2V and V2C modeling capabilities include cost parameters to show potential savings for recommended configurations. CCM has a Windows client (that is not fully browser enabled), which is used for modeling and analytics and also provides role-based access.

CA sells this product through its direct sales force as well as partners, with four different licensing bundles.

**Strengths:**

* In addition to server and application capacity, CCM functionality includes the physical aspects of the data center (e.g., power, cooling and space resources).
* The CCM has easy-to-use performance analysis, forecasting and modeling capabilities.

**Challenges:**

* The CCM toolset has limited functionality for sizing and optimizing capacity in public cloud environments (e.g., Amazon and Azure).
* The product has limited out-of-the-box capacity management capabilities for network and storage infrastructure.

### Cirba

Cirba is a privately held company headquartered in Ontario, Canada. It has 125 employees and has development offices in Ontario, Canada. It has regional sales offices throughout the U.S. and in London, U.K. Cirba's annual revenue is undisclosed.

Cirba's products are focused on the virtual server and storage (SAN) environments. Cirba's capacity management capabilities are based on Cirba's analytics engine. In addition to providing capacity management, it has the ability to optimize and align infrastructure resources, so that the IT infrastructure demand is matched to the IT infrastructure supply in an optimized manner. This enables the user to make optimal and automated workload placement decisions that are driven by policies. These policies can reflect performance, capacity, business, or security rules or technical constraints or may be driven by software requirements (e.g., to lower licensing costs). Thus, its technology is more suited to virtualized and cloud infrastructure environments than traditional network or physical infrastructure environments.

Cirba's tool has an easy-to-use console to visualize and model infrastructure reservation, model future capacity bookings and demand, and provide capacity forecasts, where services can be modeled by business units or departments. This ability to manage capacity and optimize workload placements is useful for on-premises and cloud environments, so this product provides integration and intelligence to cloud management platform (CMP) technologies, such as VMware's vRealize Automation suite, IBM Cloud Orchestrator and OpenStack. It also has a standard set of APIs that can be used for automation, including adjusting virtual machine (VM) allocations to optimize the use of CPU and memory, and for integrating and driving the Distributed Resource Scheduler (DRS) in VMware environments. These APIs can also be used to integrate with other IT operations management (ITOM) tools.

Cirba mainly sells this product through direct sales; however, it also has a service provider and system integrator (SI) partner network that uses and sells this tool. It is sold on a subscription basis, based on the number of systems analyzed and the modules being used and deployed.

**Strengths:**

* Pioneers in intuitive UIs including heat maps for capacity management visualization
* Advanced functionality in areas of workload placement, automation, and capacity reservation management

**Challenges:**

* Product more suited for virtual environments than physical environments
* Limited support for network capacity planning and management

### Dell

Dell is a privately held company headquartered in Texas. It employs more than 100,000 people worldwide, with relevant development performed in Aliso Viejo, California. As a private company since 2013, Dell no longer discloses its revenue.

Dell's capacity management product is Foglight for Virtualization, Enterprise Edition (through the acquisition of Quest Software), which is targeted mainly at virtualized enterprise environments. It is a scalable product that is easy to integrate with various monitoring data sources. Monitoring data is collected in an agentless manner from APIs, including vCenter, WMI, and other OS and hypervisor-level utilities. This data is then analyzed by the analytics engine to show real-time and historical data mainly for VMware and, more recently, Hyper-V-based, virtualized environments. The tool can also perform analytics to show capacity on virtualized infrastructures, and generate capacity reports and display alerts on a browser-based, thin-client graphical user interface (GUI). The analytics engine provides VM placement, workload allocation advice and capacity reservation with auto-deployment of VMs in the reserved area. It also provides chargeback and showback by groups for cost allocation.

Dell packages three different products:

* Foglight for Virtualization, Free Edition (freemium model through vKernel's acquisition)
* Foglight for Virtualization, Standard Edition (acquired through vKernel)
* Foglight for Virtualization, Enterprise Edition (acquired through Quest)

Enterprises typically buy the Enterprise Edition through Dell's direct sales channel.

**Strengths:**

* Enterprise Edition is an easy-to-implement and scalable product.
* Customer references report satisfaction with the level of support they get for Dell's capacity management product.

**Challenges:**

* Although additional functionality is due for release in 2015, the product is currently more suited for virtual environments than physical or cloud environments, and has limited network and storage capacity management capability.
* Dell has multiple products that lack integration or advanced functionality — e.g., heat maps and P2V, V2V and V2C modeling.

### IBM

IBM is a publicly listed company headquartered in Armonk, New York. It employs more than 430,000 people worldwide. IBM's total revenue in 2013 was nearly $99.8 billion. IBM does not disclose the specific locations where its capacity management products are developed. IBM's capacity planning and management capabilities are mainly focused on server (mainly for VMware and Power VM) and storage capacity planning. These capabilities are delivered through a set of performance-monitoring and capacity-planning tools that share a performance database. These tools are SmartCloud Monitoring and SmartCloud APM, Tivoli Netcool Performance Manager (TNPM), IBM SmartCloud Virtual Storage Center (VSC) and Optim Configuration Manager.

There are two separate user interfaces for capacity planning and management. One targeted at the server capacity planner and another targeted at the storage capacity planner. These tools provide reports for tuning and optimizing storage and server environments from performance data collected from its own monitoring tools and from virtual platform environments, such as VMware vCenter and System p VIOS or from integrating with NetApp. The tools can also use IBM Cognos engine for capacity management reporting for VMware and PowerVM.

IBM's capacity management solutions do not integrate with other third-party monitoring tools. Some of IBM's capacity-planning tools, such as VSC, provide access to its data and analytics to other applications using agents and other interfaces for chargeback and other purposes. These tools also have resource utilization, trending and historical data analysis capability for physical and virtual storage environments. What-if analysis is used to plan for scenarios such as an increase in VMs, workloads and service levels. IBM also has a number of database performance tools that can provide input into a capacity management process.

IBM packages and sells these products either individually or as a package through its passport advantage scheme. Although IBM has started to use digital marketing and sales partnerships, most of its sales are through direct sales channels.

**Strengths:**

* I&amp;O leaders have stronger product and account relationships with IBM than most competitors.
* IBM is able to bundle many products effectively as part of a wider and larger portfolio.

**Challenges:**

* Enterprises looking for point capacity planning and management products do not have IBM on their shortlists.
* Achieving full product functionality and integration may be a significant professional services task.

### Metron

Originally a U.K. company, Metron's head office and development team is in Somerset, U.K., with a U.S. head office in California, reflecting its core business focus on Europe and North America. Metron works through partners in some locations, including Japan and South Africa, and has software technology partners that add technology breadth to the product. Metron is highly focused on the capacity management field, with fewer than 50 full-time staff providing software tools and professional services. Metron is privately held and does not publish its revenue.

The capacity management toolset is called athene. It's centered on the physical server and storage environment; however, it extends its capabilities across the infrastructure by importing data from a variety of vendor tools, with presentation via a browser-based user interface for its "360-degree capacity management" philosophy. Data capture may be either agent-based or agentless, with links into the major infrastructure monitoring tools, including those from CA, HP and IBM. Coverage is good for the common environments. Although athene's functionality covers a range of virtual environments, it lacks depth of functionality, compared with some virtualization capacity management specialist tools. Athene avoids placing a reporting load on the target systems by holding all the required monitoring and reporting data in its own capacity management information system (CMIS).

In addition to trend-based forecasting, Metron advises users to identify the most critical business services and perform deeper-dive capacity modeling and planning on those systems. This enables users to take advantage of the extensive, but more time-consuming, predictive capabilities of athene, combining trending, analytical modeling and business activity pattern matching to provide more-accurate capacity and performance forecasts for those services.

Athene is modular and is supplied as a one-time software purchase with annual maintenance, and the company has recently launched SaaS and managed service offerings. The tool has local support in some countries with third-line support from the U.K. Capacity management consultancy services are also available for those who would rather not maintain the skills in-house.

**Strengths:**

* Good breadth of infrastructure coverage with integration packs for most infrastructure components, from network and storage to databases and mainframes. Network and storage capabilities have been a focus for recent development.
* A strong consultancy pedigree provides a user perspective to product development.

**Challenges:**

* Some key functionality is delivered through partners (such as IIM in Japan) for automated analysis and recommendations on z/OS mainframes.
* In virtual and cloud environments, some specialist tools provide additional analytics and automated optimization.

### NetIQ

NetIQ is a principal brand of Micro Focus International, as a part of a merger completed in November 2014. Headquartered in Houston, Texas, the company employs 1,600 people worldwide, with relevant development performed at its headquarters in Houston; Provo, Utah; and Bangalore, India.

NetIQ's PlateSpin Recon provides visual analysis and forecasting for consolidating and optimizing the data center, which includes the physical data center infrastructure (e.g., power and cooling). It collects hardware (CPU, memory, network cards, storage, etc.); software; and service inventory data for server workloads (Windows, Unix and Linux, etc.), as well as virtual infrastructure, such as VMware vCenter, Microsoft Hyper-V and Xen. PlateSpin Recon can remotely gather workload utilization to determine how resources are being used. It can also work with utilization data gathered by third-party monitoring tools. Recon collects and monitors the rate of change of storage data in terms of disk blocks, which can be useful for data recovery tools where block-level transfers take place.

PlateSpin Recon includes Reporting and Consolidation Planning modules. The Consolidation Planning module determines the optimal fit between server resource supply and workload demand. Recon's consolidation scenarios and what-if scenario planning help visualize the characteristics of server workloads before and after consolidation, and determine the servers required for consolidation. Consolidation plans can be exported directly into PlateSpin Migrate for execution. These tools can also be used with virtual infrastructures to increase consolidation ratios, and to plan workload placement. PlateSpin Recon has the ability to generate trending and forecasting reports to highlight overutilized and underutilized machines, including virtual desktop infrastructure (VDI) environments for VMware.

NetIQ sells this product directly and through partners and resellers.

**Strengths:**

* PlateSpin has strong P2V and V2V planning and modeling functionality.
* Hosted virtual desktop (HVD) or VDI size planning and forecasting identifies underutilized desktops and desktops that need more resources.

**Challenges:**

* PlateSpin lacks visibility in the capacity management market.
* PlateSpin Recon has limited support for network and external cloud environments.

### SolarWinds

Founded in 1999, SolarWinds has more than 150,000 customers worldwide and revenue of more than $400 million. SolarWinds is a publicly quoted company that employs 1,700 people in 11 countries across North America, Europe and the Asia/Pacific (APAC) region. Product development is mainly in the U.S. and Europe. Its initial public offering (IPO) in 2009 stated a vision to "manage the performance all things IT — anywhere." This has been reflected in the acquisition of a dozen companies since 2011, including Pingdom, Confio and N-Able Technologies.

Although there are a few channel partners, SolarWinds sales are mainly direct, with the target purchasers being IT practitioners responsible for managing and sustaining IT infrastructures. This bottom-up marketing strategy is supported through downloadable, fully functional, 30-day product trials that can be up and running in less than an hour. Users are able to monitor their infrastructures, resolve problems and produce reports to justify their purchase to more senior management.

SolarWinds products are mainly focused on availability and performance functionality, with capacity management as one feature of the products. The products are well-integrated and provide breadth of scope across the server, virtualization, database, storage, network and security elements of the infrastructure. The product set has demonstrated the ability to scale to thousands of VMs and disks, with a federated data collection architecture to facilitate the management of multiple data centers. SolarWinds offers some physical and virtual discovery capabilities, and it also imports configuration and monitoring data from other vendor's tools.

SolarWinds Virtualization Manager is licensed by the number of processor sockets on the physical hardware running the hypervisor. SolarWinds Storage Manager is licensed by the total number of disks in the SAN or network-attached storage (NAS) devices being managed.

**Strengths:**

* User-defined, real-time dashboards and integrated product sets provide good visibility of the infrastructure, with good performance analytics and trend-based forecasting using a variety of usage profiles.
* A low-overhead sales model supports competitive pricing with capable capacity and performance management across the entire in-house IT infrastructure.

**Challenges:**

* The aggressive recent acquisitions mean that users should confirm that the needed product components are able to seamlessly exchange the required information, and are truly integrated.
* Although the reporting functionality is adequate for a technical audience, there is limited reporting capabilities for a business audience, who may be key stakeholders.

### Sumerian

With its head office and development in Edinburgh, Scotland, and its main sales office in London, Sumerian has been established for more than 12 years as a capacity management consultancy. This is a privately held business, with a staff of 40, approximately 100 clients and a turnover of more than $3 million per annum. It sells direct to end users, primarily in the U.K. and the rest of Europe and has an especially strong financial sector presence. There is no sales presence in the U.S. or other locations, so support outside Europe is limited.

Building on its consultancy business, Sumerian entered the capacity and performance tool market in 2012. Unusually in this market, it has chosen a SaaS model for its Capacity Planner toolset.

The core functionality is concerned with workloads consuming server and storage resource. Other than the import of third-party data, network utilization analysis is limited. Sumerian Capacity Planner has a unique and powerful user interface that enables users to visualize all or part of their IT infrastructure in a "Sunburst" style, which can zoom in and out to adjust the scope from individual VMs to hosts, clusters and data centers. This allows users to visualize and model workloads, uncover performance bottlenecks and perform predictive analytics on the performance. The predictive forecasting includes time series and anomaly detection to assist with understanding current performance in detail and forecasting future performance in a variety of scenarios. Comparisons between 90-day baselines of historical data assist with uncovering patterns of business activity that is a step above basic trend-based forecasting.

Being a SaaS model, the reporting is not in real time. Hence, it will generally lag current data by several days. Nevertheless, the tool provides deep insight into the allocation and performance of the workloads, supporting segmentation of the application estate by business criticality. What-if scenarios can be modeled and visualized quickly, to provide forecasts of the performance of resources and workloads.

Data may be imported from the usual server, storage and network devices and hypervisors, including common mainframes where modeling extends to the individual logical partition of a computer's resources (LPAR). An SQL data store is used for the capacity and performance data that underpins the product.

Licensing is via a monthly fee, based on a per-user model (with a five-user minimum) plus a monthly fee per server being managed.

**Strengths:**

* The visual Sunburst-style user interface is designed specifically for engineers analyzing and optimizing their IT infrastructures.
* The SaaS model enables users to perform fully functional capacity management without storing the large amounts of required data on their own premises.

**Challenges:**

* SaaS nature of the product means that it does not facilitate near-real-time performance optimization, but is more targeted at capacity planning and predictive analytics.
* Although infrastructure predictive analytics and modeling are included in the tool, the extended application-level analytics capabilities are only available through the purchase of additional consultancy services.

### TeamQuest

Founded in 1991, TeamQuest has a worldwide staff of 150, global turnover of more than $30 million and a global customer base of more than 300 organizations. The company is privately held and headquartered in Clear Lake, Iowa, with direct sales offices in Europe, and partners serving Latin America and Asia via Hong Kong. Product development is in the U.S. and Western Europe.

The TeamQuest "IT Service Optimization" product set brings capacity-planning capability to all infrastructure components and services, although network capacity and performance analytics only consider high-level utilization. The product consists of four core components:

* Analyzer for performance analysis
* Predictor for straight capacity planning
* Surveyor for dynamic and automated analytics and reporting
* The CMIS, which collects and stores the capacity- and performance-related information

The use of automation and queuing theory in the analytics allows a deep level of insight into performance issues (throughput and response time) in the infrastructure. This provides good predictive and remediation capabilities across a broad infrastructure scope, from the component level to the workload and IT service. The CMIS may be federated to accommodate global infrastructures, such as those with multiple data centers.

With adapters for the common monitoring products and data sources, this product blends capacity management with performance optimization and is extending its functionality into ITOA to provide automated solutions to many performance issues across the physical, virtual and cloud estate.

Licensing is based in the number of physical servers and the number of terabytes of storage being managed.

**Strengths:**

* Strong user interface, modeling and automated analytics extending into some system administration functions.
* This is a capable out-of-the-box solution.
* Predictive analytics for a broad scope of the infrastructure including power consumption and the major SAN providers through a partnership with IntelliMagic.

**Challenges:**

* Some users will accept lower functionality, lower-priced products that may even be bundled in with other software or consultancy services.
* In highly virtualized or cloud environments, the specialist vendors still provide deeper levels of resource optimization.

### Virtual Instruments

Founded in 2008, Virtual Instruments has offices in the U.S., U.K., Australia, Hong Kong and Singapore, and more than 300 employees. The head office is in San Jose, California, with product development in the U.S. and the U.K. A strong network of Alliance Partners and major name resellers is consistent with VI's claimed success in penetrating 38 of the Fortune 100 companies. VI has more than 300 customers, but is a private company and does not disclose revenue.

Virtual Instruments' product, VirtualWisdom4, optimizes infrastructure performance by analyzing the traffic in the Fibre Channel, rather than by conventional capacity management techniques. The forecasting, trending and modeling capabilities are not targeted at capacity management for the full scope of the IT infrastructure. However, because the data packets traverse the SAN, a great deal of information and insight may be gleaned from the traffic. Therefore, the VI product set helps to achieve optimal use of the infrastructure resources. This has clear implications for limiting the need for additional capacity.

The heart of the technology deployed by Virtual Instruments are probes, which are placed in the SAN Fibre Channel and give the VirtualWisdom4 product the unusual capability of being able to inspect every packet that traverses the Fibre Channel, without placing additional loads on the computing, storage or network devices. The toolset aggregates and analyzes the huge amounts of data from the probes to uncover and resolve the sometimes subtle causes of latencies in an infrastructure. There are adapters for the major physical, virtual and mainframe environments.

The browser-based user interface is flexible, and it is targeted at analytics and performance optimization, with strong reporting functionality for those use cases.

VirtualWisdom4 is hosted on a dedicated appliance, and a perpetual license fee is payable for each instance.

**Strengths:**

* Extremely detailed insight into the Fibre Channel activity enables VirtualWisdom4 to uncover performance constraints that are difficult to find with other technologies.
* The Fibre Channel probe technology places no additional load on infrastructure computing, storage or network components.

**Challenges:**

* VirtualWisdom4 is designed for performance optimization and providing insight into constraints, rather than capacity planning; consequently, the capacity forecasting, scenario analysis and modeling are limited.
* Being deployed in the Fibre Channel, the insight into network devices, traffic and diagnostics is limited.

### VMTurbo

The first release of VMTurbo was in 2010, and this privately held company now has offices in Boston, New York and Reading, U.K. Development is located in New York. The current CEO, Ben Nye joined in 2013, and the company now exceeds $30 million turnover, with a staff of more than 260 and 1,000 paying customers.

VMTurbo Operations Manager is distributed direct, as well as through a number of established channel partners, according to the location and size of the target customer. Direct support is mainly provided remotely from the U.S. and U.K. offices.

VMTurbo Operations Manager is focused on controlling the application workload, virtual server estate, and public and private cloud environments. It also has modules for closely related technologies, such as Storage and Fabric Control. VMTurbo uses an economic model whereby entities in the data center (such as applications, virtual and physical servers, storage and network elements) are represented as buyers and sellers of resources, with the resources represented as commodities traded between these entities. The utilization of these resources is abstracted as a price. The resulting market of "buyers" and "sellers" allows the allocation of workloads to be optimized, based on the target class of service and the value the business receives from the service associated with the workload.

The user interface allows assurance of the performance of the workloads and identification of constraints. Then, automated or manual intervention may be made to prevent performance or capacity problems in the virtual and cloud environment before they affect users. Modeling and what-if functionality allows users to analyze service quality, while managing business risk. Capacity planning is provided by the control platform, enabling capacity plans to be created, based on real-time and historical operational data.

The free Virtual Health Monitor product is distributed as an unlimited renewable license while VMTurbo Operations Manager is priced on a per-socket basis on either perpetual or term licensing.

**Strengths:**

* Resource allocation is based on economic principles to assure the performance of services and workloads. This enables services to be prioritized and overall performance assured, based on performance, cost and risk.
* Infrastructure resources may be allocated in real time, in response to changing application workload demand.

**Challenges:**

* The product reviewed had little support for network capacity planning or for physical server and software capabilities outside the virtual environment.
* Although functional for the designed purpose, the user interface is less intuitive than some competitors.

### VMware

VMware is a publicly listed company, headquartered in California, with revenue of more than $5.2 billion in 2013. It employs more than 13,000 people worldwide with vRealize development performed in the U.S., Europe and Asia.

VMware's capacity management functionality is part of the vRealize Operations suite, which includes additional ITOM functionality. The capacity management functionality extends coverage of VMware environments into the wider infrastructure, using management packs that gather and report capacity metrics. These packs are typically written by partners (e.g., EMC, HP, Brocade and NetApp) to include storage, networking and other extended capabilities. The product uses the vRealize Operations console to report capacity shortfalls, opportunities to optimize virtual infrastructure, and any risks of violating thresholds or policies set for infrastructure segments.

Capacity reports can be customized to show various trending reports for the resources, such as vCPU, memory and storage. These reports can be scheduled, based on data collected from the resources being monitored. Scenario-based capacity planning enables infrastructure teams to add multiple upcoming projects and to understand its impact on future capacity. The console is able to visualize the overall location of capacity for optimization opportunities. The vRealize Operations suite has APIs (REST-based) and a software development kit (SDK) to export and import data to and from other management tools.

VMware sells this product directly and through its partners. It comes in three versions: Standard, Advanced and Enterprise.

**Strengths:**

* Although vRealize is strongest in the VMware estate, the range of management packs extends VMware's analytics and automation capabilities to virtual, physical and cloud environments, including integration of data from other vendors' toolsets.
* VMware has some 20,000 customers and many good relationships with its user base of infrastructure administrators and managers with capacity management requirements.

**Challenges:**

* VMware relies on its partner ecosystem to extend product functionality via management packs, for which some vendors may charge fees.
* vRealize is less than 12 months old in its current form. Users will need assurance that other vendors' management packs will remain compatible with all future vRealize releases.  