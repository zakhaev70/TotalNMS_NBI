/***
Javier Sorribes, Hispasat S.A.
18/07/2017

Requests to TotalNMS' NBI in jQuery
Like reqjq.js, but written differently

Requires jQuery
***/

var $postSetup = {
    beforeSend: function(xhr){
        xhr.setRequestHeader('Authorization', 'Basic ' + btoa('admin:manager'));
        xhr.setRequestHeader('Content-Type', 'text/xml;charset=UTF-8');
        xhr.setRequestHeader('SOAPAction', '');
        //xhr.setRequestHeader('Connection', 'keep-alive');  //not required
    },
    contentType: 'xml',  //type specs not required either
    dataType: 'xml',
    type: 'POST',
    url: 'http://127.0.0.1:9000'
};

function getCPEsByManagedGroup() {
	$('#numCPEs').text('Loading...');
    var req;
	$.ajax({
        async: false,  //wait for xml request to load
        error: function(){
           $('#numCPEs').text('Error loading xml request');
        },
        success: function(xhr){req=xhr;},
        type: 'GET',
        url: '/src/XMLReqs/getCPEsByManagedGroup.xml'
    });
    $(req).find('managedGroupId').text( $('input#managedGroupId').val() );
    reqtxt = new XMLSerializer().serializeToString(req.documentElement);
    $.ajax($.extend({}, $postSetup, {  //this technique allows for other posts
        data: reqtxt, 
        error: function(xhr){
            $('#numCPEs').text( $(xhr.responseText).find('faultString').text() );
        },
        success: function(resp){
            $('#numCPEs').text( $(resp).find('totalNumber').text() );
        }
    }));
}

