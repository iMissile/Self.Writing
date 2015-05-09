
[Source](http://blog.takipi.com/the-7-log-management-tools-you-need-to-know/ "Permalink to The 7 Log Management Tools You Need To Know")

# The 7 Log Management Tools You Need To Know

![blog_boat \(1\)][1]

#### **Splunk vs. Sumo Logic vs. LogStash vs. GrayLog vs. Loggly vs. PaperTrails vs.&nbsp;Splunk&gt;Storm**

&nbsp;  
7  
Splunk, Sumo Logic, LogStash, GrayLog, Loggly, PaperTrails – did I miss someone? I'm pretty sure I did. Logs are like fossil fuels – we've been wanting to get rid of them for the past 20 years, but we're not quite there yet. Well, if that's the case I want a BMW!

To deal with the growth of log data a host of log management &amp; analysis tools have been built over the last few years to help developers and operations make sense of the growing data. I thought it'd be interesting to look at our options and what are each tools' selling point, from a **developer's standpoint**.

As the biggest tool in this space, I decided to put Splunk in a category of its own. That's not to say it's the best tool for what you need, but more to give credit to a product who essentially created a new category.

#### Pros

Splunk is probably the most feature rich solution in the space. It's got hundreds of apps (I counted [537][2]) to make sense of almost every format of log data, from security to business analytics to infrastructure monitoring. Splunk's search and charting tools are feature rich to the point that there's probably no set of data you can't get to through its UI or APIs.

#### Cons

Splunk has two major cons. The first, that is more subjective, is that it's an on-premise solution which means that setup costs in terms of money and complexity are high. To deploy in a high-scale environment you will need to install and configure a dedicated cluster. As a developer, it's usually something you can't or don't want to do as your first choice.

Splunk's second con is that it's expensive. To support a real-world application you're looking at tens of thousands of dollars, which most likely means you'll need sign offs from high-ups in your organization, and the process is going to be slow. If you've got a new app and you want something fast that you can quickly spin up and ramp as things progress – keep reading.

Some more enterprise log analyzers can be found [here][3].

## SaaS Log Analyzers

### [Sumo Logic][4]

Sumo was founded as a SaaS version of Splunk, going so far as to imitate some of splunk's features and visuals early on. Having said that, SL has developed to a full fledged enterprise class log management solution.

#### Pros

SL is chock-full of features to reduce, search and chart mass amounts of data. Out of all the SaaS log analyzers, it's probably the most feature rich. Also, being a SaaS offering it inherently means setup and ongoing operation are easier. One of Sumo Logic's main points of attraction is the ability to establish baselines and to actively notify you when key metrics change after an event such as a new version rollout or a breach attempt.

#### Cons

This one is shared across all SaaS log analyzers, which is you need to get the data to the service to actually do something with it. This means that you'll be looking at possible GBs (or more) uploaded from your servers. This can create issues on multiple fronts –

1. As a developer, if you're logging sensitive or PII you need to make sure it's redacted.
2. There may be a lag between the time data is logged and the time it's visible to to the service.
3. There's additional overhead on your machines transmitting GBs of data, which really depends on your logging throughput.

Sumo's pricing is also not [transparent][5], which means you might be looking at a buying process which is more complex than swiping your team's credit card to get going.

**Update** – I just got a note from Brandon at the Sumo Logic team letting us know you can purchase the product directly using your credit card from within the Free version. Not as easy as going through the web site, but quite close.

### [Loggly][6]

Loggly is also a robust log analyzer, focusing on simplicity and ease of use for a devops audience.

#### ![Loggly][7]

#### Pros

Whereas Sumo Logic has a strong enterprise and security focus, Loggly is geared more towards helping devops find and fix operational problems. This makes it very developer-friendly. Things like creating custom performance and devops dashboards are super-easy to do. Pricing is also transparent, which makes start of use easier.

#### Cons

Don't expect Loggly to scale into a full blown infrastructure, security or analytics solution. If you need forensics or infrastructure monitoring you're in the wrong place. This is a tools mainly for devops to parse data coming from your app servers. Anything beyond that you'll have to build yourself.

### [PaperTrails][8]

PaperTrails is a simple way to look and search through logs from multiple machines, in one consolidated easy-to-use interface. Think of it like [tailing][9] your log in the cloud, and you won't be too far off.

#### ![PaperTrails][10]

#### Pros

PT is what it is. A simple way to look at log files from multiple machines in a singular view in the cloud. The UX itself is very similar to looking at a log on your machine, and so are the search commands. It aims to do something simple and useful, and does it elegantly. It's also very [affordable][11].

#### Cons

PT is mostly text based. Looking for any advanced integrations, predictive or reporting capabilities? You're barking up the wrong tree.

### [Splunk&gt;Storm][12]

This is Splunk's little (some may say step) SaaS brother. It's a pretty similar offering that's hosted on Splunk's servers.

#### Pros

Storm lets you experiment with Splunk without having to install the actual software on-premise, and contains much of the features available in the full version.

#### Cons

This isn't really a commercial offering, and you're limited in the amount of data you can send. It seems to be more of an online limited version of Splunk meant to help people test out the product without having to deploy first. A new service called [Splunk Cloud][13] is aimed at providing a full-blown Splunk SaaS experience.

## Open Source Analyzers

### [Logstash][14]

Logstash is an open source tool for collecting and managing log files. It's part of an open-source stack which includes ElasticSearch for indexing and searching through data and Kibana for charting and visualizing data. Together they form a powerful Log management solution.

![Logstash][15]

#### Pros

Being an open-source solution means you're inherently getting a lot of a control and a very good price. Logstash uses three mature and powerful components, all heavily maintained, to create a very robust and [extensible][16] package. For an open-source solution it's also very easy to install and start using. We use Logstash and love it.

#### Cons

As Logstash is essentially a stack, it means you're dealing with three different products. That means that extensibility also becomes complex. Logstash filters are written in Ruby, Kibana is pure javascript and ElasticSearch has its own REST API as well as JSON templates.

When you move to production, you'll also need to separate the three into different machines, which adds to the complexity.

### [Graylog2][17]

A fairly new player in the space, GL2 is an open-source log analyzer backed by MongoDB as well as ElasticSearch (similar to Logstash) for storing and searching through log errors. It's mainly focused on helping developers detect and fix errors in their apps.

Also in this category you can find [fluentd][18] and [Kafka][19] whose one of its main use-cases is also storing log data. Phew, so many choices!

![][20]

While this post is not about Takipi, I thought there's one feature it has which you might find relevant to all of this.

The biggest disadvantage in all log analyzers and log files in general, is that the right data has to be put there by you first. From a dev perspective, it means that if an exception isn't logged, or the variable data you need to understand why it happened isn't there, no log file or analyzer in the world can help you. Production debugging sucks ![:\(][21]

One of the things we've added to Takipi is the ability to jump into a recorded debugging session straight from a log file error. This means that for every log error you can see the actual source code and variable values at the moment of error. You can learn more about it [here][22].

This is one post where I would love to hear from you guys about your experiences with some of the tools mentioned (and some that I didn't). I'm sure there are things you would disagree with or would like to correct me on – so go ahead, the comment section is below and I would love to hear from you.

**Know great Java hacks**? Always wanted to share coding insights with fellow developers?  
If you want to contribute to Takipi's blog, and reach more than 80,000 developers&nbsp;a month, we're looking for guest writers!&nbsp;Shoot us an email with your idea for a guest post: [hello@takipi.com][23].

![fredjava][24]

The sneaky bug that got an entire production environment down  
[Read more][25]

[1]: http://384uqqh5pka2ma24ild282mv.wpengine.netdna-cdn.com/wp-content/uploads/2014/04/blog_boat-1.png
[2]: https://apps.splunk.com/apps/#/
[3]: http://devopsangle.com/2012/11/20/ask-devops-top-5-business-alternatives-to-splunk/
[4]: http://www.sumologic.com/
[5]: https://www.loggly.com/plans-and-pricing/
[6]: https://www.loggly.com/
[7]: http://384uqqh5pka2ma24ild282mv.wpengine.netdna-cdn.com/wp-content/uploads/2014/04/Loggly.png
[8]: https://papertrailapp.com/
[9]: http://fc03.deviantart.net/fs70/i/2011/327/4/f/tails_and_konata_by_cycloniccyance-d4h1drr.jpg
[10]: http://384uqqh5pka2ma24ild282mv.wpengine.netdna-cdn.com/wp-content/uploads/2014/04/PaperTrails.png
[11]: https://papertrailapp.com/plans
[12]: https://www.splunkstorm.com/
[13]: http://www.splunk.com/goto/cloud
[14]: http://logstash.net/
[15]: http://384uqqh5pka2ma24ild282mv.wpengine.netdna-cdn.com/wp-content/uploads/2014/04/Logstash.png
[16]: http://cookbook.logstash.net/
[17]: http://graylog2.org/
[18]: http://fluentd.org/
[19]: http://kafka.apache.org/
[20]: http://384uqqh5pka2ma24ild282mv.wpengine.netdna-cdn.com/wp-content/uploads/2014/10/rec1.gif
[21]: http://384uqqh5pka2ma24ild282mv.wpengine.netdna-cdn.com/wp-includes/images/smilies/icon_sad.gif
[22]: http://www.takipi.com/logs?utm_source=blog&amp;utm_medium=in-post-link&amp;utm_content=7logtools&amp;utm_campaign=java "http://www.takipi.com"
[23]: mailto:hello@takipi.com
[24]: http://384uqqh5pka2ma24ild282mv.wpengine.netdna-cdn.com/wp-content/uploads/2014/12/fredjava.png
[25]: https://www.takipi.com/the-sneaky-bug?utm_source=Blog&amp;utm_medium=Post-footer-sneaky&amp;utm_content=7logmgmt&amp;utm_campaign=Java
  