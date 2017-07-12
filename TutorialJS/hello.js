/* Reads file and calls writer with the plain text received */
function readFile(filename, writer=dummy) {
    var file = new XMLHttpRequest();
    file.onreadystatechange = function() {
        if( file.readyState == 4 && file.status == 200 ){
            writer(file.responseText);
        }
    };
    file.open('GET', filename);
    file.overrideMimeType('text/plain');
    file.send();
}

/* Doesn't do much, it's there just in case */
function dummy(...args) {
    console.log('Dummy function called with the following arguments: ');
    for( var i=0; i<args.length; i++) {
        console.log((i+1) + ': ' + args[i]);
    }
}

function write2p(text) {
    document.getElementById('p').innerHTML = text;
}

//var localhost = 'http://127.0.0.1:8887'
//readFile(localhost+'/TutorialJS/hello.txt');
//readFile(localhost+'/XMLReqs/getCPEsByManagedGroup.xml');
//readFile(localhost+'/XMLReqs/getCPEsByManagedGroup.xml', write2p);
