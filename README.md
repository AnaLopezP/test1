# test1

Este grupo esta formado por Andrea Manuel, Paula Naranjo y Ana López 

TRADUCCIÓN PAGINA 2
hay una frase que me salto porque la mitad esta en la primera

En estos nuevos sistemas, están permitidos los procesos llevados a cabo por humanos [5]; i.e. procesos conocidos, ejecutados y gestionados por personas (aunque pueden estar supervisados por mecanismos digitales).
Para crear una intergración real entre las personas y la tecnología, y mover el proceso de ejecución desde el subsistema social (humanos) al mundo cibernético (componentes de hardware y software), se necesitan técnicas para la extracción de información. Muchas soluciones y enfoques de distintos tipos se han planteado durante los últimos años, pero el más prometedor, hoy dia, es la técnica de reconocimiento de patrones.
El uso de Inteligencia Artificial, modelos estadísticos y otras herramientas similares han permitido un desarrollo real e increible en el reconocimiento de patrones, aunque aún quedan pendientes algunos desafíos. 
Primero, las técnicas de reconocimiento de patrones dependen del hardware subyacente para la captura de información. La estructura y el proceso de aprendizaje cambia si, (por ejemplo), en vez de acelerómetros consideramos sensores infrarojos. Esto es bastante problemático, ya que las tecnologías de hardware avanzan mucho mas rápido que las soluciones de software. 
Y, segundo, hay un limite de precision en el proceso de reconocimiento. De hecho, así como las acciones humanas se complican, más variables y modelos más complejos se necesitan para reconocerlas. Este enfoque causa grandes problemas de optimización, cuyo error residual incrementa al igual que incrementa el numero de variables; lo que produce un decrecimiento en la tasa de reconocimiento del éxito [6]. En conclusión, las matemáticas (no el software, por tanto, no depende de la implementación) fuerzan una cierta precisión para el patrón de proceso de reconocimiento dadas las acciones a estudiar. Para evitar esta situación, se deberían de considerar un menor numero de variables, pero esto tambien reduce la complejidad de las acciones que se pudieran analizar; una solución no aceptable en escenarios industriales, donde se desarrollan actividades complejas de producción. 
Por lo tanto, el objetivo de este papel es describir un nuevo algoritmo de patrón de reconocimiento abordando estos dos problemas básicos. 


#TRADUCCION PAG 3#

categorias[9]: (i)  los Modelos Ocultos de Markov ; (ii) the Skip Chain Conditional Random 
Field (ver que es); (iii) los Prones Emergentes; (iv)  the Conditional Random Field (mirar); y (v) los clasificadores Bayesianos. 
De hecho, la mayoría de los autores proponen el uso de los modelos de Hidden Markov (HMM) para modelar las actividades humanas. HMM permitemodelar acciones como las cadenas de Markov [10][11]. Básicamete, HMM genera esados ocultos a partir de los datos observados. En particular, el objetivo final de esta técnica es construir la secuencia de los estados ocultos que encaja con ciertos datos de la secuencia. Para finalizarmente definir todo el modelo, HMM debe dedecir los datos del modelo paramétrico de una forma fiable. La figura 1 nos muestra una esquemática representación sobre cómo HMM trabaja. Cuando se reconocieron las actividades humanas, las acciones que componen las actividades son los estados ocultos, y las salidas de los sensonres son datos en estudio. Además, HMM, permite el uso de técnicas de formación considerando el conocimiento anterior sobre el modelo.  Esta formación es algo esencial para "introducir" todos los datos posibles de las secuencias requeridas para calcular el HMM. Finalmente, es my importante resaltar que el HMM aislado puede combinarse para crear modelos más grandes y complejos. 

(Figura 1. Representación gráfica de un HMM)

Sin embargo, HMM, son inútiles para modeliza ciertas actividades concurrentes, por tanto, los autores han reportado una nueva técnica llamada, Campo aleatorio Condicional (CRF). CRF se emplean para modelizar esas actividades que presentan acciones concurrentes o, en general, muchas acciones interactivas [12][13]. Además, HMM requiere un gran esfuerzo en el trabajo de descubrir 
