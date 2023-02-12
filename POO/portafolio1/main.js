function e1(){
    document.getElementById('metros').value = document.getElementById('millas').value*1852
}
function e2(){
    document.getElementById('monto').value = document.getElementById('precio').value * document.getElementById('porcentaje').value/100

}
function e3(){
    document.getElementById('pdescuento').value = (document.getElementById('precio2').value - document.getElementById('preciodes').value)*100/document.getElementById('precio2').value
}
function e4(){
    document.getElementById('sum').value = parseFloat(document.getElementById('numero1').value) + parseFloat(document.getElementById('numero2').value)
    document.getElementById('res').value = parseFloat(document.getElementById('numero1').value) - parseFloat(document.getElementById('numero2').value)
    document.getElementById('mul').value = parseFloat(document.getElementById('numero1').value) * parseFloat(document.getElementById('numero2').value)
    document.getElementById('div').value = parseFloat(document.getElementById('numero1').value) / parseFloat(document.getElementById('numero2').value)

}
function e5(){
    document.getElementById('v1').value = document.getElementById('r1').value**2*Math.PI
}
function e6(){
    document.getElementById('cm').value = document.getElementById('pulgadas').value * 2.54
}
function e7(){
    
    let segs = document.getElementById('seg').value
    let h = Math.trunc(document.getElementById('seg').value/3600)
    let min = Math.trunc(document.getElementById('seg').value%3600/60)
    let s = Math.trunc(document.getElementById('seg').value%3600%60)
    document.getElementById('hrs').value = h +" hrs " + min + " min " + s + " s"


}
function e8(){
    document.getElementById('v2').value = document.getElementById('r2').value**2*Math.PI*document.getElementById('h1').value


}
function e9(){
    document.getElementById('v3').value = document.getElementById('r3').value**2*Math.PI*document.getElementById('h2').value*(1/3)
}
function e10(){
    document.getElementById('v4').value = document.getElementById('l').value**3

}
function e(){

}















