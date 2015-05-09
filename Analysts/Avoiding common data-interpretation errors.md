
[Source](http://blog.asmartbear.com/data-interpretation-mistakes.html "Permalink to Avoiding common data-interpretation errors – @ASmartBear")

# Avoiding common data-interpretation errors – @ASmartBear

They say "statistics lie," but they don't. People do.

Well, that's a little harsh. Sure _some _people intentionally skew numbers and selectively pull data, but most folks misinterpret data by accident.

Why do you care if you're not a scientist? &nbsp;Because you collect data about your business all the time&nbsp;— web traffic, revenue sources, expenses, customer behavior&nbsp;— and make decisions based on your (mis)understanding of that data.

Here's a few basic mistakes I encounter constantly.

### **Statistics don't tell the whole story**

It's easy to boil a data set down to a single number, like an average. Easy&nbsp;— and often shortsighted.

Single numbers feel powerful; you feel able to wrap your mind around a lot of data. Sometimes that is indeed useful, but it can also obscure the truth.

Consider [Anscombe's Quartet][1], four graphs that have _identical_ statistical properties, yet clearly represent four distinct processes:

![anscombe quartet][2]

Since the statistics are identical in each case, it's clear that statistics alone don't describe what's actually happening with the data.

The true story of each graph:

1. The process is mostly linear. The best-fit line is handy in describing the relationship, but there are other possibly-random factors at work as well.
2. The data are perfectly related, but not linear. Applying typical linear statistics is just wrong.
3. The data are perfectly linear, with one outlier. Probably the outlier should be ignored, and the best-fit line should reflect the other points.
4. The data don't vary at all in the _x_ direction, except for an outlier which probably should be ignored. All the standard statistical numbers are useless.

**Lessons:**

* Processes can't be boiled down to a single number.
* Blindly applying statistics doesn't explain what's happening.
* Charts can help.

### **"Average" is often useless**

You can't open an analytics tool without being attacked by averages:&nbsp;Average hits/day, average conversion ratios, average transaction size, average time on site.

Trouble is, the average is often not only useless, but misleading. Take "average time-on-site," a typical web analytics metric. It's important enough in Google Analytics that it appears on the top-level site information dashboard, as shown in this real example from my blog:

![Average time on site, Google Analytics][3]

Of course it's better if a visitor spends longer on a site because it means they're engaged.

**Is 1:33 good? Actually that's the wrong question.** The true story&nbsp;becomes clear when you break this single number into pieces:

![annotated-time-on-site-bi-modal][4]

The "average" time-on-site of 93 seconds is useless when trying to explain user behavior. The correct way to think about time-on-site is:

1. Most visitors "bounce" off the site without really looking at it.
2. About a third of the visitors stayed long enough to read some articles.

Furthermore, the way you optimize #1 and #2 are completely different:

1. Bouncing can indicate that the traffic source is poor (i.e. we attracted eyeballs, but they weren't the right eyeballs) or the landing page was poor (i.e. we attracted the right eyeballs, but we failed to lure them into reading further).
2. Getting a few minutes of time on a blog is already "success." Trying to get someone to stay even longer (e.g. 10 minutes instead of 5) probably isn't useful. So the better question is: How do we get more people into this category, rather than trying to "increase the average" in this category?

So not only is the average value 1:33 useless in _describing reality_, it's useless in deciding _what to do next_.

**Lessons:**

* The simple "average" is often meaningless.
* Using a single number to describe a process obscures the truth.
* Using a single number to describe a process prevents you from learning how to improve and optimize.

### **The dangers of "Top 10' and "Others"**

Whether it's a cover article in Cosmo or a web analytics report, people love to read "Top 10' lists.

Top lists can be useful. For example, here are the origins of search engine traffic to my blog:

![top search engines][5]

There are several "other" search engines (e.g. Ask and AOL), but the traffic doesn't amount to a hill of beans (as we say in Texas). It's useful to cut those out of the chart because they're just noise.

The trouble starts when "Other" isn't so trivial. The following chart is a real report from a board meeting I was in years ago (only the names and layout have been altered):

![top accounts no other][6]

Looks fine. But later I was poking around the data myself and decided to add a category for "Others":

![top-accounts-four-other][7]

Some people call this the&nbsp;[Long Tail][8]&nbsp;— a pattern&nbsp;wherein a few big players are far larger than any other single player, but when you add up all the little players they collectively match or&nbsp;— as in this case&nbsp;— tower over the big players.

If you discover a Long Tail in your data, there's several ways to react. Consider the case of having a Long Tail in sales of your product line, as with iTunes and Amazon who have a few blockbuster hits plus a long tail containing millions of products that sell infrequently. Here are four opposing viewpoints of how you could approach the situation:

* The Long Tail is too expensive to sell into because it requires reaching a lot of people, each of whom don't give us much money, so&nbsp;[it won't be cost-effective][9].
* The Long Tail is the least expensive way to sell because it means reaching under-served&nbsp;markets, which means cheap ads and hungry customers.
* Addressing the Long Tail means we have to be all things to all people, and that means we're unfocused. Instead, let's try to be #1 at one thing.
* Trying to be #1 at anything is hard, and often the spoils go to those with the most money, not to the smartest or most passionate. Rather than fight the 800-pound&nbsp;gorilla, let's address the rest of the market that gorillas&nbsp;ignore, but which contains a ton of potential business.

No one of these views is automatically correct. For example, iTunes gets most of their revenue from the big players (contrary to "common" knowledge), but other companies like [Beatport][10] make millions of dollars off the Long Tail of niche music markets (electronic music, in their case).

The only wrong thing is to _ignore_ your "Others" column.

**Lessons:**

* "Top 10' lists can hide important data.
* Any time you truncate data you must first be certain you're not throwing away important information.
* Data patterns like the "Long Tail" aren't "good" or "bad" _per se. _There are usually many equally-viable ways for you to react.

### **Metrics and statistics "rules" cannot be applied blindly**

Consider the following (intentionally unlabelled) chart:

![mystery data][11]

It's tempting to start making observations:

* The average value is 57. (But you already know this is crap, right?)
* The value is generally increasing as we move to the right.
* Some data is missing. Maybe they should be discarded.

Unfortunately, even these basic observations are assumptions, and could be wrong depending on context. Consider these&nbsp;scenarios:

1. These are a student's test scores over time. The student was failing and not turning in assignments. However, in the middle of the period the student hired a tutor. Results improved, and by the end of the class the student had mastered the material.This student should probably be awarded an A or B because of the clear improvement and steady results at the end of the year when tests are hardest. **The student should not receive a grade of 57&nbsp;— the average. **
2. Each result represents a survey of one person on the effectiveness of a certain advertisement.The "zero" rating from subjects #2 and #4 is real data, and it's a bad sign. This could indicate something drastically wrong with the ad, for example being offensive. We need to dig in with those participants and learn more about this failure.In general the average value&nbsp;— including the zeros&nbsp;— is probably a useful indication of the ad's overall effectiveness. It's curious that the results "improved" so much in later trials since the participants were supposed to be randomized. &nbsp;This may indicate a bias in the test itself.

An interesting result of #1 is that **in order to obtain a useful "average" value we ought to throw away almost all our data points!** The opposite is true with #2.

The point is that the _context_ for the data determines how the data is interpreted. You can't blindly apply a "rule," such as which data points can be ignored.

**Lessons:**

* You have to&nbsp;_interpret_ results _in context_, not blindly apply formulas.
* Form a theory first, then see whether the data supports or invalidates your theory.

### **Formulas are not a substitute for thinking.**

Like any tool, statistics is useful when used properly and dangerous otherwise. Like any algorithm, garbage in yields garbage out.

Yes this means "metrics analysis" is harder than it looks. Yes this means you have to take time with your data and verify your thought process with others.

But what's the alternative? Thinking about your processes incorrectly and then wasting time on senseless "solutions?"

Final lesson: **Since metrics are hard and take time and effort to get correct, don't attempt to measure and act on 100 variables.** Pick just a few you really understand and can act on, and optimize with those alone. You're more likely to make a genuine, positive change in your business.

**What tips do you have? [**Leave a comment][12] and join the conversation.

[1]: http://en.wikipedia.org/wiki/Anscombe's_quartet "Wikipedia has more detail"
[2]: http://asmartbear.wpengine.netdna-cdn.com/wp-content/uploads/anscombe-quartet.png "anscombe quartet"
[3]: http://asmartbear.wpengine.netdna-cdn.com/wp-content/uploads/google-analytics-avg-time-on-site.png "Average time on site, Google Analytics"
[4]: http://asmartbear.wpengine.netdna-cdn.com/wp-content/uploads/annotated-time-on-site-bi-modal.png "annotated-time-on-site-bi-modal"
[5]: http://asmartbear.wpengine.netdna-cdn.com/wp-content/uploads/top-search-engines-barchart.png "top search engines"
[6]: http://asmartbear.wpengine.netdna-cdn.com/wp-content/uploads/top-accounts-four.png "top accounts no other"
[7]: http://asmartbear.wpengine.netdna-cdn.com/wp-content/uploads/top-accounts-four-other.png "top-accounts-four-other"
[8]: http://en.wikipedia.org/wiki/The_Long_Tail "Wikipedia definition "
[9]: http://www.newstatesman.com/business/2009/05/anderson-wired-business "Andrew Orlowski argues that there's a lack of empirical evidence of the Long Tail effect actually working"
[10]: http://www.beatport.com "Beatport company home page"
[11]: http://asmartbear.wpengine.netdna-cdn.com/wp-content/uploads/mystery-data.png "mystery data"
[12]: http://blog.asmartbear.com/data-interpretation-mistakes.html#respond
  