/***
Javier Sorribes, Hispasat S.A.
18/07/2017

Requests to TotalNMS' NBI in jQuery

Requires ../helpers.js
***/

var $ajaxSetup = $.ajaxSetup({
    beforeSend: function(xhr){
        xhr.setRequestHeader('Authorization', 'Basic ' + btoa('admin:manager'));
        xhr.setRequestHeader('Content-Type', 'text/xml;charset=UTF-8');
        xhr.setRequestHeader('SOAPAction', '');
        //xhr.setRequestHeader('Connection', 'keep-alive');  //not required
    },
    contentType: 'xml',  //type specs not required either
    dataType: 'xml',
    url: 'http://127.0.0.1:9000'
});

function getCPEsByManagedGroup(mgid) {
	$('#numCPEs').text('Loading...');
	var req;
	readXMLFile('../XMLReqs/getCPEsByManagedGroup.xml', function(xml) {
		req = xml;
	}, false);  // async=false so it waits and puts the xml into req
    $(req).find('managedGroupId').text(mgid);
    reqtxt = new XMLSerializer().serializeToString(req.documentElement);
    $.post($ajaxSetup.url, reqtxt, function(resp){
        $('#numCPEs').text( $(resp).find('totalNumber').text() );
    });
}
