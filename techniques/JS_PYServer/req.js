/***
Javier Sorribes, Hispasat S.A.
06/07/2017

Requests to TotalNMS' NBI

Requires ../helpers.js
***/
var host = 'http://127.0.0.1:9000';
var username = 'admin';
var password = 'manager';

function getCPEsByManagedGroup(mgid) {
	document.getElementById('numCPEs').innerHTML = 'Loading...'
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4) {
            if (this.status == 200) {
			    xmlDoc = xhttp.responseXML;
			    ret = xmlDoc.childNodes[0].childNodes[0].childNodes[0];
			    document.getElementById('numCPEs').innerHTML = ret.getElementsByTagName('totalNumber')[0].childNodes[0].nodeValue;
            }
		    else if (this.status == 500) {
                xmlDoc = xhttp.responseXML;
                fault = xmlDoc.childNodes[0].childNodes[0];
			    document.getElementById('numCPEs').innerHTML = fault.getElementsByTagName('faultstring')[0].childNodes[0].nodeValue;
            }
            else {
                document.getElementById('numCPEs').innerHTML = 'Not successful, status code: ' + this.status;
            }
		}
	};
	xhttp.open('POST', host, true);//, username, password);
	//xhttp.withCredentials = true;
    xhttp.setRequestHeader('Authorization', 'Basic ' + btoa(username+':'+password));
	xhttp.setRequestHeader('Content-Type', 'text/xml;charset=UTF-8');
	xhttp.setRequestHeader('SOAPAction', '');
	//xhttp.setRequestHeader('Connection', 'keep-alive');  //not required
	var req;
	readXMLFile('/src/XMLReqs/getCPEsByManagedGroup.xml', function(xml) {
		req = xml;
	}, false);  // async=false so it waits and puts the xml into req
	getFirstChild(getFirstChild(getChild(req.documentElement,1))).childNodes[0].nodeValue = mgid;  //input id
	reqtxt = new XMLSerializer().serializeToString(req.documentElement);
	xhttp.send(reqtxt);
}
