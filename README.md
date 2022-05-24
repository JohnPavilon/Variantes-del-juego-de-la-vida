# Variantes-del-juego-de-la-vida

# 1. Resumen

Como el nombre lo indica, se tratan de diferentes reglas de evolución para el autómata celular bidimensional conocido como "El juego de la vida".
Algunas de estas reglas pueden ser encontradas y leídas en el siguiente enlace: 

<p align="center">
  https://es.wikipedia.org/wiki/Juego_de_la_vida#Variantes
</p>

# 2. Ejecución del programa

Para proceder a ejecutar el programa, se requerirá primeramente que se descargue la carpeta Variantes-del-juego-de-la-vida/ adjunto a su contenido. Además de lo anterior, deberá tener instalado la biblioteca PyGame, en caso de no tenerlo instalado consulte el siguiente enlace: https://www.pygame.org/wiki/GettingStarted

Posteriormente, se ejecutará alguno de los archivos con terminación .py localizado en Variantes-del-juego-de-la-vida/, este archivo se puede ejecutar dentro de una terminal (esto se puede realizar utilizando el comando "python3 [nombre del archivo].py", asegúrate de que la terminal se encuentre en la carpeta donde se ubica "[nombre del archivo].py" usando el comando cd, de lo contrario te marcará el error de archivo no encontrado) o ejecutando el script con algún IDE (como lo es el caso del programa Anaconda, Spider o Visual Studio Core disponible para Windows, Linux y Mac, puedes consultar el método de instalación en el siguiente enlace: https://docs.anaconda.com/anaconda/install/index.html)

Con lo anterior realizado, usted verá que se iniciará el programa abriendo una ventana, mostrando en pantalla una interfaz en donde se mostrará una cuadrícula azul con la cual el usuario podrá interactuar.

# Controles
<p align="center">
  Presione click izquierdo del mouse para asignar el estado "vivo" a la celula
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155262708-6b663a10-2466-48db-ad6f-1c181b1704a7.gif" alt="animated" />
</p>

<p align="center">
  En caso de querer "matar" a la celula, presione click derecho
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155408321-839f8d28-6151-462c-8056-b46a3f6b5818.gif" alt="animated" />
</p>

<p align="center">
  Una vez establecido la configuración inicial, para proceder a la siguiente generación presione la tecla Enter
</p>


<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155263660-8eab2da0-f783-4f92-b1d6-d128ee6bdd6e.gif" alt="animated" />
</p>

<p align="center">
  Si se desea dejar corriendo "el juego de la vida", presione la tecla Space. Presione nuevamente la tecla si se desea pausar.
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155414472-ce985a3f-465c-4fc0-923d-d147094fcc68.gif" alt="animated" />
</p>

<p align="center">
  En caso de querer reiniciar el juego, presione la tecla Backspace (Esta se localiza encima de la tecla Enter)
</p>

<p align="center">
  <img src="https://user-images.githubusercontent.com/75518367/155264886-3f42fb4e-8b6f-4c92-84b2-9c9d4822f9e5.gif" alt="animated" />
</p>

# 3. Listas de variantes

<p align="center">
  1. Variante 235678/3678 (Mancha de Tinta)
</p>

<p align="center">
  <img src="https://media4.giphy.com/media/ja6K5Dzx6ygaDWXtHD/giphy.gif" alt="animated" />
</p>

<p align="center">
  2. Variante 245/368 (muerte, locomotoras y naves)
</p>

<p align="center">
  <img src="https://media2.giphy.com/media/oRqIYS6wbtxZU0sEeZ/giphy.gif" alt="animated" />
</p>

<p align="center">
  3. Variante 34/34 (crece) «Vida 34»
</p>

<p align="center">
  <img src="https://media1.giphy.com/media/20FmaY7kCvFdsEIJLK/giphy.gif" alt="animated" />
</p>

# 4. Información del contenido

A continuación se mostrará la lista de elementos contenidos en Variantes-del-juego-de-la-vida/ junto a una somera descripción de los mismos:

Variantes-del-juego-de-la-vida/

1. README.md: Es el archivo que está leyendo en este momento
2. game-of-life.py: Ejecuta una simulación del juego de la vida con las reglas 23/3 (una célula nace si tiene 3 vecinas y vive siempre que haya 2 o 3 vecinas)
3. ink_stain.py: Simula las reglas 235678/3678 (mancha de tinta que se seca rápidamente)
4. train_and_ships.py: Variante 245/368 (muerte, locomotoras y naves)
5. life_34.py: Ejecuta la variante 34/34 (Vida 34)
