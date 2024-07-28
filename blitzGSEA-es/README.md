<img title="a title" alt="blitzGSEA" src="https://github.com/MaayanLab/blitzgsea/raw/main/icon/bgsea_small.png" width=200>

[Instalación](#installation) | [Ejemplo](#python-example) | [Parámetros opcionales](#optional-parameters) | [Aceleración](#speeding-up-enrichment-calculations) | [Graficación](#plotting-enrichment-results) | [Atribución](#attribution) | [Referencias](#references)

# Introducción a blitzGSEA

Este paquete Python proporciona una implementación computacionalmente eficiente del algoritmo de preordenación para el Análisis de Enriquecimiento de Conjuntos de Genes (GSEA) [1]. GSEApy se utilizó como referencia para el cálculo de la suma acumulada y la puntuación de enriquecimiento [2]. El algoritmo estima la distribución de la puntuación de enriquecimiento (ES) del modelo nulo ajustando los datos a distribuciones gamma en lugar de calcular permutaciones para cada conjunto de genes. blitzGSEA calcula los p-valores con una precisión mucho mayor que otras implementaciones de referencia disponibles en Python.

Las bibliotecas de conjuntos de genes pueden cargarse directamente desde Enrichr (<a href="https://maayanlab.cloud/Enrichr" target="_blank">https://maayanlab.cloud/Enrichr</a>). Para ello utilice la función `blitzgsea.enrichr.get_library()`. También se pueden listar todas las bibliotecas con `blitzgsea.enrichr.print_libraries()`.

blitzGSEA proporciona funciones de trazado para generar figuras listas para su publicación similares a las del software GSEA-P original. `blitzgsea.plot.running_sum()` traza un gráfico de enriquecimiento para un único conjunto de genes y `blitzgsea.plot.top_table()` traza los `n` principales conjuntos de genes en una tabla compacta. 

# Instalación
<span id="#installation"></span>
blitzGSEA está disponible como un paquete de Python en este repositorio GitHub y en el original de [Ma'ayan Laboratory](https://github.com/MaayanLab/blitzgsea). Puede instalar el paquete blitzGSEA Python y sus dependencias a través de pip mediante el siguiente comando:

```
$ pip install blitzgsea
```

# Análisis de enriquecimiento con blitzGSEA

blitzGSEA depende de dos archivos de entrada: 1) una firma de genes o de expresión génica y 2) una biblioteca de conjuntos de genes. La biblioteca de conjuntos de genes es un diccionario con el nombre del conjunto de genes como clave y una lista de IDs de genes como valores. Las bibliotecas de conjuntos de genes pueden cargarse directamente desde Enrichr. La firma debe ser un marco de datos de "pandas" con dos columnas [0,1]. La primera columna debe contener los identificadores de los genes (que coincidan con los IDs de los genes de la biblioteca de conjuntos de genes).

### Ejemplo en Python

Este breve ejemplo descargará 2 archivos (firma y biblioteca de conjuntos de genes). La biblioteca de conjuntos de genes consiste en rutas de la KEGG y la firma es un ejemplo de firma de expresión génica diferencial de muestras musculares de donantes jóvenes y viejos. La expresión génica diferencial se calculó con Limma Voom.

```python
import blitzgsea as blitz
import pandas as pd

# Se lee la firma como marco de datos de "pandas"
signature = pd.read_csv("https://github.com/MaayanLab/blitzgsea/raw/main/testing/ageing_muscle_gtex.tsv")

# lista de bibliotecas de conjuntos de genes disponibles en Enrichr
blitz.enrichr.print_libraries()

# Se utiliza el submódulo enrichr para recuperar la biblioteca de conjuntos de genes
library = blitz.enrichr.get_library("KEGG_2021_Human")

# Se ejecuta el análisis de enriquecimiento
result = blitz.gsea(signature, library)
```

### Ejemplo de entrada

| index | 0	| 1 |
|:-----|:-------------:|------:|
| 1	| ADO	| -7.833439 |
| 2	| CHUK	| -7.800920 |
| 3	| GOLGA4	| -7.78722 |
| ... | ... | ... |

La biblioteca de conjuntos de genes es un diccionario con los nombres de los conjuntos de genes como clave y listas de identificadores  de genes (sus correspondientes símbolos de la HUGO, en el caso de los genes humanos) como valores.

```python
{
'ERBB2 SIGNALING PATHWAY (GO:0038128)': ['CDC37',
                                          'PTPN12',
                                          'PIK3CA',
                                          'SOS1',
                                          'CPNE3',
                                          'EGF',
                                          ...
                                         ],
'HETEROTYPIC CELL-CELL ADHESION (GO:0034113)': ['DSC2',
                                                 'ITGAV',
                                                 'ITGAD',
                                                 'LILRB2',
                                                 ...
                                                ],
...
}
```

### Parámetros opcionales

La función principal de `blitzgsea.gsea()` soporta varios parámetros opcionales. Los parámetros por defecto deberían funcionar bien para la mayoría de los casos de uso. 

| nombre del parámetro | tipo | por defecto	| descripción |
|:-----|:---------|:-------------|:------|
| `permutations`	| int | 2000	| Número de permutaciones aleatorias para estimar las distribuciones de ES. |
| `min_size` | int | 5 | Número mínimo de genes en el conjunto de genes. |
| `max_size` | int | 4000 | Número máximo de genes en el conjunto de genes. |
| `anchors`	| int | 20 | Número de distribuciones del tamaño del conjunto de genes calculadas. Las restantes son interpoladas. |
| `processes`	| int | 4	| Número de hilos paralelos. No hay mucha ganancia después de 4 hilos. |
| `symmetric` | bool | False | Utiliza los mismos parámetros de distribución para ES negativos y positivos. Si su valor es `False`, se estiman por separado. |
| `signature_cache` | bool | True | Almacena en memoria los parámetros de anclaje precalculados para reutilizarlos posteriormente. |
| `shared_null` | bool | False | Usa el mismo nulo para las firmas si ya existe un modelo compatible (utiliza la prueba de divergencia KL). |
| `kl_threshold`| float | 0.3 | Controla lo similares que deben ser las distribuciones de valores de firma para su reutilización. |
| `kl_bins`| int | 200 | Número de intervalos en la representación PDF de las distribuciones para el test KL. |
| `plotting`| bool | False | Grafica los parámetros de anclaje estimados. |
| `verbose` | bool | False | Activa la salida adicional. |
| `progress` | bool | False | Activa la barra de progreso. |
| `seed` | int | 0 | Semilla aleatoria. Para la misma semilla se obtiene un resultado idéntico. Si la semilla es igual a `-1`, se genera una semilla aleatoria. |
| `add_noise` | bool | False | Añade un pequeño ruido aleatorio a la firma. El ruido es una fracción de los valores de expresión. |
| `center` | bool | True | Centrar los valores de las firmas en 0 antes de calcular la suma acumulada. |

### Aceleración de los cálculos de enriquecimiento

blitzGSEA es actualmente la implementación más rápida de GSEA. El paso que más tiempo consume en blitzGSEA es la generación de una distribución nula robusta para realizar el cálculo de los p-valores. Dado que la distribución nula depende de la distribución de valores de la firma de entrada, por defecto, blitzGSEA computará una nueva distribución nula para cada nueva firma de entrada. blitzGSEA puede calcular la similitud entre firmas de entrada utilizando la divergencia de Kullback-Leibler, a fin de identificar firmas similares para compartir modelos nulos. Se emplea un modelo nulo en caché si una firma anterior tiene una distribución de valores similar. A continuación se muestran los parámetros relevantes de la función `blitzgsea.gsea()`:

| nombre del parámetro | tipo | por defecto	| descripción |
|:-----|:---------|:-------------|:------|
| `signature_cache` | bool | True | Almacena en memoria los parámetros de anclaje precalculados para reutilizarlos posteriormente. |
| `shared_null` | bool | False | Utiliza el mismo nulo para las firmas si ya existe un modelo compatible. (utiliza el test de divergencia KL). |
| `kl_threshold`| float | 0.3 | Controla lo similares que deben ser las distribuciones de valores de firma para su reutilización. Cuanto más pequeña, más conservadora. |
| `kl_bins`| int | 200 | Número de intervalos en la representación PDF de las distribuciones para la prueba KL. |

### Example
```python

import blitzgsea as blitz
import pandas as pd

# read signature as pandas dataframe
signature = pd.read_csv("https://github.com/MaayanLab/blitzgsea/raw/main/testing/ageing_muscle_gtex.tsv")

# run enrichment analysis
result = blitz.gsea(signature, library, shared_null=True)
```

### Plotting enrichment results

blitzGSEA supports several plotting functions. `blitzgsea.plot.running_sum()` and `blitzgsea.plot.top_table()` can be used after enrichment has been performed. `blitzgsea.plot.running_sum()` shows the running sum of an individual gene set. It has a `compact` mode in which the image will be more readable if small. `blitzgsea.plot.top_table()` shows the top `n` enriched gene sets and displays the results in a table, with normalized enrichment score (NES) and the distribution of hits relative to the gene ranking of the signature.

### Example
```python

import blitzgsea as blitz
import pandas as pd

# read signature as pandas dataframe
signature = pd.read_csv("https://github.com/MaayanLab/blitzgsea/raw/main/testing/ageing_muscle_gtex.tsv")

# use enrichr submodule to retrieve gene set library
library = blitz.enrichr.get_library("KEGG_2021_Human")

# run enrichment analysis
result = blitz.gsea(signature, library)

# plot the enrichment results and save to pdf
fig = blitz.plot.running_sum(signature, "Cell adhesion molecules", library, result=result, compact=False)
fig.savefig("running_sum.png", bbox_inches='tight')

fig_compact = blitz.plot.running_sum(signature, "Cell adhesion molecules", library, result=result, compact=True)
fig_compact.savefig("running_sum_compact.png", bbox_inches='tight')

fig_table = blitz.plot.top_table(signature, library, result, n=15)
fig_table.savefig("top_table.png", bbox_inches='tight')

```

The resulting plots will look like the examples below:

#### running_sum.pdf

<div style="bachground-color: white">
<img title="a title" alt="blitzGSEA sunning_sum" src="https://github.com/MaayanLab/blitzgsea/raw/main/icon/running_sum.png" width=300>
</div>

#### running_sum_compact.pdf
<img title="a title" alt="blitzGSEA sunning_sum" src="https://github.com/MaayanLab/blitzgsea/raw/main/icon/running_sum_compact.png" width=300>

#### top_table.pdf
<img title="a title" alt="blitzGSEA sunning_sum" src="https://github.com/MaayanLab/blitzgsea/raw/main/icon/top_table.png" width=300>

### Sample shuffling
This is the sample shuffling algorithm from GSEApy. It performs a t-test to build signatures for phenotype shuffled groups. The input is a gene expression dataframe, which should be normalized for library size. `groups` is a list containing 0 or 1 describing the corresponding group for the samples in `exprs`. The index of `exprs` are the gene ids matching the gene set library. 

```python
blitz.shuffle.gsea(exprs, library, groups, permutations=50, seed=1)
```

| parameter name | type | default	| description |
|:-----|:---------|:-------------|:------|
| `exprs`	| pd.DataFrame | NA	| Normalized gene expression matrix. |
| `library` | dictionary | NA | Gene set library. |
| `groups` | list | NA | Phenotype group labels of samples. Labels are 0 or 1. |
| `permutations` | int | 1000 | Number of permutations. |
| `seed`	| int | 1 | Random state seed. |

# Dependencies
Python 3.6+

# Attribution

The statistical tool was developed by the [Ma'ayan Laboratory](https://labs.icahn.mssm.edu/maayanlab/). When using blitzgsea please cite the following reference:

Lachmann, Alexander, Zhuorui Xie, and Avi Ma’ayan. "blitzGSEA: efficient computation of gene set enrichment analysis through gamma distribution approximation." Bioinformatics (2022).
https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btac076/6526383?login=false

# References

[1] Lachmann, Alexander, Zhuorui Xie, and Avi Ma’ayan. "blitzGSEA: efficient computation of gene set enrichment analysis through gamma distribution approximation." Bioinformatics (2022).

[2] Subramanian, Aravind, Heidi Kuehn, Joshua Gould, Pablo Tamayo, and Jill P. Mesirov. "GSEA-P: a desktop application for Gene Set Enrichment Analysis." Bioinformatics 23, no. 23 (2007): 3251-3253.

[3] Fang, Zhuoqing, Xinyuan Liu, and Gary Peltz. "GSEApy: a comprehensive package for performing gene set enrichment analysis in Python." Bioinformatics (2022).
