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

There are different ways to interact with the code through command line arguments. Also ensure that use two dashes instead of one for your arguments. Ex: ```--r``` vs ```-r```

There are three arguments:

The first argument is the splitting command argument ```--mode```. And there are three single options you can pass in, the first is ```N``` for normal splitting, the second option is ```R``` for random splitting, and the last option is ```V``` for adding a third dataset (validation) on top of testing and training. Here is a sample command using random splitting:  ```python3 Lab3.py --mode R```

The second argument is the ratio(training:testing) you would like to split the training and testing data, this argument works in conjuction with the ```N``` and ```R``` mode. The acceptable values are decimal values between 0 and 1 (exclusively). Here is a sample command that sets a ratio to 0.4: ```python3 Lab3.py --r 0.4```. Remember that the r flag must be used with the modes ```N``` or ```R```, else you would be setting r that won't be used(N or R with ratios work together)

The third argument is the ratios(training:testing:validation) you would like to split the training, testing, and validation data, this argument works in conjuction with the ```V``` mode. The acceptable values are decimal values between 0 and 1 (exclusively) and the sum of the ratios must be 1. Here is a sample command that sets the ratios to 0.4:0.5:0.1: ```python3 Lab3.py --mode V --ratios 0.4 0.5 0.1```. Remember that the ratios flag must be used with the mode ```V```, or else you would be setting ratios that won't be used(V and ratios work together)

For quick use, you can run ```python3 Lab3.py``` and the mode defaults to ```N``` and
the ratio defaults to ```0.7```

# Extra work 
Added another mode ```V``` which splits the data into test, training, and validation data. It works in combination with a new command line argument called ```--ratios``` which is the ratio of the data in the form of test:training:validation. Specific Documentation above in How to Run Your Code. 