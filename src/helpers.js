/***
Javier Sorribes, Hispasat S.A.
06/07/2017

Helper methods devised for SOAP apps
***/

/* Reads file and calls writer with the plain text read */
function readFile(filename, writer=dummy, async=true) {
    var file = new XMLHttpRequest();
    file.open('GET', filename, async);
    file.onreadystatechange = function() {
        if( file.readyState == 4) {
            if(file.status === 200 || rawFile.status == 0) {
                writer(file.responseText);
            }
        }
    };
    file.overrideMimeType('text/plain');
    file.send();
}

/* Reads file and calls handler with the xml read */
function readXMLFile(filename, handler=dummy, async=true) {
    var file = new XMLHttpRequest();
    file.open("GET", filename, async);
    file.onreadystatechange = function() {
        if(file.readyState === 4) {
            if(file.status === 200 || rawFile.status == 0) {
				handler(file.responseXML);
            }
        }
    }
    file.overrideMimeType('text/xml');
    file.send();
}

/* The following allow for simple navigation through xml,
    avoiding empty subnodes*/
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

/* Doesn't do much, it's there just in case */
function dummy(...args) {
    console.log('Dummy function called with the following arguments: ');
    for( var i=0; i<args.length; i++) {
        console.log((i+1) + ': ' + args[i]);
    }
}
