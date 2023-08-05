var b1 = window.document.getElementById("botao1")
var b2 = window.document.getElementById("botao2")
var b3 = window.document.getElementById("botao3")
var b4 = window.document.getElementById("botao4")
var l1 = window.document.getElementById("link1")
var l2 = window.document.getElementById("link2")
var l3 = window.document.getElementById("link3")
var l4 = window.document.getElementById("link4")

b1.addEventListener("mouseenter", entrarB1)
b1.addEventListener("mouseout", sairB1)
b2.addEventListener("mouseenter", entrarB2)
b2.addEventListener("mouseout", sairB2)
b3.addEventListener("mouseenter", entrarB3)
b3.addEventListener("mouseout", sairB3)
b4.addEventListener("mouseenter", entrarB4)
b4.addEventListener("mouseout", sairB4)
l1.addEventListener("mouseenter", entrarL1)
l1.addEventListener("mouseout", sairL1)
l2.addEventListener("mouseenter", entrarL2)
l2.addEventListener("mouseout", sairL2)
l3.addEventListener("mouseenter", entrarL3)
l3.addEventListener("mouseout", sairL3)
l4.addEventListener("mouseenter", entrarL4)
l4.addEventListener("mouseout", sairL4)

var corb = "#D3D3D3"

function entrarB1(){
    b1.style.color = "#E7A386";
}

function sairB1(){
    b1.style.color = "black"
}
function entrarB2(){
    b2.style.color = "#E7A386";
}

function sairB2(){
    b2.style.color = "black"
}
function entrarB3(){
    b3.style.color = "#E7A386";
}

function sairB3(){
    b3.style.color = "black"
}
function entrarB4(){
    b4.style.color = "#E7A386";
}

function sairB4(){
    b4.style.color = "black"
}

function entrarL1(){
    l1.style.color = "#E7A386";
}

function sairL1(){
    l1.style.color = "black"
}
function entrarL2(){
    l2.style.color = "#E7A386";
}

function sairL2(){
    l2.style.color = "black"
}
function entrarL3(){
    l3.style.color = "#E7A386";
}

function sairL3(){
    l3.style.color = "black"
}
function entrarL4(){
    l4.style.color = "#E7A386";
}

function sairL4(){
    l4.style.color = "black"
}