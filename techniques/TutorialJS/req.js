var host = 'http://172.19.254.3/ws';
var username = 'admin';
var password = 'manager';

function getCPEsByManagedGroup(mgid) {
	document.getElementById('numCPEs').innerHTML = 'Loading...'
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
    	    xmlDoc = xhttp.responseXML;  //response body as XML element
		    ret = xmlDoc.childNodes[0].childNodes[0].childNodes[0];
		    document.getElementById('numCPEs').innerHTML 
                    = ret.getElementsByTagName('totalNumber')[0].childNodes[0].nodeValue; 
		}
	};
	xhttp.open('POST', host+'/cpeService', true, username, password);
    xhttp.setRequestHeader('Content-Type', 'text/xml;charset=UTF-8');
	xhttp.setRequestHeader('SOAPAction', '');
	//xhttp.setRequestHeader('Connection', 'keep-alive');  //not required
	var req;
	readXMLFile('../../src/XMLReqs/getCPEsByManagedGroup.xml', function(xml) {
		req = xml;
	}, false);  // async=false so it waits and puts the xml into req
	getFirstChild(getFirstChild(getChild(req.documentElement,1))).childNodes[0].nodeValue 
            = mgid;  //input MG Id
	reqtxt = new XMLSerializer().serializeToString(req.documentElement);
	xhttp.send(reqtxt);
}
