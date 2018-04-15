from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    map_button = Button(
        display_text='Calculate',
        name='map-button',
        icon='glyphicon glyphicon-globe',
        style='info',
        attributes={
            'data-toggle': 'tooltip',
            'data-placement': 'top',
            'onclick': 'app.bufferPoint()',
            'title': 'Calculate'
        }
    )

    context = {
               'map_button': map_button,
               }

    return render(request, 'geoids_ttpoly/home.html', context)