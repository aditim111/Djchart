from django.shortcuts import render
from django.http import HttpResponse
from .fusioncharts import FusionCharts
from .models import Population



def chart(request):
	dataSource = {}
	dataSource['chart'] = { 
    	"caption": "Delhi population growth rates",
        "xAxisName": "Year",
        "yAxisName": "Percent change",
        "theme": "zune"

    }


	dataSource['data'] = []
	for key in Population.objects.all():
  		data = {}
  		data['label'] = key.year
  		data['value'] = key.growth_rate
  		data['tooltext']= key.growth_rate
  		dataSource['data'].append(data)

	column2D = FusionCharts("column2D", "ex1" , "600", "350", "chart-1", "json", dataSource)
	return render(request, 'index.html', {'output': column2D.render()}) 