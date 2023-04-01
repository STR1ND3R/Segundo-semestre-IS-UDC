

// ejercicio 1
class Articulo{
    #_precioMenudeo = 0
    #_precioMayoreo = 0
    #_nombre = ''
    #_precioBase = 0

    constructor(nombre,precioBase) {
        if(!isNaN(parseInt(precioBase))){
            this.#_precioBase=precioBase
        }
        this.#_nombre=nombre
        this.#_precioMenudeo = this.precioBase*1.30
        this.#_precioMayoreo = this.precioBase*1.15

    }

    get nombre(){
        return this.#_nombre
    }
    set nombre(value){
        if(value.toString().length > 0){
            this.#_nombre=value
        }
    }
    
    get precioBase(){
        return this.#_precioBase
    }
    set precioBase(value){
        if(!isNaN(parseFloat(value))){
            this.#_precioBase=value
        }
        this.#_precioMenudeo = this.precioBase*1.30
        this.#_precioMayoreo = this.precioBase*1.15
    }

    get precioMenudeo(){
        return this.#_precioMenudeo
    }
    
    get precioMayoreo(){
        return this.#_precioMayoreo
    }
}
a = new Articulo('xd', 100)
console.log(a.precioBase, a.nombre, a.precioMayoreo, a.precioMenudeo)
a.precioBase = 200
console.log(a.precioBase, a.nombre, a.precioMayoreo, a.precioMenudeo)

// ejercicio 2

class Alumno{
    #_numeroDeCuenta = 0
    #_nombre = ''
    #_cal = []
    #_promf = 0
    
    constructor(numeroDeCuenta, nombre, calificaciones){
        if(!isNaN(parseInt(numeroDeCuenta))){
            this.#_numeroDeCuenta=numeroDeCuenta
        }

        this.#_nombre=nombre

        if(Array.isArray(calificaciones)){
            calificaciones.forEach(element => {
                if(!isNaN(parseFloat(element)) && parseFloat(element)>=0 && parseFloat(element)<= 10){
                    this.#_cal.push(parseFloat(element))
                }
            });   
        }

        let sum = 0
        for(let i = 0; i < this.#_cal.length; i++){
            sum = sum + this.#_cal[i]
            this.#_promf = sum/this.#_cal.length
        }
    }


    estatus(){
        if(this.#_promf<6)
            return 'Reprobado'
        else
            return 'Aprobado'
    }


    get nombre(){
        return this.#_nombre
    }
    set nombre(value){
        this.#_nombre = value
    }


    get numeroDeCuenta(){
        return this.#_numeroDeCuenta
    }
    set numeroDeCuenta(value){
        if(!isNaN(parseInt(value))){
            this.#_numeroDeCuenta=value
        }
    }


    get calificaciones(){
        return this.#_cal
    }
    set calificaciones(value){
        if(Array.isArray(value)){
            value.forEach(element => {
                if(!isNaN(parseFloat(element)) && parseFloat(element)>=0 && parseFloat(element)<= 10){
                    this.#_cal.push(parseFloat(element))
                }
            });   
        }

        let sum = 0
        for(let i = 0; i < this.#_cal.length; i++){
            sum = sum + this.#_cal[i]
            this.#_promf = sum/this.#_cal.length
        }
    }


    get promedioFinal(){
        return this.#_promf
    }



}

b = new Alumno
b.numeroDeCuenta = 20194433
b.nombre = "xd"
cal = [0,9,0]
b.calificaciones = cal
console.log(b.nombre, b.numeroDeCuenta, b.calificaciones, b.promedioFinal, b.estatus())

// ejercicio 3

class Rectangulo {
    #_ancho = 0
    #_alto = 0
    constructor(alto, ancho) {
        if(!isNaN(parseFloat(alto))){
            this.#_alto = alto;
        }
        if(!isNaN(parseFloat(alto))){
            this.#_ancho = ancho;
        }

    }   
    perimetro(){
        return this.alto*2+this.ancho*2
    }
    area(){
        return this.alto*this.ancho
    }

    get alto(){
        return this.#_alto
    }
    set alto(value){
        if(!isNaN(parseFloat(alto))){
            this.#_alto = alto;
        }
    }


    get ancho(){
        return this.#_ancho
    }
    set ancho(value){
        if(!isNaN(parseFloat(alto))){
            this.#_ancho = ancho;
        }
    }
}
c = new Rectangulo(10, 100)
console.log(c.alto, c.ancho, c.perimetro(), c.area())


  // ejercicio 4

  class Fecha{
    #_dia = 0
    #_mes = 0
    #_año = 0
    constructor(dia, mes, año) {

        if(!isNaN(parseInt(dia)) && parseInt(dia) <= 31 && parseInt(dia) >= 1){
            this.#_dia = dia;
        }
        if(!isNaN(parseInt(mes)) && parseInt(mes) <= 12 && parseInt(mes) >= 1){
            this.#_mes = mes;
        }
        if(!isNaN(parseInt(año)) && parseInt(año) <= 9999 && parseInt(año) >= 1){
            this.#_año = año;
        }
    }

    get  dia(){
        return this.#_dia
    }
    get  mes(){
        return this.#_mes
    }
    get  año(){
        return this.#_año
    }



    set  dia(value){
        if(!isNaN(parseInt(value)) && parseInt(value) <= 31 && parseInt(value) >= 1){
            this.#_dia = value;
        }
    }
    set  mes(value){
        if(!isNaN(parseInt(value)) && parseInt(value) <= 12 && parseInt(value) >= 1){
            this.#_mes = value;
        }   
    }
    set  año(value){
        if(!isNaN(parseInt(value)) && parseInt(value) <= 9999 && parseInt(value) >= 1){
            this.#_año = value;
        }
    }



  }

f = new Fecha(31,3,2023)
console.log(f.dia, f.mes, f.año)


  class Persona{
    #_nombre = ''
    #_fechaNac = Object()
    constructor(nombre, fechaNac) {
        
        this.#_nombre = nombre
        this.#_fechaNac = fechaNac

        
    }

    get nombre(){
        return this.#_nombre
    }
    set nombre(value){
        this.#_nombre = value
    }


    get fechaDeNacimiento(){
        return this.#_fechaNac
    }
    set fechaDeNacimiento(value){
        this.#_fechaNac = value
    }


    edad(fecha){
        let edad = fecha.año-this.#_fechaNac.año-1
        if(fecha.dia>=this.#_fechaNac.dia   && fecha.mes>=this.#_fechaNac.mes){
            edad++
            
        }

        return edad
    }


  }


  yo = new Persona('Alberto', new Fecha(6,5,2004))
  console.log(yo.nombre, yo.fechaDeNacimiento.dia, yo.fechaDeNacimiento.mes, yo.fechaDeNacimiento.año, yo.edad(f))