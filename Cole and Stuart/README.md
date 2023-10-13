# Cole, Jonah and Stuart's Group Project
We have not decided on our project idea yet so for now we are using this dataset to practice with.

# Input
The dataset contains every pitch, steal, or lineup event for each at-bat in the 2016 post season. We have access to a variety of attributes that may have had an effect to the outcomes specified. Attributes such as seasonType, attendance, duration, hitterId, pitcherId, and other baseball positions. 

# Output
By training a model with this dataset we could predict whether there will be a succesful pitch, steal, or lineup event using the different attributes in the dataset. 

# Where the dataset be found
The dataset can be found on Google Open Dataset. 
Here is the link: https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=baseball&page=dataset&project=sacred-flight-401223&ws=!1m5!1m4!4m3!1sbigquery-public-data!2sbaseball!3sgames_post_wide

# How to run the code
**Firstly, move the data.csv file into the same directory as the Lab3.py file**

There are different ways to interact with the code through command line arguments. Also ensure that use two dashes instead of one. Ex: ```--r``` vs ```-r```

There are two arguments:

The first argument is the splitting command argument ```--mode```. And there are two options you can pass in, the first is ```N``` for normal splitting, and the second option is ```R``` for random splitting. Here is a sample command using random splitting:  ```python3 Lab3.py --mode R```

The second argument is the ratio(training:testing) you would like to split the training and testing data. The acceptable values are decimal values between 0 and 1 (exclusively). Here is a sample command that sets a ratio to 0.4: ```python3 Lab3.py --r 0.4```

For quick use, you can run ```python3 Lab3.py``` and the mode defaults to ```N``` and
the ratio defaults to ```0.7```

# Extra work 
