//Escribe una función que tome 
//un array de números y 
//devuelva el número más grande.

function numeroMasGrande(numeros){
    return Math.max(...numeros);
}
console.log(numeroMasGrande([1,2,3,4]));