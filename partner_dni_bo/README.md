English
==============================================
This module was developed to add identity card and identification for Department where Bolivia was issued fields, Bolivia also establishes default when registering a client.


UNICO Restriccion
==============================================

C.I. and the Department are unique identifier:

_sql_constraints = [('ci_emision_unique','UNIQUE (ci,emission)','Error: Customer already registered')]

DEFAULT Setting
==============================================

So that the user does not register at the point of sale the same data of the region, it is set by default the most common users.

'Country' = 'Bolivia'
'Status =' La Paz '
'Emission' = 'La Paz'
'City' = 'El Alto'
'Zip' = 'LP'



SPANISH
==============================================

Este modulo se desarrollo para añadir los campos Carnet de Identidad y Departamento donde se emitio la identificacion para Bolivia, tambien establece por defecto Bolivia al momento de registrar un cliente.

Restriccion UNICO
==============================================

C.I. y Departamento son un identificador unico: 

_sql_constraints = [('ci_emision_unique', 'UNIQUE(ci,emision), 'Error: Cliente ya registrado!')].

Estableciendo valores por DEFECTO
==============================================

Para que el usuario no tenga que registrar en el punto de venta los mismos datos de la region, se establece por defecto los usuarios mas comunes.

'Pais' = 'Bolivia',
'Estado' = 'La Paz',
'Emision' = 'La Paz',
'Ciudad' = 'El Alto',
'Zip' = 'LP',
