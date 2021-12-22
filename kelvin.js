//forecast in kelvin
const kelvin = 0
//celsius to kelvin
var celsius = kelvin - 273
//celsius to fahrenheit
let fahrenheit = celsius * (9/5) + 32
//converts previous fahrenheit number to decimal
fahrenheit = Math.floor(fahrenheit)
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit.`)