
import sys
import numpy as np
import pandas as pd
from google.cloud import bigquery
import pandas_gbq as gbq

def CreateDataSet(client, dataset_name, project_id, dataset_description):

    '''
    Descripción: esta función crea un conjunto de datos llamado dataset_name en el proyecto dado project_id, con la data_description proporcionada, si no existe ya; si existe devuelve un mensaje. 
    Entradas:
        client: BigQueryClient, el cliente de BigQuery que creará el conjunto de datos.
        dataset_name: cadena de caracteres, el nombre del conjunto de datos que se creará.
        project_id: "string", el proyecto en el que se creará el "dataset".
        dataset_description: cadena de caracteres, la descripción del conjunto de datos.
    '''

    dataset_id = client.dataset(dataset_name, project=project_id)
    try:
        dataset=client.get_dataset(dataset_id)
        print('Dataset {} already exists.'.format(dataset.dataset_id))
    except:
        dataset = bigquery.Dataset(dataset_id)
        dataset = client.create_dataset(dataset)
        dataset.description =dataset_description
        dataset = client.update_dataset(dataset, ["description"])
        print('Dataset {} created.'.format(dataset.dataset_id))



def CreateTable(client, data, dataset_name, table_name, project_id, table_desc, table_annotation=None):
    '''
     Descripción: esta función crea un conjunto de datos llamado dataset_name en el proyecto dado project_id, con la data_description proporcionada, sobrescribe si existe una tabla con el mismo nombre.
     Entradas:
         client: BigQueryClient, el cliente de BigQuery que creará el conjunto de datos.
         data: "dataframe", los datos que se guardarán en la tabla de BigQuery.
         dataset_name: "string", el "dataset" en el que se guardará la tabla.
         table_name: cadena de caracteres, el nombre de la tabla que se creará.
         project_id: "string", el proyecto en el que se guardará el conjunto de datos.
         table_desc: cadena de caracteres, la descripción de la tabla.
         table_annotation: diccionario, el diccionario de nombres de columnas de la tabla y sus anotaciones.
    '''

    dataset_id = client.dataset(dataset_name, project=project_id)
    try:
        dataset=client.get_dataset(dataset_id)
        if table_annotation is None:
            gbq.to_gbq(data, dataset.dataset_id +'.'+ table_name, project_id=project_id, if_exists='replace')

        else:
            gbq.to_gbq(data, dataset.dataset_id +'.'+ table_name, project_id=project_id, table_schema = table_annotation , if_exists='replace')
        print("Table created successfully")

    except:
        print('Table could not be created')
    try:
        table=client.get_table(dataset.dataset_id +'.'+ table_name)
        table.description =table_desc
        table = client.update_table(table, ["description"])
        #print("Table description added successfully")
    except:
        print('Table description could not be updated')
