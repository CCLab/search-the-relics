# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader, Context
from django.db.models import Q

from wikilubizabytki.relic_search.models import Relic

def home( request ):
    '''Just a simple home page'''
    t = loader.get_template( "home.html" )

    return HttpResponse( t.render( Context({}) ) )


def results( request ):
    '''Search db for the relic name or/and relic location
       and return results list'''
    s_m = request.GET.get( 'strict_mode', 'off' )
    r_q = request.GET.get( 'query', '' )
    l_q = request.GET.get( 'location', '' )

    if s_m == 'on' and r_q != '':
        query  = Q( relic_name__iexact=r_q )
        query |= Q( relic_group__iexact=r_q )
    else:
        query  = Q( relic_name__icontains=r_q )
        query |= Q( relic_group__icontains=r_q )

    if s_m == 'on' and l_q != '':
        query2  = Q( voivodship__iexact=l_q )
        query2 |= Q( poviat__iexact=l_q )
        query2 |= Q( parish__iexact=l_q )
        query2 |= Q( city__iexact=l_q )
    else:
        query2  = Q( voivodship__icontains=l_q )
        query2 |= Q( poviat__icontains=l_q )
        query2 |= Q( parish__icontains=l_q )
        query2 |= Q( city__icontains=l_q )

    relics = Relic.objects.filter(
                                query,
                                query2
                        ).order_by(
                                'voivodship',
                                'poviat',
                                'parish',
                                'relic_name'
                        )

    t = loader.get_template( "result.html" )
    c = Context({
            'relics': relics,
            'stat': len( relics ),
            'l_q': l_q,
            'r_q': r_q,
            's_m': s_m
        })

    return HttpResponse( t.render( c ) )


def register( request ):
    '''Search db for the registry number of the relic and return results list'''
    r_q = request.GET.get( 'idef', '' )

    relics = Relic.objects.filter(
                                idef__icontains=r_q
                        ).order_by(
                                'voivodship',
                                'poviat',
                                'parish',
                                'relic_name'
                        )

    t = loader.get_template( "result.html" )
    c = Context({
            'relics': relics,
            'stat': len( relics ),
            'l_q': '',
            'r_q': r_q,
            's_m': 'off'
        })

    return HttpResponse( t.render( c ) )
