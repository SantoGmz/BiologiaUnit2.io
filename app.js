// Array de preguntas
const preguntas = [
    {
        pregunta: "Proceso mediante el cual los nutrientes pasan a la sangre",
        opciones: ["Ingestión", "Absorción", "Digestión", "Egestión"],
        respuestaCorrecta: 1 // Índice de la respuesta correcta
    },
    {
        pregunta: "¿Qué es la fotosíntesis?",
        opciones: ["Proceso de respiración", "Proceso de producción de energía en plantas", "Reacción química en animales", "Ninguna de las anteriores"],
        respuestaCorrecta: 1
    },
    {
        pregunta: "La mayor absorción de nutrientes ocurre en",
        opciones: ["Estómago", "Boca", "Intestino Grueso", "Intestino Delgado"],
        respuestaCorrecta: 3
    },    
    {
        pregunta: "La digestión oral es aquella que se realiza en",
        opciones: ["Esófago", "Intestino Grueso", "Boca", "Estómago"],
        respuestaCorrecta: 2
    },
    {
        pregunta: "En el proceso digestivo, la absorción del agua ocurre a nivel del",
        opciones: ["Estómago", "Esófago", "Intestino Grueso", "Intestino Delgado"],
        respuestaCorrecta: 2
    },
    {
        pregunta: "En la boca se inicia la digestión de",
        opciones: ["Proteínas", "Grasas", "Almidón", "Vitaminas"],
        respuestaCorrecta: 2
    },
    {
        pregunta: "Antes de ser digeridas, las grasas deben ser emulsificadas por las sales biliares producidas en el",
        opciones: ["Páncreas", "Hígado", "Estómago", "Sangre"],
        respuestaCorrecta: 1
    },
    {
        pregunta: "Una dieta pobre en fibras y agua puede dificultar el proceso de",
        opciones: ["Digestión", "Emulsificación", "Egestión", "Absorción"],
        respuestaCorrecta: 0
    },
    {
        pregunta: "Sección del tubo digestivo donde viven bacterias necesarias para nuestra supervivencia",
        opciones: ["Esófago", "Páncreas", "Vesícula biliar", "Intestino grueso"],
        respuestaCorrecta: 3
    },
    {
        pregunta: "Enzima que hidroliza los ácidos nucleicos",
        opciones: ["Peptidasa", "Nucleasa", "Disacarasa", "Lipasa"],
        respuestaCorrecta: 1
    }
];

let preguntaActual = 0;
let respuestasCorrectas = 0; // Contador de respuestas correctas

// Función para mezclar preguntas
function mezclarPreguntas(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

// Función para mezclar opciones de respuesta
function mezclarOpciones(opciones) {
    for (let i = opciones.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [opciones[i], opciones[j]] = [opciones[j], opciones[i]];
    }
}

// Función para obtener opciones mezcladas con respuestas de otras preguntas
function obtenerOpcionesMezcladas(pregunta) {
    const opciones = [...pregunta.opciones]; // Crear una copia de las opciones
    const respuestaCorrecta = opciones[pregunta.respuestaCorrecta];

    // Recopilar respuestas incorrectas de otras preguntas
    const respuestasIncorrectas = preguntas
        .flatMap(p => p.opciones)
        .filter(opcion => opcion !== respuestaCorrecta) // Filtrar la respuesta correcta actual
        .sort(() => 0.5 - Math.random()); // Mezclar respuestas incorrectas

    // Tomar las tres primeras respuestas incorrectas
    const opcionesFinales = [...opciones, ...respuestasIncorrectas].slice(0, 4); // Seleccionar 4 opciones
    mezclarOpciones(opcionesFinales); // Mezclar y devolver
    return opcionesFinales;
}

// Mezclar preguntas al inicio
mezclarPreguntas(preguntas);

// Mostrar la pregunta y las opciones
function mostrarPregunta() {
    const quizDiv = document.getElementById("quiz");
    const preguntaObj = preguntas[preguntaActual];

    quizDiv.innerHTML = `<p>${preguntaObj.pregunta}</p>`;
    
    // Obtener las opciones mezcladas
    const opcionesMezcladas = obtenerOpcionesMezcladas(preguntaObj);

    // Mostrar las opciones mezcladas
    opcionesMezcladas.forEach((opcion, index) => {
        quizDiv.innerHTML += `<button onclick="verificarRespuesta(${preguntaObj.respuestaCorrecta}, '${opcion}')">${opcion}</button>`;
    });
}

// Función para obtener la respuesta correcta
function obtenerRespuestaCorrecta(pregunta) {
    return pregunta.opciones[pregunta.respuestaCorrecta];
}

// Función para verificar la respuesta
function verificarRespuesta(respuestaCorrecta, opcionElegida) {
    const resultDiv = document.getElementById("result");
    const quizContainer = document.getElementById("quizContainer"); // Obtener el contenedor del quiz

    // Comprobar si la opción elegida es la correcta
    if (opcionElegida === obtenerRespuestaCorrecta(preguntas[preguntaActual])) {
        respuestasCorrectas++; // Aumentar el contador si la respuesta es correcta
        resultDiv.classList.add("correcto"); // Cambiar el fondo a verde
        resultDiv.innerHTML = "¡Correcto!"; // Mensaje si la respuesta es correcta
    } else {
        resultDiv.classList.add("incorrecto");
        resultDiv.innerHTML = "Incorrecto. Intenta de nuevo."; // Mensaje si la respuesta es incorrecta
        
    }

    // Esperar 2 segundos antes de mostrar la siguiente pregunta
    setTimeout(() => {
        resultDiv.classList.remove("correcto"); // Limpiar la clase de fondo
        resultDiv.classList.remove("incorrecto"); // Limpiar la clase de fondo

        preguntaActual++;
        if (preguntaActual < preguntas.length) {
            mostrarPregunta(); // Mostrar la siguiente pregunta
        } else {
            resultDiv.innerHTML = `¡Fin del cuestionario! Respuestas correctas: ${respuestasCorrectas} de ${preguntas.length}.`;
            preguntaActual = 0; // Reiniciar el índice
            respuestasCorrectas = 0; // Reiniciar el contador
            mezclarPreguntas(preguntas); // Mezclar preguntas de nuevo
            setTimeout(mostrarPregunta, 2000); // Esperar 2 segundos antes de reiniciar
        }
    }, 2000);
}

// Iniciar el cuestionario
mostrarPregunta();
