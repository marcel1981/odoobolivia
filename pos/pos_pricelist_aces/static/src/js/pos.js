odoo.define('pos_pricelist_aces.pos_pricelist_aces', function (require) {
"use strict";

var Class   = require('web.Class');
var Model   = require('web.Model');
var session = require('web.session');
var core    = require('web.core');
var screens = require('point_of_sale.screens');
var gui     = require('point_of_sale.gui');
var pos_model = require('point_of_sale.models');
var utils = require('web.utils');
var BarcodeParser = require('barcodes.BarcodeParser');
var chrome = require('point_of_sale.chrome');

var _t      = core._t;

pos_model.load_models({
    model: 'product.pricelist',
    fields: [],
    context: [['type', '=', 'sale']],
    loaded: function(self, prod_pricelists){
        self.prod_pricelists = [];
        self.prod_pricelists = prod_pricelists;
    },
});

pos_model.load_fields("res.partner", ['property_product_pricelist']);

var ProductListWidgetAce = screens.ProductListWidget;
var OrderWidgetAce = screens.OrderWidget;
var ProductScreenWidgetAce = screens.ProductScreenWidget;
var ClientListScreenWidgetAce = screens.ClientListScreenWidget;
var PosModelAce = pos_model.PosModel;
var OrderSelectorWidgetAce = screens.OrderSelectorWidget;


var _modelproto = pos_model.PosModel.prototype;
pos_model.PosModel = pos_model.PosModel.extend({
	delete_current_order: function(){
		_modelproto.delete_current_order.call(this);
        var order = this.get_order();
        $('#price_list').val(order.get_pricelist());
    },
    set_order: function(order){
    	_modelproto.set_order.call(this, order);
    	var order = this.get_order();
    	if(order.get_client()){
            order.set_pricelist_val(order.get_client().id);
            $('#price_list').val(order.get_pricelist());
        } else {
            $('#price_list').val('');
        }
    },
    add_new_order: function(){
    	var res = _modelproto.add_new_order.call(this);
    	var order = this.get_order();
    	if(order.get_client()){
            order.set_pricelist_val(order.get_client().id);
            $('#price_list').val(order.get_pricelist());
        } else {
            $('#price_list').val('');
        }
        return res;
    },
});
ClientListScreenWidgetAce.include({
	save_changes: function(){
		this._super();
        if( this.has_client_changed()){
        	if(this.new_client){
        		this.pos.get_order().set_pricelist_val(this.new_client.id);
        	} else {
        		$('#price_list').val('');
        	}
        }
    },
});
ProductScreenWidgetAce.include({
	start: function(){ 
		var self = this;
		this._super();
		
        var pricelist_list = this.pos.prod_pricelists;
        var new_options = [];
        new_options.push('<option value="">Select Pricelist</option>\n');
        if(pricelist_list.length > 0){
            for(var i = 0, len = pricelist_list.length; i < len; i++){
                new_options.push('<option value="' + pricelist_list[i].id + '">' + pricelist_list[i].display_name + '</option>\n');
            }
            $('#price_list').html(new_options);
            var order = self.pos.get('selectedOrder');
            if(order.get_client() && order.get_client().property_product_pricelist[0]){
            	$('#price_list').val(order.get_client().property_product_pricelist[0]);
            }
            $('#price_list').selectedIndex = 0;
        }
        $('#price_list').on('change', function() {
            var partner_id = self.pos.get('selectedOrder').get_client() && parseInt(self.pos.get('selectedOrder').get_client().id);
            if (!partner_id) {
            	$('#price_list').html(new_options);
                alert('Pricelist will not work as customer is not selected !');
                return;
            }
        });
	},
});
var _super_order = pos_model.Order.prototype;
pos_model.Order = pos_model.Order.extend({
	set_pricelist_val: function(client_id) {
        var self = this;
        if (client_id) {
            new Model("res.partner").get_func("read")(parseInt(client_id), ['property_product_pricelist']).pipe(
                function(result) {
                    if (result && result.property_product_pricelist) {
                        self.set('pricelist_val', result.property_product_pricelist[0] || '');
                        $('#price_list').val(result.property_product_pricelist[0]);
                    }
                }
            );
        }
    },
    get_pricelist: function() {
        return this.get('pricelist_val');
    },
	add_product: function(product, options){
	    var partner = this.get_client();
	    var pricelist_id = parseInt($('#price_list').val()) || this.get_pricelist();
		if(this._printed){
	        this.destroy();
	        return this.pos.get_order().add_product(product, options);
	    }
	    this.assert_editable();
	    options = options || {};
	    var attr = JSON.parse(JSON.stringify(product));
	    attr.pos = this.pos;
	    attr.order = this;
	    var line = new pos_model.Orderline({}, {pos: this.pos, order: this, product: product});
	
	    if(options.quantity !== undefined){
	        line.set_quantity(options.quantity);
	    }
	    if(options.price !== undefined){
	        line.set_unit_price(options.price);
	    }
	    if(options.discount !== undefined){
	        line.set_discount(options.discount);
	    }
	
	    if(options.extras !== undefined){
	        for (var prop in options.extras) { 
	            line[prop] = options.extras[prop];
	        }
	    }
	
	    var last_orderline = this.get_last_orderline();
	    if( last_orderline && last_orderline.can_be_merged_with(line) && options.merge !== false){
	        last_orderline.merge(line);
	        if(partner){
	        	if(pricelist_id){
//	        		var pricelist_id = partner.property_product_pricelist[0];
	        		var qty = last_orderline.get_quantity();
	        		new Model("product.pricelist").get_func('price_get')([pricelist_id], product.id, qty).pipe(
                        function(res){
                            if (res[pricelist_id]) {
                                var pricelist_value = parseFloat(res[pricelist_id].toFixed(2));
                                if (pricelist_value) {
                                    last_orderline.set_unit_price(pricelist_value);
                                }
                            }
                        }
                    );
	        	}
		    }
	    } else {
	    	var pricelist_value = null;
            if (partner) {
                var self = this;
                if(pricelist_id){
//	        		var pricelist_id = partner.property_product_pricelist[0];
	        		new Model("product.pricelist").get_func('price_get')([pricelist_id], product.id,1).pipe(
                        function(res){
                            if (res[pricelist_id]) {
                                var pricelist_value = parseFloat(res[pricelist_id].toFixed(2));
                                if (pricelist_value) {
                                    line.set_unit_price(pricelist_value);
                                    self.orderlines.add(line);
                                    self.select_orderline(self.get_last_orderline());
                                }
                                else {
                                	self.orderlines.add(line);
                                	self.select_orderline(self.get_last_orderline());
                                }
                            }
                        }
                    );
	        	} else {
	            	this.orderlines.add(line);
	            }
            } else {
            	this.orderlines.add(line);
            }
	    }
	    this.select_orderline(this.get_last_orderline());
	},
	finalize: function(){
        this.destroy();
        if (this.pos.config.default_partner) {
            var client = this.pos.db.get_partner_by_id(this.pos.config.default_partner[0])
            this.pos.get_order().set_client(client);
        }
    },
});

ProductListWidgetAce.include({
    init: function(parent, options) {
        var self = this;
        this._super(parent,options);
        if (self.pos.config.default_partner) {
            var client = self.pos.db.get_partner_by_id(self.pos.config.default_partner[0])
            self.pos.get_order().set_client(client);
        }
    }
});

OrderWidgetAce.include({
	set_value: function(val) {
        var order = this.pos.get_order();
        if (order.get_selected_orderline()) {
            var mode = this.numpad_state.get('mode');
            if( mode === 'quantity'){
            	var partner = order.get_client();
            	var pricelist_id = order.get_pricelist();
                if (pricelist_id && order.get_selected_orderline() && (val != 'remove')) {
//                	var pricelist_id = partner.property_product_pricelist[0];
                    var qty = order.get_selected_orderline().get_quantity();
                    var p_id = order.get_selected_orderline().get_product().id;
                    if (! val) {
                        val = 1;
                    }
                    new Model("product.pricelist").get_func('price_get')([pricelist_id], p_id, parseInt(val)).pipe(
                        function(res){
                            if (res[pricelist_id]) {
                                var pricelist_value = parseFloat(res[pricelist_id].toFixed(2));
                                if (pricelist_value) {
                                	order.get_selected_orderline().set_quantity(val);
                                    order.get_selected_orderline().set_unit_price(pricelist_value);
                                }
                            }
                        }
                    );
                } else {
                	order.get_selected_orderline().set_quantity(val);
                }
            }else if( mode === 'discount'){
                order.get_selected_orderline().set_discount(val);
            }else if( mode === 'price'){
                order.get_selected_orderline().set_unit_price(val);
            }
        }
    },
});

});
