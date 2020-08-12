# UsedCarPricePrediction

Using Dataset from kaggle I created different models XGBoost, Random Forest, Decision Tree and Lasso Regression and took the most suitable model and deployed it using Django and made its user interface minimally aesthetic using bootstrap4 in django.

Random Forest worked well enough among others. I pickled it and used in my Django API.

In my DjangoAPI project I created models with respect to the required fields in the dataset.

I used serializers to make my data interpretable to the machine by converting complex data such as querysets and model instances to be converted into native Python data types.

To accept details of car from user I created forms in Django.

Now I edited my views to create functions that will work in the backdround to fetch the posted details and perform preprocessing on it and use my ML model to predict and display answers.

I created forms using 'crispy' and used Bootstrap 4 to organize the page.

If there are any suggestions as to what more can be done to improve model's efficiency or Django code or the user interface. Do let me know.
