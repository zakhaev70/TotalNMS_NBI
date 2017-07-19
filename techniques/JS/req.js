var host = 'http://172.19.254.3/ws';
var user = 'admin';
var password = 'manager';

function getCPEsByManagedGroup() {
	var mgid = document.getElementById('managedGroupId').value;
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		console.log('There was a change:'+this.readyState+' '+this.status);
		if (this.readyState == 4 && this.status == 200) {
			xmlDoc = xhttp.responseXML;
			console.log(xmlDoc);
			ret = xmlDoc.childNodes[0].childNodes[0].childNodes[0];
			document.getElementById('numCPEs').innerHTML = ret.getElementsByTagName('totalNumber')[0].nodeValue;
        }
		else if (this.readyState == 4 && this.status == 0) {
			console.log('No response, should debug');
			console.log(xhttp.getAllResponseHeaders());
		}
	};
	xhttp.open('POST', host+'/cpeService', true, user, password);
	xhttp.setRequestHeader('Content-Type', 'text/xml;charset=UTF-8');
	xhttp.setRequestHeader('SOAPAction', '');
	//xhttp.setRequestHeader('Connection', 'keep-alive');
	//xhttp.setRequestHeader("Authorization", "Basic " + btoa(user+' '+password));
	//req = readXMLFile('../../src/XMLReqs/getCPEsByManagedGroup.xml');
	//reqtxt = new XMLSerializer().serializeToString(req.documentElement);
	reqtxt = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:com="com.gilat.ngnms.server.services.ws.cfg.face"><soapenv:Header/><soapenv:Body><com:getCPEsByManagedGroup><managedGroupId>2</managedGroupId><lastIndex>0</lastIndex></com:getCPEsByManagedGroup></soapenv:Body></soapenv:Envelope>'
	xhttp.send(reqtxt);
}
