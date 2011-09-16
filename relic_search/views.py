# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader, Context
from django.template.defaultfilters import slugify
from django.db.models import Q

from wiki_zabytki.relic_search.models import Relic


def home( request ):
    # it's stupid and should be done better
    t = loader.get_template( "home.html" )
    return HttpResponse( t.render( Context({}) ) )


def results( request ):
    # relic query
    r_q = request.GET.get( 'query', '' )
    # location query
    l_q = request.GET.get( 'location', '' )

    query  = Q( relic_name__icontains=r_q )
    query |= Q( relic_group__icontains=r_q )

    query2  = Q( voivodship__icontains=l_q )
    query2 |= Q( poviat__icontains=l_q )
    query2 |= Q( parish__icontains=l_q )
    query2 |= Q( city__icontains=l_q )

    relics = Relic.objects.filter( query, query2 ).order_by( 'voivodship_slug', 'poviat_slug', 'parish_slug', 'relic_name' )

    t = loader.get_template( "result.html" )
    c = Context( { 'relics': relics, 'stat': len( relics ) } )

    return HttpResponse( t.render( c ) )
