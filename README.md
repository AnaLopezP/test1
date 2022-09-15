# test1

Este grupo esta formado por Andrea Manuel, Paula Naranjo y Ana López 

TRADUCCIÓN PAGINA 2
hay una frase que me salto porque la mitad esta en la primera

En estos nuevos sistemas, están permitidos los procesos llevados a cabo por humanos [5]; i.e. procesos conocidos, ejecutados y gestionados por personas (aunque pueden estar supervisados por mecanismos digitales).
Para crear una intergración real entre las personas y la tecnología, y mover el proceso de ejecución desde el subsistema social (humanos) al mundo cibernético (componentes de hardware y software), se necesitan técnicas para la extracción de información. Muchas soluciones y enfoques de distintos tipos se han planteado durante los últimos años, pero el más prometedor, hoy dia, es la técnica de reconocimiento de patrones.
El uso de Inteligencia Artificial, modelos estadísticos y otras herramientas similares han permitido un desarrollo real e increible en el reconocimiento de patrones, aunque aún quedan pendientes algunos desafíos. 
Primero, las técnicas de reconocimiento de patrones dependen del hardware subyacente para la captura de información. La estructura y el proceso de aprendizaje cambia si, (por ejemplo), en vez de acelerómetros consideramos sensores infrarojos. Esto es bastante problemático, ya que las tecnologías de hardware avanzan mucho mas rápido que las soluciones de software. 
Y, segundo, hay un limite de precision en el proceso de reconocimiento. De hecho, así como las acciones humanas se complican, más variables y modelos más complejos se necesitan para reconocerlas. Este enfoque causa grandes problemas de optimización, cuyo error residual incrementa al igual que incrementa el numero de variables; lo que produce un decrecimiento en la tasa de reconocimiento del éxito [6]. En conclusión, las matemáticas (no el software, por tanto, no depende de la implementación) fuerzan una cierta precisión para el proceso de reconocimiento de patrones dadas las acciones a estudiar. Para evitar esta situación, se deberían de considerar un menor numero de variables, pero esto tambien reduce la complejidad de las acciones que se pudieran analizar; una solución no aceptable en escenarios industriales, donde se desarrollan actividades complejas de producción. 
Por lo tanto, el objetivo de este papel es describir un nuevo algoritmo de reconocimiento de patrones abordando estos dos problemas básicos. El mecanismo propuesto define las acciones como una composición de movimientos simples. Los movimientos simples se reconocen usando tecnicas de Dynamic Time Warping (DTW) [7].Este proceso depende del harware seleccionado para la captura de información, pero las DTW son muy flexibles y actualizar el repositorio del patrón es suficiente para reconfigurar el algoritmo en su totalidad. Entonces, las acciones complejas se reconocen como combinaciones de movimietnos simples mediante Modelos Escondidos de Markov (HMM). Estos modelos son completamente independientes de las tecnologías de hardware, ya que solo consideran acciones simples. Este enfoque de dos pasos tambien reduce la complejidad de los modelos, incrementando la tasa de precisión y éxito en el proceso de reconocimiento.
El resto del papel está organizado de la siguiente manera: la Sección 2 describe el estado del arte en el reconocimiento de patrones de actividades humanas; la Sección 3 describe la solución propuesta, incluyendo las dos fases ya definidas; la Sección 4 presenta una validación experimental usando un escenario real y usuarios finales; y la Sección 5 concluye el papel.

2. Estado del arte en el reconocimiento de patrones
Se han reportado muchas tecnicas de reconocimiento de patrones diferentes para actividades humanas. De cualquier manera, las propuestas más comunes se pueden clasificar en cinco básicas...


#TRADUCCION PAG 3#

categorias[9]: (i)  los modelos Ocultos de Markov ; (ii) campo aleatorio condicional de la cadena de saltar; (iii) los patrones emergentes; (iv)  the Conditional Random Field (mirar); y (v) los clasificadores bayesianos. 
De hecho, la mayoría de los autores proponen el uso de los modelos de Hidden Markov (HMM) para modelar las actividades humanas. HMM permitemodelar acciones como las cadenas de Markov [10][11]. Básicamete, HMM genera esados ocultos a partir de los datos observados. En particular, el objetivo final de esta técnica es construir la secuencia de los estados ocultos que encaja con ciertos datos de la secuencia. Para finalizarmente definir todo el modelo, HMM debe dedecir los datos del modelo paramétrico de una forma fiable. La figura 1 nos muestra una esquemática representación sobre cómo HMM trabaja. Cuando se reconocieron las actividades humanas, las acciones que componen las actividades son los estados ocultos, y las salidas de los sensonres son datos en estudio. Además, HMM, permite el uso de técnicas de formación considerando el conocimiento anterior sobre el modelo.  Esta formación es algo esencial para "introducir" todos los datos posibles de las secuencias requeridas para calcular el HMM. Finalmente, es my importante resaltar que el HMM aislado puede combinarse para crear modelos más grandes y complejos. 

(Figura 1. Representación gráfica de un HMM)

Sin embargo, HMM, son inútiles para modeliza ciertas actividades concurrentes, por tanto, los autores han reportado una nueva técnica llamada, Campo aleatorio Condicional (CRF). CRF se emplean para modelizar esas actividades que presentan acciones concurrentes o, en general, muchas acciones interactivas [12][13]. Además, HMM requiere un gran esfuerzo en el trabajo de descubrir todos los posibles estados ocultos. Para resolver estos problemas, Campo aleatorio Condicnional (CRF) emplea probabilidades condicionales en vez de unir las distribucines de probabilidad. De esta manera, las actividades cuyas acciones son desarrolladas en algún orden pueden ser más fácil de modelar. A diferencia que las cadenas en HMM, CRF emplea grafos acíclicos, y permite la integración condicionada de los estados ocultos (estados que dependen de las observaciones pasadas y/o futuras).

Por otro lado, los CFR, siguen siendo inútiles para modelizar ciertos comportamientos, por lo que algunas propuestas generalizan este concepto y proponen el campo aleatorio condicional de la cadena de saltar (SCCRF). SCCRF es una técnica de reconocimiento de patrones, más general que CRF, que permite modelizar actividades que no sean secuenciales de las acciones en la naturaleza
