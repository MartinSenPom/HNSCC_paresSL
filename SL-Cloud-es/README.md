# Synthetic Lethality Cloud (SL-Cloud)

Este proyecto proporciona una plataforma de acceso a datos basada en la nube junto con software y cuadernos computacionales bien documentados que reimplementan algoritmos de inferencia de letalidad sintética (SL) publicados para facilitar la investigación novedosa de la letalidad sintética. Además, proporcionamos funciones de propósito general que apoyan estos flujos de trabajo de predicción, por ejemplo, guardar datos en tablas bigquery. Anticipamos que los usuarios con conocimientos informáticos pueden aprovechar los recursos proporcionados en este proyecto para llevar a cabo análisis altamente personalizables basados en su tipo de cáncer de interés y contexto particular. 

Abra el marco en **MyBinder**: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/isb-cgc/Community-Notebooks/HEAD?labpath=SL-Cloud%2FMyBinder_Authentication.ipynb)

Cita: 
Bahar Tercan, Guangrong Qin, Taek-Kyun Kim, Boris Aguilar, Christopher J. Kemp, Nyasha Chambwe, Ilya Shmulevich. SL-Cloud: A Computational Resource to Support Synthetic Lethal Interaction Discovery. BioRxiv 2021.09.18.459450; doi: https://doi.org/10.1101/2021.09.18.459450

 Si tiene alguna pregunta, póngase en contacto con Bahar Tercan btercan@isbscience.org. 
## Primeros pasos

### Conseguir una identidad Google

Para poder utilizar nuestra plataforma, los investigadores primero deben tener una identidad de Google; si no la tiene, haga clic en [aquí](https://accounts.google.com/signup/v2/webcreateaccount?dsh=308321458437252901&continue=https%3A%2F%2Faccounts.google.com%2FManageAccount&flowName=GlifWebSignIn&flowEntry=SignUp#FirstName=&LastName=) también puede vincular una cuenta que no sea de Gmail(como sluser<span>@isbscience.org</span>) como una identidad de Google mediante [este método](https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp&nogm=true).

### Solicitar créditos de Google Cloud

Benefíciese de un único [crédito de Google de 300 $](https://cloud.google.com/free/).
Si ya ha utilizado esta oferta única (o existe algún otro motivo por el que no puede utilizarla), consulte esta información sobre cómo [solicitar créditos en la nube de ISB-CGC](https://isb-cancer-genomics-cloud.readthedocs.io/en/latest/sections/HowtoRequestCloudCredits.html).

### Configurar un proyecto de Google Cloud

Consulte la documentación de Google sobre cómo crear un [Proyecto de Google Cloud](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

[Habilitar las API de Google Cloud requeridas](https://cloud.google.com/apis/docs/getting-started#enabling_apis)

### First Notebook

Por favor, ejecute el [primer cuaderno](https://github.com/isb-cgc/SL-Cloud-F1000/blob/main/first_notebook.ipynb) para empezar a utilizar nuestras tablas bigquery desde su ordenador.  

## ¿Qué hay en el proyecto?
### Scripts
- [Carpeta de scripts](https://github.com/isb-cgc/SL-Cloud-F1000/tree/main/Scripts/): incluye las funciones utilizadas por los flujos de trabajo DAISY y Mutation Dependent SL Inference que se explican a continuación. Esta carpeta también contiene scripts para procedimientos de manipulación de datos como la creación de conjuntos de datos y tablas BigQuery, cómo guardar datos DEPMAP en tablas BigQuery, funciones de ayuda como la escritura de marcos de datos en archivos Excel y la conversión de genes entre símbolos de genes, EntrezID y alias.

### Flujos de trabajo de inferencia de letalidad sintética 
Puede encontrar cuadernos de ejemplo en el directorio Example_pipelines, que incluye los siguientes cuadernos:
- [Tubería DAISY](https://github.com/isb-cgc/SL-Cloud-F1000/blob/main/Example_workflows/DAISY_example.ipynb): Reimplementamos el flujo de trabajo publicado DAISY (Jerby-Arnon et al., 2014) utilizando recursos de datos a gran escala actualizados. </br>
- [Tubería LS dependiente de mutaciones](https://github.com/isb-cgc/SL-Cloud-F1000/blob/main/Example_workflows/MDSLP_example.ipynb): Implementamos un flujo de trabajo de predicción de letalidad sintética dependiente de mutaciones (MDSLP) basado en el razonamiento de que para tumores con mutaciones que tienen un impacto en la expresión de proteínas o en la estructura de proteínas (mutación funcional), los efectos de "knockout" o inhibición de un gen diana asociado muestran una dependencia condicional para las entidades moleculares mutadas.</br>
- [Inferencia basada en la conservación a partir de interacciones genéticas en levaduras](https://github.com/isb-cgc/SL-Cloud-F1000/blob/main/Example_workflows/CGI_example.ipynb): Presentamos un flujo de trabajo que aprovecha la conservación entre especies, para inferir interacciones letales sintéticas en levaduras derivadas experimentalmente, a fin de predecir pares LS relevantes en humanos. Implementamos el flujo de trabajo Conserved Genetic Interaction (CGI) basándonos, en parte, en los métodos descritos en (Srivas et al., 2016). </br>

### Recursos de datos de inferencia de letalidad sintética
Este recurso proporciona acceso a conjuntos de datos genómicos sobre el cáncer disponibles públicamente y relevantes para la inferencia de SL. Estos datos se han preprocesado, limpiado y almacenado en tablas consultables basadas en la nube aprovechando la tecnología [Google BigQuery](https://cloud.google.com/bigquery). Además, aprovechamos los conjuntos de datos relevantes disponibles a través del Institute for Systems Biology Cancer Genomics Cloud ([ISB-CGC](https://isb-cgc.appspot.com/)) para hacer inferencias de posibles interacciones letales sintéticas. 
A continuación se presentan conjuntos de datos específicos de proyectos con relevancia para la inferencia de LS:

- **DEPMAP**: DEPMAP shRNA (DEMETER2 V6) y CRISPR (DepMap Public 20Q3) expresión génica, información de la muestra, mutación y alteraciones del número de copias para experimentos CRISPR y puntuaciones de dependencia génica para shRNA y puntuaciones de efecto génico.

- **CellMap**: Conjunto de datos de interacción de levaduras basado en puntuaciones de eficacia biológica tras "knockouts" simples y dobles de experimentos de SGA.

- **Gene Information**: Tablas con información relevante sobre anotación de genes, como información sobre ortólogos humanos y de levadura, mapeo gen-alias-Entrez ID, mapeo de ID de genes Ensembl, mapeo gen-Refseq.


### Acceso a los recursos del ISB-CGC
Para poder ver los datos en el proyecto ISB-CGC, por favor clique en https://console.cloud.google.com/bigquery y añada el conjunto de datos de letalidad sintética. Para ello, los usuarios necesitan fijar el proyecto de LS haciendo clic primero en "+ AGREGAR" y, después, seleccionando "Destaca un proyecto por nombre", entre las "Fuentes adicionales" disponibles. Entonces, aparecerá una ventana denominada "Destacar un proyecto". Por último, luego de escribir isb-cgc-bq en la casilla "Nombre del proyecto", haga clic en "DESTACAR". 
