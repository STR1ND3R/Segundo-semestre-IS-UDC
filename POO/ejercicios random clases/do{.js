

let a = true
do{
    let x = prompt('Escriba S para continuar N para sali')
    
    if(x.toUpperCase() == 'N'){
        a = false
    }
    console.log('Si')
}while(a)
    
