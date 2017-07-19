/***
Javier Sorribes, Hispasat S.A.
18/07/2017

Requests to TotalNMS' NBI in jQuery

Requires jQuery
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
    error: function(xhr){
        $('#numCPEs').text( $(xhr.responseText).find('faultString').text() );
    },
    url: 'http://127.0.0.1:9000'
});

function getCPEsByManagedGroup() {
	$('#numCPEs').text('Loading...');
	$.get('../../src/XMLReqs/getCPEsByManagedGroup.xml', function(req){
        $(req).find('managedGroupId').text( $('input#managedGroupId').val() );
        var reqtxt = new XMLSerializer().serializeToString(req.documentElement);
        $.post($ajaxSetup.url, reqtxt, function(resp){
            $('#numCPEs').text( $(resp).find('totalNumber').text() );
        });
    });
}

