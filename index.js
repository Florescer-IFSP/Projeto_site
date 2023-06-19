var b = window.document.getElementsByClassName("botao")
var l = window.document.getElementsByClassName("link")

b.addEventListener("mouseenter", entrarB)
b.addEventListener("mouseout", sairB)
l.addEventListener("mouseenter", entrarL)
l.addEventListener("mouseout", sairL)


function entrarB(){
    b.style.color = "#E7A386";
}

function sairB(){
    b.style.color = "black"
}

function entrarL(){
    l.style.color = "#E7A386";
}

function sairL(){
    l.style.color = "black"
}