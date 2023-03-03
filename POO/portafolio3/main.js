var $ = function(id){return document.getElementById(id).value}
var xd = function(id, value){document.getElementById(id).value = value}


function e1(){
    document.getElementById('10').value = ''
    document.getElementById('12').value = ''
    let a = []
    let par = 0, impar = 0
    while(true){
        a.push(prompt('Escriba un numero: '))
        if(a[a.length - 1] < 0){
            break
        }
    }
    a.pop()
    a.forEach(element => {
        if(element%2 == 0){
            par++
            
        }
        if(element%2 == 1){
            impar++
        }
    });
    xd('10',par)
    xd('12',impar)
    

}

function e2(){
    let a = [],b =true
    while(b){
        a.push(parseInt(prompt('Escriba un numero: ')))
        b = confirm('Desea introducir otro numero?')
    }
    a.sort(function (a,b){return a-b})
    xd('21', a[a.length-1])
    xd('22', a[0])
}

function e3(){
    for(i = 1; i <=10; i++){
        xd('st' + i,$('ht' + i)*$('sh' + i)*30)

    }
    let x = 0
    for(i = 1; i <=10; i++){
        x += parseFloat($('st' + i))
    }
    x = x/10
    xd('pr', x)

}
function e4(){
    var tabla = document.createElement('table')
         
    for(i = 1; i <= 10; i++){
        var fila = document.createElement('tr')
        
        for(j = 1; j<= 10; j++){
            let celda = document.createElement('td')
            if(i==1 && j == 1){
            celda.setAttribute('id', '0')
            }
            celda.innerText = String(i*j)
            
            fila.appendChild(celda)
        }
        tabla.appendChild(fila)
    }
    tabla.setAttribute('border', '1px solid black')
    document.getElementById('tablas').appendChild(tabla)
}
function e5(){
    var hmayor = 0, hmenor = 0, mmayor = 0, mmenor = 0
    while(true){
        let edad = parseInt(prompt("Escriba la edad de la persona: "))
        let sexo = prompt("Escriba el sexo de la persona (M) para masculino (F) para femenino").toUpperCase()
        let x = 1
        if(edad < 18){
            if(sexo == 'M'){
                hmenor = hmenor + x
            }
            if(sexo == 'F'){
                mmenor++
            }
        }
        if(edad >= 18){
            if(sexo == 'M'){
                hmayor++
            }
            if(sexo == 'F'){
                mmayor++
            }
        }
        
        if(!(confirm("Quiere introducir los datos de mas personas?"))){
            break
        }
        
    }
    
    xd('51',hmayor)
    xd('52',mmayor)
    xd('53',hmenor)
    xd('54',mmenor)
    
}

function e6(){
    let a=[]
    for(i = 2; i <=200; i+=2){
        a.push(i)
    }
    document.getElementById('61').innerText = a
}

function e7(){
    let a = [], b = [2,3,5,7,]
    b.forEach(element => {
        if($('71')%element==0){
            a.push(element)
        }
    });
    xd('72', a)

}

function e8(){
    let s = 0
    for(i = 0; i<=parseInt($('81'));i++){
        s+=i
    }
    xd('82', s)
}
