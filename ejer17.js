//Escribe una función que tome una cadena 
//como entrada y devuelva 
//la cadena invertida.

function invertirCadena(cadena){
    return cadena.split('').reverse().join('');
}
console.log(invertirCadena("hola"));

//Leo
//['L','e','o'] split
//['o','e','L'] reverse
// oel join