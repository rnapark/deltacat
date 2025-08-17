# utils/config_loader.py
import yaml
from deltacat.catalog.model.properties import CatalogProperties


def load_catalog_config_from_yaml(config_path: str) -> CatalogProperties:
    with open(config_path, "r") as f:
        config_dict = yaml.safe_load(f)
    return CatalogProperties(**config_dict)
