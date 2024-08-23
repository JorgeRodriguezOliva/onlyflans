console.log("hola")

window.sr = ScrollReveal();

sr.reveal('.navbar', {
    duration: 3000,
    origin: 'left',
    distance: '-400px'
})


sr.reveal('.texto', {
    duration: 3000,
    origin: 'rigth',
    distance: '-400px'
})

sr.reveal('.tarjetas2', {
    duration: 3000,
    origin: 'left',
    distance: '-400px'
})
sr.reveal('.rotar', {
    duration: 3000,
    rotate: {
        x: 1,
        y: 180,
    }
})
