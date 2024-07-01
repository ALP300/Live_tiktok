//Escribe una función que tome dos arrays 
//y devuelva un array de 
//elementos comunes entre ellos.

function elementosComunes(array1, array2){
  return array1.filter(elemento=> array2.includes(elemento));
}
console.log(elementosComunes([1,2,3], [2,3,4]));
//PARA PARTICIPAR EN EL SORTEO:
//SEGUIRME POR INSTAGRAM:
//leonardo_palomino1
//SEGUIRME POR TWITCH
//lacasainformatica