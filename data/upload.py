# -*- coding: utf_8 -*-
import sys
import sqlite3 as sq3

con = sq3.connect( '../data.db' )
cur = con.cursor()

for i, row in enumerate( open( sys.argv[1] )):
    cells = row.replace('"', '').split( '\t' )
    print( cells[0] )
    data = [ 1000+i ] + cells
    query  = 'insert into relic_search_relic values '
    query += '( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? )'

    cur.execute( query, data )

con.commit()


