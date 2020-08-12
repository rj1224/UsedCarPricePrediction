from django import forms

class DetailForm(forms.Form):
	#FUEL_TYPE =
	#TRANSMISSION = 
	#OWNER_TYPE = 
	Model_car=forms.CharField(max_length=64,widget=forms.TextInput(attrs={'placeholder':'Enter Model of Car'}))
	Location=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder':'Enter City'}))
	Year= forms.IntegerField(min_value=2005,max_value=2020,widget=forms.NumberInput(attrs={'placeholder':'Enter Year in which car was bought'}))
	Kilometers_Driven=forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder':'Enter Kilometers Driven'}))
	Fuel_Type=forms.ChoiceField(choices=[
		('Diesel','Diesel'),
		('Petrol','Petrol'),
		('CNG','CNG'),
		('LPG','LPG'),
	])
	Transmission=forms.ChoiceField(choices=[
		('Automatic','Automatic'),
		('Manual','Manual')
	])
	Owner_Type=forms.ChoiceField(choices=[
		('First','First owner of car'),
		('Second','Second owner of car'),
		('Third','Third owner'),
		('Fourth & Above','Fourth & Above')
	])
	Mileage=forms.FloatField(localize=False,max_value=40,min_value=5,widget=forms.NumberInput(attrs={'placeholder':'Mileage of car in Km/l'}))
	Engine=forms.IntegerField(max_value=3500,widget=forms.NumberInput(attrs={'placeholder':'Enter Engine size of Car in CC.'}))
	Power=forms.FloatField(max_value=250,widget=forms.NumberInput(attrs={'placeholder':'Enter Power of car in bhp.'}))
	Seats=forms.IntegerField(max_value=8,min_value=4,widget=forms.NumberInput(attrs={'placeholder':'No. of seats'}))
	bought_at=forms.IntegerField(max_value=100,widget=forms.NumberInput(attrs={'placeholder':'Original Price in lakhs '}))

