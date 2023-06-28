from etl.load_export.src.api_export import merge_endpoints, export_files
from etl.load_export.settings import api_reader_root_url

merged = merge_endpoints()
export_files(api_reader_root_url, merged)