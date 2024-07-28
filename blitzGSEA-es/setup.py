import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="blitzgsea",
    version="1.3.36",
    author="Alexander Lachmann",
    author_email="alexander.lachmann@mssm.edu",
    description="Paquete para el cálculo rápido y preciso del Análisis de Enriquecimiento de Conjuntos de Genes (GSEA), similar a la preordenación, utilizando una aproximación de distribución gamma.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maayanlab/blitzgsea",
    packages=setuptools.find_packages(),
    classifiers=[
        "Lenguaje de programación :: Python :: 3",
        "Licencia :: Aprobado por la ISO :: Licencia de software Apache",
        "Sistema operativo :: Independiente del sistema operativo",
    ],
    package_data={
        "blitzgsea": ["data/*"]
    },
    include_package_data=True,
    install_requires=[
        'pandas>=1.1.5',
        'numpy',
        'scikit-learn',
        'tqdm',
        'statsmodels',
        'mpmath'
    ],
    python_requires='>=3.6',
)
