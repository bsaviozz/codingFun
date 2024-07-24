var translatorType = "ascii";
let currentDecimal = '';

function setTranslator(clicked) {
    document.getElementById("st").classList.remove("noshow");
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => button.classList.remove('clicked'))
    translatorType = clicked.id;
    document.getElementById("tr").innerHTML = ""; 
    document.getElementById("og").innerHTML = ""; 
    clicked.classList.add("clicked")
}

function translateASCII(e){ 
    let key = e.key;
    if(key.match(/^[a-zA-Z0-9]$/)){
        document.getElementById("tr").innerHTML = key.charCodeAt(0); 
        document.getElementById("og").innerHTML = key;   
    } 
}

function translateBinaryText(e){
    let key = e.key;
    if(key.match(/^[a-zA-Z]$/)){
        document.getElementById("tr").innerHTML = key.charCodeAt(0).toString(2).padStart(8, '0'); 
        document.getElementById("og").innerHTML = key;   
    } 
}

function translateBinaryNum(e){
    let key = e.key;
    let og = document.getElementById("og");
    let tr = document.getElementById("tr");

    if (key.match(/^[0-9]$/)) {
        currentDecimal += key;
    } else if (key === 'Backspace') {
        currentDecimal = currentDecimal.slice(0, -1);
    } else {
        return;
    }

    og.innerHTML = currentDecimal;

    if (currentDecimal === '') {
        tr.innerHTML = '';
    } else {
        tr.innerHTML = parseInt(currentDecimal, 10).toString(2).padStart(8, '0');
    }
}


window.addEventListener('keydown', function(e) {
    document.getElementById("st").classList.add("noshow");
    switch(translatorType){
        case "ascii":
            translateASCII(e);
            break;
        case "ttb":
            translateBinaryText(e);
            break;
        case "dtb":
            translateBinaryNum(e);
            break;
    }
});