from django.shortcuts import render


def richa_portfolio_view(request):
    template = 'richa_portfolio_info/portfolio.html'
    return render(request, template)
