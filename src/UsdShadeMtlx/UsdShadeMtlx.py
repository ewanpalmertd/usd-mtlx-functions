import json
from pxr import Usd, Sdf, UsdShade

class MtlxShade:

    def __init__(self, layer, path:str, nodeType:str) -> None:
        self.layer = layer
        self.path  = path
        self. nodeType = nodeType