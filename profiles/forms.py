from django import forms

class recuravail(forms.Form):
	day = forms.ChoiceField(choices=[('monday','Monday'),('tuesday','Tuesday'),('wednesday','Wednesday'),('thursday','Thursday'),('friday','Friday'),('saturday','Saturday'),('sunday','Sunday')])
	hour = forms.ChoiceField(choices=[(x, x) for x in range(1, 13)])
	minute = forms.ChoiceField(choices=[('00','00'),('15','15'),('30','30'),('45','45')])
	half = forms.ChoiceField(choices=[('AM','AM'),('PM','PM')])
	
	
class individualavail(forms.Form):
	month = forms.ChoiceField(choices=[(1,'January'),(2,'February'),(3,'March'),(4,'April'),(5,'May'),(6,'June'),(7,'July'),(8,'August'),(9,'September'),(10,'October'),(11,'November'),(12,'December')])
	date = forms.ChoiceField(choices=[(x, x) for x in range(1, 32)])
	hour = forms.ChoiceField(choices=[(x, x) for x in range(1, 13)])
	minute = forms.ChoiceField(choices=[('00','00'),('15','15'),('30','30'),('45','45')])
	half = forms.ChoiceField(choices=[('AM','AM'),('PM','PM')])