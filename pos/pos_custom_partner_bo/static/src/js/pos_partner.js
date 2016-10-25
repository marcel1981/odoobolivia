odoo.define('pos_partner.models', function (require) {
	"use strict";

	var models = require('point_of_sale.models');    
    
    models.load_models({    	
            model:  'res.partner',
            fields: ['name','street','city','state_id','country_id','vat','phone','zip','mobile','email','barcode','write_date','ci','emision'],
            domain: [['customer','=',true]], 
            loaded: function(self,partners){
                self.partners = partners;
                self.db.add_partners(partners);
            },
    });       

});
