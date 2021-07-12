from django.shortcuts import render
import pickle
import os
from django.conf import settings

model = os.path.join(settings.BASE_DIR,'model.sav')
# Create your views here.
def index(req):
    return render(req,'index.html')

def predict(req):
	if req.method=="POST":
		v1 = float(req.POST['1'])
		v2 = float(req.POST['2'])
		v3 = float(req.POST['3'])
		v4 = float(req.POST['4'])
		v5 = float(req.POST['5'])
		v6 = float(req.POST['6'])
		load_model = pickle.load(open("model.sav", 'rb'))
		result = load_model.predict([[v1,v2,v3,v4,v5,v6]])
		if result[0] == 0:
			result = 'No Diabetes Detected'
		else:
			result = 'Diabetes Detected'
	else:
		result = None
	return render(req,'index.html',{'res':result})
	