from docling.document_converter import DocumentConverter
import pandas as pd

from pathlib import Path

source="MER April 2021_0.pdf"
converter = DocumentConverter()

result=converter.convert(source)

output_dir =Path("MER-Tables")  

output_dir.mkdir(parents=True, exist_ok=True) 


for table_ix, table in enumerate(result.document.tables):
    table_df: pd.DataFrame = table.export_to_dataframe()
    print(f"## Table {table_ix}")
    print(table_df.to_markdown())

    element_csv_filename = output_dir / f"table-{table_ix+1}.csv"
        
    table_df.to_csv(element_csv_filename)

