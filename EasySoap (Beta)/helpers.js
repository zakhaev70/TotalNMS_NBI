function readXMLFile(file) {
    var xml = null;
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, true);
    rawFile.onreadystatechange = function() {
        if(rawFile.readyState === 4) {
            if(rawFile.status === 200 || rawFile.status == 0) {
                xml = rawFile.responseXML;
				alert(rawFile.responseText);
				console.log(rawFile.responseXML);
            }
        }
    }
    rawFile.send();
    return xml;
}

function getFirstChild(n) {
    var y = n.firstChild;
    while (y.nodeType != 1) {
        y = y.nextSibling;
    }
    return y;
}
function getChild(n,i) {
    var y = getFirstChild(n);
    for (k=0; k<i; k++) {
        y = y.nextSibling;
        while (y.nodeType != 1) {
            y = y.nextSibling;
        }
    }
    return y;
}
function getNextSibling(n) {
    var y = n.nextSibling;
    while (y.nodeType != 1) {
        y = y.nextSibling;
    }
    return y;
}
