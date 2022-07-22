# House_Price_Prediction

I have used XGBRegressor model because the data set is less.

You can view my google colab notebook for this project :
https://colab.research.google.com/drive/1ErAbu53JChWlZbxdtIAClOUjMvK5fbY_#scrollTo=u3tUADbsPpVo

Process involved:
1. Importing the modules and the dataset
Note: I have used the inbuilt library sklearn for the dataset, but we can also import from the drive or the local computer using import feature or google drive feature
link: https://colab.research.google.com/notebooks/io.ipynb //1st one

2. Pre-Processing:
Check if there are missing values or not,and if any then remove the empty values, but since the dataset which I used didn't have any null values, therefore I proceeded to the next step which is,

3. Ananlysis:
In this process, I evaluated weather the datasets hav corelation or not(+ve and -ve)

4. Test/Train Split:
Splitting in the testing values and training values

5. Using XGBRegressor Model:
For the prediction of the train and test data

6. Evaluation:
Evaluating the accuracy of the model by using the metrics function of sklearn module
