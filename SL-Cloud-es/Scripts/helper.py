
from google.cloud import bigquery
import pandas as pd

def ConvertGene(client, input_vector, input_type, output_type):
    '''
    Descripción: esta función proporciona la conversión entre EntrezID, Gene y Alias.
    Entradas:
        client: BigQueryClient, el cliente BigQuery que realizará la operación.
        input_vector: lista de enteros o cadenas de caracteres (dependiendo la entrada)	
        input_type: "string", valores válidos: 'Alias', 'Gene', 'EntrezID'.
        output_type: lista de cadenas de caracteres,  tipo de salida debe ser un vector como ['Gene', 'EntrezID'].
    '''
    sql='''
    SELECT DISTINCT __IN_TYPE__,  __OUT_TYPE__
   
    FROM  `isb-cgc-bq.annotations.gene_info_human_NCBI_current`
    where  __IN_TYPE__  in (__IN_VECTOR__)
    '''

    if input_type=='EntrezID':
        intermediate_representation = [str(x) for x in input_vector]
    else:
        intermediate_representation = ["'"+str(x)+"'" for x in input_vector]

    input_vector_query= ','.join(intermediate_representation)

    out_type_intermediate_representation = [str(x) for x in output_type]
    output_type_for_query= ','.join(out_type_intermediate_representation)

    sql=sql.replace('__OUT_TYPE__', output_type_for_query)
    sql=sql.replace('__IN_TYPE__', input_type)
    sql=sql.replace('__IN_VECTOR__', input_vector_query)

    result= client.query(sql).result().to_dataframe()
    return(result)


def WriteToExcel(excel_file, data_to_write, excel_tab_names):
    '''
    Descripción: esta función escribe los marcos de datos cuyos nombres se dan en el parámetro data_to-write en los archivos Excel cuyos nombres se proporcionan en el parámetro excel_file_names.
    Entradas:
       excel_file: "string", el nombre del archivo Excel en el que se escribirán los datos. 
       data_to_write: lista de "dataframes", los marcos de datos que se escribirán en las pestañas del libro de Excel.
       excel_tab_names: lista de cadenas de caracteres, los nombres de las pestañas del archivo Excel, en el mismo orden que los "dataframes" que se escribirán.
    
    '''
    with pd.ExcelWriter(excel_file) as writer:
        for i in range(len(excel_tab_names)):
            data_to_write[i].to_excel(writer, sheet_name=excel_tab_names[i], index=False)

