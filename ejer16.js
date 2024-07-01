class Animal{
    constructor(nombre){
        this.nombre = nombre;
    }
    hacerSonido(){
        console.log("El animal hace sonido");
    }
}

class Perro extends Animal{
    hacerSonido(){
        console.log("El perro ladra")
    }
}

const miPerro= new Perro('Fido')
miPerro.hacerSonido();

//REQUISITOS PARA PARTICIPAR:
//SEGUIRME POR IG
//leonardo_palomino1
//SEGUIRME POR TWITCH
//lacasainformatica