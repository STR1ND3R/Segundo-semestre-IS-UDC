

var $ = function(id){return document.getElementById(id).value}
var xd = function(id, value){document.getElementById(id).value = value}

function e1(){
    parseInt( $('n1')) > parseInt($('n2')) ? xd('mayor', $('n1')) : xd('mayor', $('n2'))


}
function e2(){
    n = [parseInt($('n12')), parseInt($('n22')), parseInt($('n32'))]
    n.sort(function(a,b){return a-b})
    xd('ordenados', n)
}
function e3(){
    $('n13')%5 == 0 ? xd('n23', 'Si') : xd('n23', 'No')
}
function e4(){
    $('n14')%2 == 0 && $('n24')%2 == 0 ? xd('n34', 'Si') : xd('n34', 'No')
}
function e5(){
    h = parseInt($('n15'))
    m = parseInt($('n25'))
    s = parseInt($('n35'))
    s = s + 1
    alert(s)
    if (s == 60){
        m++
        s = 0
    }
    if (m == 60){
        h++
        m = 0
    }
    if (h == 24){
        h = 0
    }
    alert(h,m,s)
    xd('n45', h+ ':' + m + ':' + s)
    
}
function e6(){
    if($('n16') < 0)
        xd('n26', 'negativo')
    if($('n16') == 0)
        xd('n26', 'cero') 
    if($('n16') > 0)
        xd('n26', 'positivo')
}
function e7(){
    if($('n17')%2 ==  0)
        xd('n27', 'par')
    if($('n17') == 0)
        xd('n27', 'cero') 
    if($('n17')%2 == 1)
        xd('n27', 'impar')
}
function e8(){
    let a = []
    for (let i = 0; i < 10; i++) {
        a.push(parseInt(prompt("Escribe un numeor")))
    }
    a.sort(function(a,b){return a-b})
    xd('n18', a[a.length-1])
    xd('n28', a[0])
}
function e9(){
    parseInt($('n19'))>=10000 ? xd('n29', $('n19')*0.85) : xd('n29', $('n19')*0.90)

}
function e10(){
    let l = ['A','E','I','O','U']
    l.includes($('n10').toUpperCase()) ? xd('n20', 'Si') : xd('n20', 'No')

}