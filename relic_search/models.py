from django.db import models

class Relic( models.Model ):
    voivodship  = models.CharField( max_length = 150 )
    poviat      = models.CharField( max_length = 150 )
    parish      = models.CharField( max_length = 150 )
    city        = models.CharField( max_length = 150 )
    relic_name  = models.CharField( max_length = 150 )
    relic_group = models.CharField( max_length = 150 )
    relic_num   = models.CharField( max_length = 150 )
    material    = models.CharField( max_length = 150 )
    date        = models.CharField( max_length = 150 )
    idef        = models.CharField( max_length = 150 )
    street      = models.CharField( max_length = 150 )

    def __unicode__( self ):
        return "%s, %s, %s --> %s" % ( self.voivodship,
                                       self.poviat,
                                       self.parish,
                                       self.relic_name )
