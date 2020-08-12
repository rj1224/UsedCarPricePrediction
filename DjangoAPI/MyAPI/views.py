from django.shortcuts import render
from . form import DetailForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response 
from rest_framework import status
from django.contrib import messages
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import cardetails
from . serializer import detailsSerializer
import joblib
import pickle
import numpy as np
from sklearn import preprocessing
import pandas as pd
# Create your views here.
class detailsView(viewsets.ModelViewSet):
	queryset = cardetails.objects.all()
	serializer_class = detailsSerializer

def ohevalue(df):
	ohe_col=['Year', 'Kilometers_Driven', 'Mileage', 'Engine', 'Power', 'Seats',
	   'Fuel_Type_CNG', 'Fuel_Type_Diesel', 'Fuel_Type_LPG',
	   'Fuel_Type_Petrol', 'Transmission_Automatic', 'Transmission_Manual',
	   'Owner_Type_First', 'Owner_Type_Fourth & Above', 'Owner_Type_Second',
	   'Owner_Type_Third']
	cat_columns=['Fuel_Type','Transmission','Owner_Type']
	df_processed=pd.get_dummies(df,columns=cat_columns)
	newdict={}
	for i in ohe_col:
		if i in df_processed.columns:
			newdict[i]=df_processed[i].values
		else:
			newdict[i]=0
	print(newdict)
	newdf=pd.DataFrame(newdict)
	return newdf

#@api_view(["POST"])
def predictedprice(X):
	try:
		mdl=joblib.load("C:/Users/palak/DjangoAPI/MyAPI/Price_predict.pkl")
		y_pred=mdl.predict(X)
		newdf=pd.DataFrame(y_pred,columns=['Price'])
		return (newdf)
	except ValueError as e:
		return Response(e.args[0],status.HTTP_400_BAD_REQUEST)

def contact(request):
	if request.method=='POST':
		form=DetailForm(request.POST)
		if form.is_valid():
			Model_car=form.cleaned_data['Model_car']
			location=form.cleaned_data['Location']
			Year=form.cleaned_data['Year']
			Kilometers_driven=form.cleaned_data['Kilometers_Driven']
			Fuel_Type=form.cleaned_data['Fuel_Type']
			Transmission=form.cleaned_data['Transmission']
			Owner_Type=form.cleaned_data['Owner_Type']
			Mileage=form.cleaned_data['Mileage']
			Engine=form.cleaned_data['Engine']
			Power=form.cleaned_data['Power']
			Seats=form.cleaned_data['Seats']
			bought_at=form.cleaned_data['bought_at']
			myDict=(request.POST).dict()
			df=pd.DataFrame(myDict,index=[0])
			answer=predictedprice(ohevalue(df))
			messages.success(request,'Estimated Resale Price: {}'.format(answer))

	form=DetailForm()

	return render(request,'myform/detailsform.html',{'form':form})

