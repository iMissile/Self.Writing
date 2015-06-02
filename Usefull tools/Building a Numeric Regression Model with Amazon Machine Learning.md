
[Source](http://blogs.aws.amazon.com/bigdata/post/Tx2OZ63RJ6Z41A0/Building-a-Numeric-Regression-Model-with-Amazon-Machine-Learning "Permalink to Building a Numeric Regression Model with Amazon Machine Learning")

# Building a Numeric Regression Model with Amazon Machine Learning

_Guy Ernest is a Solutions Architect with AWS_

We need to predict future values in our businesses. These predictions are important for better planning of resource allocation and making other business decisions. Often, we settle for a simplified heuristic of average values from the past and some change assumption because more accurate alternatives are too complex or expensive. The new [Amazon Machine Learning][1] (Amazon ML) service changes this equation by providing a simple and inexpensive way of building and using models such as numeric regression.

This post uses the example of a bike share program where you need to know how many bikes are required at each hour of each day in a specific city. In this scenario, you need a machine learning model that predicts a number based on a set of features or predictors. You will build a regression model based on a data set that is publicly available in [Kaggle][2], a large community site of data scientists that compete against each other to solve data science problems. By building the model, you will explore a few concepts around the successful application of machine learning to solve similar problems in your domain.

##  What is the difference between analytics and machine learning?

The bike share example demonstrates the limits of analytics systems when it comes to making accurate predictions. One of the Kaggle participants created the following web page to analyze the provided data. If you choose the **Plots** tab, you can see a visualization of data that was created using R, popular free analytics software, and Shiny, a popular web interface for R: [View Bike Sharing Demand][3].

![][4]

This visualization shows that the demand for bikes is different on weekdays versus weekends, and peaks at 8 AM and 5 PM. You can also dive deeper and compare registered versus occasional (casual) users. The data visualizations below show that casual users are more likely to rent their bikes during the weekend and on Monday, and that registered users are more likely to rent their bikes during weekdays.

![][5]  
&nbsp;

![][6]

It may appear that you can predict the usage of the bike share service based on the data visualizations above; however, there are other factors that influence usage such as season, weather, holidays, and more. It becomes more complex to visualize these additional factors, which is why you may turn to machine learning.

##  Preparing the data to build the machine learning model

The most important part of building a successful machine learning model is to find the most relevant data to feed it. The rule to remember is "Garbage-In-Garbage-Out" (or "Gold-In-Gold-Out", depending on your perspective). Domain knowledge is helpful in identifying what might be a relevant factor (relevant = impactful, easily available for all records, and available for predicting future results).

In the above example, you saw the importance of the weekday versus weekend distinction, so you can use these as Boolean variables in the data set. You also know that the weather has a major effect on bike usage, as people rent fewer bikes when it is raining or too cold. It is easy to get historical weather information and accurate weather prediction for the coming days. The organizers of the [competition][7] on the Kaggle site prepared the data as follows:

    datetime - hourly date + timestamp&nbsp;
    season -&nbsp; 1 = spring, 2 = summer, 3 = fall, 4 = winter
    holiday - whether the day is considered a holiday
    workingday - whether the day is neither a weekend nor holiday
    weather - 1: Clear, Few clouds, Partly cloudy, Partly cloudy
    2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
    3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light
    Rain + Scattered clouds
    4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
    temp - temperature in Celsius
    atemp - "feels like" temperature in Celsius
    humidity - relative humidity
    windspeed - wind speed
    casual - number of non-registered user rentals initiated
    registered - number of registered user rentals initiated
    count - number of total rentals

You have three numbers to predict at the end of the list above: the number of rentals by casual users, number of rentals by registered users, and the total number of rentals. Because the total count is the sum of the first two numbers, and you saw above that casual users behave differently than registered users, you will build two different models to predict each user type separately.

You can use various tools to work with the columns of the CSV file, for example Microsoft Excel or RStudio IDE (http://www.rstudio.com), which is popular among data scientists. In this post, you will use simple shell commands such as _cut_, _sed_, and _awk_ to manipulate the data.

The first manipulation to perform is to shuffle the lines of the training data to remove any order in the data that might bias the machine learning model.

    # shuffle the lines except for the first header line
    tail -n+2 train.csv | gshuf -o BikeShareTrainData.csv
    # Add the header line from the original file as the first line of the
    shuffled file
    head -1 train.csv | cat - BikeShareTrainData.csv &gt; temp &amp;&amp; mv temp BikeShareTrainData.csv

To create a training data file for the prediction of casual user rentals, you need to trim the last two fields (_registered_ and _count_) from the original training data file. Use _cut_ with the ',' delimiter to store the first 10 fields (up to the _casual_ counter) in a new casual training data file:

    cat BikeShareTrainData.csv | cut -d',' -f1-10 &gt; BikeShareCasualTrainData.csv

Repeat this for the registered users, by skipping the 10th field (_casual_) and keeping the 11th (_registered_):

    cat BikeShareTrainData.csv | cut -d',' -f1-9,11 &gt; BikeShareRegisteredTrainData.csv

To train the model, you need to copy the files to Amazon S3. Create a bucket in the same AWS region where the machine learning models will run and copy the files into the bucket using the [AWS CLI][8].

    aws s3 cp BikeShareCasualTrainData.csv s3://<bucket_name>/ML/input/ --region us-east-1
    aws s3 cp BikeShareRegisteredTrainData.csv s3://<bucket_name>/ML/input/ --region us-east-1

Make sure to remove data that you are not going to have later in prediction time (the test data in this case). For example, if you didn't remove the fields for _casual_ and _registered_ from the training data and you then try to learn to predict the _count_ variable, the model has a very easy task; it will simply sum the two variables and ignore the weather and other features.

![][9]

  
&nbsp;In the Amazon ML console, create a datasource by pointing to the training data file that you just uploaded to Amazon S3.

Next, define and optimize a schema for the data.

![][10]

&nbsp;Fix the _season_ variable, which is represented by a number (1 - Spring, 2 - Summer,...), to be a category instead of a numeric data type. Numeric variables have values that describe a measurable quantity as a number, such as 'how many' or 'how much'. If you know that a specific number is not representing a quantity, it is better to label it as a category instead of a numeric value.

Next, choose the target that the machine learning model should predict.

![][11]

Choose the _casual_ variable as the target for this model. The service identifies it as a number and notifies you that it will use numerical regression. Continue with the defaults for the next screens and start the model building process. The process should take a few minutes, depending on the size (length and width) of the data. In later cycles, you can see more advanced ways to build the models, but it is best to start with the simple and default options first.

##  Evaluating the machine learning model

After the model has been created, you can evaluate how good it is; use the simple default machine learning model creation to create the evaluation automatically. It is important to test the evaluation of the model with data that the model was not trained on, data that it didn't "see". Amazon ML does this by [splitting][12] the data randomly into two sets of records: 70% of the records are used to train the model and the rest is held out for the evaluation of the model. You can choose to use your own scheme for training and evaluation and cut the training data differently, but for now use the default.

![][13]

The evaluation produces both a numeric value and a visualization. For numeric [regression][14], the numeric value is called the root-mean-square error (RMSE). The lower the RMSE number, the smaller the error of the prediction, and the better the model. In this example, the RMSE of the model is 39 compared to a naïve model that guesses the average with a RMSE of 49.

You can now also evaluate how each of the variables provided (_temp_, _windspeed_, _working_ _day_, etc.) correlated to the prediction target: in this case, casual or registered user rentals.

![][15]  
Variables with a higher value have better prediction power. In this example, _atemp_ ("feels like" temperature) has a value of 0.32 with the casual user number, compared to 0.01 for _windspeed_. It is also interesting to see that the _datetime_ variable is a strong predictor at 0.21.

![][16]  
Amazon ML is able to parse the text fields and extract tokens such as 01, 02, 03, etc. as predictors for the model.

Now, you can decide if you want to use the model as-is or improve it further by lowering the RMSE. You could try to extract the hour from the _datetime_ variable (known as feature processing), but you saw earlier that the service is doing a decent job in parsing this text field for you. Instead, you can extract the day of the week or the month. Here is an example script to add the day of the week to the variables and copy it into the casual training set:

    awk 'NR&gt;1{system("date -j -f "%Y-%m-%d" " $1 " +%A")}' BikeShareTrain.csv &gt;
    BikeShareTrainDoW.csv
    paste -d "," BikeShareTrainDoW.csv BikeShareCasualTrain.csv &gt; BikeShareCasualDoW.csv

Each one of these feature transformations can potentially improve the prediction accuracy of the model. Being a domain expert in the problem field can be helpful in identifying variables to add (_is raining_, for example).

##  Using the ML model for batch prediction

After the model is satisfactory, you can start using it to make predictions. The model is ready to use immediately, even at great scale or in real time. In this example, you run a batch prediction of the model on the test data from the Kaggle competition site.

![][17]

After the job ends, usually in a few minutes, download the files containing the batch prediction results. Before submitting the results, sum the values of both predictions (casual + registered) to get the total number of expected rentals for each hour in the test file.

You can now combine the results, for example, by printing out the sum of the numbers:

    paste casual_batch.out registered_batch.out | awk '$1+$2&gt;0 {print int($1 + $2); next} {print "0"}' &gt; bike_share_sub_test.csv

That's it! In just a few minutes, you have built a simple machine learning model that is a significant improvement over a heuristic model or an average. If you'd like to learn more about Amazon ML or machine learning, see the [Amazon ML Developer Guide][18].

If you have any questions or suggestions, please leave a comment below.

[1]: https://aws.amazon.com/machine-learning
[2]: http://www.kaggle.com
[3]: https://mlespiau.shinyapps.io/devdataprod-016/
[4]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_1.png
[5]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_2.png
[6]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_3.png
[7]: http://www.kaggle.com/c/bike-sharing-demand
[8]: http://aws.amazon.com/cli/
[9]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_4.png
[10]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_5.png
[11]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_6a.png
[12]: http://docs.aws.amazon.com/machine-learning/latest/mlconcepts/mlconcepts.html#splitting-the-data-into-training-and-evaluation-data
[13]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_7.png
[14]: http://docs.aws.amazon.com/machine-learning/latest/mlconcepts/mlconcepts.html#regression
[15]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_8.png
[16]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_9.png
[17]: http://cdn.amazonblogs.com/bigdata_awsblog/images/ML_Image_10.png
[18]: http://docs.aws.amazon.com/machine-learning/latest/dg/
