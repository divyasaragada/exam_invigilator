from django.forms import ModelForm
from schedule.models import tt
class tt1(ModelForm):
	class Meta:#returns fields
		model=tt
		fields='__all__'


