from django.urls import path
from richa_portfolio.views import richa_portfolio_view

urlpatterns = [

    path('richa/', richa_portfolio_view, name='richa'),
]