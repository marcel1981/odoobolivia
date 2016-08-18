openerp.disable_openerp_online = function(instance) {
    // Disabling the lookup of a valid OPW for the dbuuid,
    // resulting in 'Your OpenERP is not supported'
    instance.web.WebClient.include({
        init: function(parent, client_options) {
            this._super(parent, client_options);
            this.set('title_part', {"zopenerp": "La Selva"});
        },
        show_annoucement_bar: function() {}
    });
};

