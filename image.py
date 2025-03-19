from docling_core.types.doc import ImageRefMode, PictureItem, TableItem
from docling.datamodel.base_models import FigureElement, InputFormat, Table
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
IMAGE_RESOLUTION_SCALE = 2.0
from pathlib import Path


pipeline_options = PdfPipelineOptions()
pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
pipeline_options.generate_page_images = True
pipeline_options.generate_picture_images = True


source="MER April 2021_0.pdf"


doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

output_dir =Path("image")  



output_dir.mkdir(parents=True, exist_ok=True) 
conv_res = doc_converter.convert(source)


table_counter =    0
picture_counter =   0

for element, _level in conv_res.document.iterate_items():
        if isinstance(element, PictureItem):
            
            picture_counter += 1

            
            element_image_filename = output_dir / f"mer_april_2010_picture-{picture_counter}.png"

            with element_image_filename.open("wb") as fp:
                element.get_image(conv_res.document).save(fp, "PNG")