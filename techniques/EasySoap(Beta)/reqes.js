function getCPEsByManagedGroup() {

    "use strict";

	var easysoap = require('easysoap');

    // define soap params
    var params = {
	    host   : '172.19.254.3/ws',
		path   : '/cpeService',
        wsdl   : '172.19.254.3/ws/cpeService?wsdl',

		/* set soap headers (optional)
		headers: [{
            'name'     : 'item_name',
            'value'    : 'item_value',
            'namespace': 'item_namespace'
        }]*/
    };
    var clientOptions = {
        secure : false
    };

    /*
     * create the client
     */
    var soapClient = easysoap.createClient(params, clientOptions);

    soapClient.getRequestXML............
};

	/*
	 * call soap method
	soapClient.call({
    	method    : 'methodName',
		attributes: {
        	xmlns: 'http://www.sample.com'
        },
		params: {
			testParam: 1,
			testParam: [2, 3],
			testParam: {
				'_value'     : 4,
				'_attributes': {
                	'xmlns1': 'http://www.sample.com/other'
                }
            }
        }
    })
    .then((callResponse) => {
		console.log(callResponse.data);	// response data as json
        console.log(callResponse.body);	// response body
		console.log(callResponse.header);  //response header
    })
	.catch((err) => { throw new Error(err); });
    */
