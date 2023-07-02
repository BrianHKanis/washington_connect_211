from etl.load_export.src.api_export import export_files
from etl.load_export.settings import api_writer_root_url

export_files(api_writer_root_url)