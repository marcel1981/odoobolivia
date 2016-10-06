odoo.define('pos_ticket_custom_bo.pos_ticket_custom_bo', function (require) {
    "use strict";
    var core = require('web.core');
    var screens = require('point_of_sale.screens');
    var gui = require('point_of_sale.gui');
    var QWeb = core.qweb;

    var BillScreenWidget = screens.ReceiptScreenWidget.extend({
        template: 'BillScreenWidget',
        show: function(){
        this._super();
        var self = this;
        this.render_receipt();
    },

    render_receipt: function(){
        console.log("Render Reciept funtion called");
        this._super();
        //RKD-Start
        var customer = this.pos.get_order().get_client();
        var street = '';
        var city ='';
        var customer_name='';
        if (customer != undefined)
        {
            customer_name = customer.name;
            street = customer.street;
            city=customer.city;
        }

        this.$('.pos-receipt-container').html(QWeb.render('PosTicket',{
            widget:this,
            order: order,
            receipt: order.export_for_printing(),
            orderlines: order.get_orderlines(),
            paymentlines: order.get_paymentlines(),
            customer_name:customer_name,
            customer_street:street,
            city:city,
        }));

        //RKD-End
        }

    });
    gui.define_screen({name:'receipt', widget: pos_ticket_custom_bo.BillScreenWidget});
});