# -*- coding: utf-8 -*-
{
    'name': 'Modulo de peliculas',
    'version': '1.0',
    # Eliminamos 'base' y ponemos 'contacts'
    'depends': ['contacts'],
    'author': 'Suman',
    'category': 'Peliculas',
    'description': """
    Modulo para hacer presupuestos de peliculas
    """,
    'data': [
        'security/security.xml',        
        'security/ir.model.access.csv',
        'views/presupuesto_views.xml',  
        'views/views.xml',
        'report/reporte_peliculas.xml',
        'data/data.xml',
        'demo/demo.xml',
    ],
    'demo': [
    ],
}
