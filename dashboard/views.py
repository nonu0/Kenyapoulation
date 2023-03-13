from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
 # Create your views here.


class Home(TemplateView):
    template_name = 'home.html'
    

    def get_context_data(self, **kwargs):
        county = County.objects.all().order_by('area')
        population = Population.objects.all()
        females_sum = sum(females_pop.females for females_pop in population)
        males_sum = sum(males_pop.males for males_pop in population)
        females_pop = [females_pop.females for females_pop in population]
        males_pop = [males_pop.males for males_pop in population]
        county_names = [county_names.name for county_names in county]
        area = [area.area for area in county]
        context = super().get_context_data(**kwargs)
        context['county_names'] = county_names
        context['females_pop'] = females_pop
        context['males_pop'] = males_pop
        context['area'] = area
        context['females_sum'] = females_sum
        context['males_sum'] = males_sum
        return context


class Coast_data(TemplateView):
    template_name = 'coast.html'

    def get_context_data(self, **kwargs):
        coast = Coast.objects.all()
        coast_counties = [coast_counties.counties for coast_counties in coast]
        coast_area = [coast_area.area for coast_area in coast]
        coast_females_sum = sum(coast_females.females for coast_females in coast)
        coast_males_sum = sum(coast_males.males for coast_males in coast)
        coast_females = [coast_females.females for coast_females in coast]
        coast_males = [coast_males.males for coast_males in coast]
        context = super().get_context_data(**kwargs)
        context['coast_counties'] = coast_counties
        context['coast_area'] = coast_area
        context['coast_females'] = coast_females
        context['coast_males'] = coast_males
        context['coast_females_sum'] = coast_females_sum
        context['coast_males_sum'] = coast_males_sum

        return context


class Central_data(TemplateView):
    template_name = 'central.html'
    def get_context_data(self, **kwargs):
        central = Central.objects.all()
        central_counties = [
        central_counties.counties for central_counties in central]
        central_area = [central_area.area for central_area in central]
        central_females = [central_females.females for central_females in central]
        central_males = [central_males.males for central_males in central]
        central_females_sum = sum(central_females.females for central_females in central)
        central_males_sum = sum(central_males.males for central_males in central)
        context = super().get_context_data(**kwargs)
        context['central_counties'] = central_counties
        context['central_area'] = central_area
        context['central_females'] = central_females
        context['central_males_sum'] = central_males_sum
        context['central_females_sum'] = central_females_sum
        context['central_males'] = central_males

        return context


class Nyanza_data(TemplateView):
    template_name = 'nyanza.html'

    def get_context_data(self, **kwargs):
        nyanza = Nyanza.objects.all()
        nyanza_counties = [
        nyanza_counties.counties for nyanza_counties in nyanza]
        nyanza_area = [nyanza_area.area for nyanza_area in nyanza]
        nyanza_females = [nyanza_females.females for nyanza_females in nyanza]
        nyanza_males = [nyanza_males.males for nyanza_males in nyanza]
        nyanza_females_sum = sum(nyanza_females.females for nyanza_females in nyanza)
        nyanza_males_sum = sum(nyanza_males.males for nyanza_males in nyanza)
        context = super().get_context_data(**kwargs)
        context['nyanza_counties'] = nyanza_counties
        context['nyanza_area'] = nyanza_area
        context['nyanza_females'] = nyanza_females
        context['nyanza_females_sum'] = nyanza_females_sum
        context['nyanza_males_sum'] = nyanza_males_sum
        context['nyanza_males'] = nyanza_males

        return context


class Riftvalley_data(TemplateView):
    template_name = 'rvalley.html'

    def get_context_data(self, **kwargs):
        rvalley = RValley.objects.all()
        rvalley_counties = [
            rvalley_counties.counties for rvalley_counties in rvalley]
        rvalley_area = [rvalley_area.area for rvalley_area in rvalley]
        rvalley_females = [rvalley_females.females for rvalley_females in rvalley]
        rvalley_males = [rvalley_males.males for rvalley_males in rvalley]
        rvalley_females_sum = sum(rvalley_females.females for rvalley_females in rvalley)
        rvalley_males_sum = sum(rvalley_males.males for rvalley_males in rvalley)
        context = super().get_context_data(**kwargs)
        context['rvalley_counties'] = rvalley_counties
        context['rvalley_area'] = rvalley_area
        context['rvalley_females'] = rvalley_females
        context['rvalley_females_sum'] = rvalley_females_sum
        context['rvalley_males_sum'] = rvalley_males_sum
        context['rvalley_males'] = rvalley_males

        return context


class Eastern_data(TemplateView):
    template_name = 'eastern.html'

    def get_context_data(self, **kwargs):
        eastern = Eastern.objects.all()
        eastern_counties = [eastern_counties.counties for eastern_counties in eastern]
        eastern_area = [eastern_area.area for eastern_area in eastern]
        eastern_females = [eastern_females.females for eastern_females in eastern]
        eastern_males = [eastern_males.males for eastern_males in eastern]
        eastern_females_sum = sum(eastern_females.females for eastern_females in eastern)
        eastern_males_sum = sum(eastern_males.males for eastern_males in eastern)
        context = super().get_context_data(**kwargs)
        context['eastern_counties'] = eastern_counties
        context['eastern_area'] = eastern_area
        context['eastern_females'] = eastern_females
        context['eastern_males_sum'] = eastern_males_sum
        context['eastern_females_sum'] = eastern_females_sum
        context['eastern_males'] = eastern_males

        return context


class Neastern_data(TemplateView):
    template_name = 'neastern.html'
    def get_context_data(self, **kwargs):
        neastern = NEastern.objects.all()
        neastern_counties = [
        neastern_counties.counties for neastern_counties in neastern]
        neastern_area = [neastern_area.area for neastern_area in neastern]
        neastern_females = [neastern_females.females for neastern_females in neastern]
        neastern_males = [neastern_males.males for neastern_males in neastern]
        neastern_females_sum = sum(neastern_females.females for neastern_females in neastern)
        neastern_males_sum = sum(neastern_males.males for neastern_males in neastern)
        context = super().get_context_data(**kwargs)
        context['neastern_counties'] = neastern_counties
        context['neastern_area'] = neastern_area
        context['neastern_females'] = neastern_females
        context['neastern_males'] = neastern_males
        context['neastern_females_sum'] = neastern_females_sum
        context['neastern_males_sum'] = neastern_males_sum

        return context


class western_data(TemplateView):
    template_name = 'western.html'

    def get_context_data(self, **kwargs):
        western = Western.objects.all()
        western_counties = [western_counties.counties for western_counties in western]
        western_area = [western_area.area for western_area in western]
        western_females = [western_females.females for western_females in western]
        western_males = [western_males.males for western_males in western]
        western_females_sum = sum(western_females.females for western_females in western)
        western_males_sum = sum(western_males.males for western_males in western)
        context = super().get_context_data(**kwargs)
        context['western_counties'] = western_counties
        context['western_area'] = western_area
        context['western_females'] = western_females
        context['western_females_sum'] = western_females_sum
        context['western_males_sum'] = western_males_sum
        context['western_males'] = western_males

        return context



# now let's do it like a f***'n programmer
# write a function that takes a queryset and returns the details