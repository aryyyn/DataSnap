from django.shortcuts import render
from .models import CarbonEmission
import plotly.express as px
def co2Visualizer(request):
    # return render(request,"co2.html", name="co2")
    Co2Emission = CarbonEmission.objects.all()

    fig = px.line(
        x=[c.date for c in Co2Emission],
        y=[c.average for c in Co2Emission],
        title="Co2 Emission",
        labels={'x':'Date', 'y':"Average Emission"}
    )


    chart = fig.to_html()
    return render(request, "home.html", {'chart': chart})


def pollutionVisualizer(request):
    pass


