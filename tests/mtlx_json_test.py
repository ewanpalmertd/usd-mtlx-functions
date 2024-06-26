from typing import List, Dict
import hou

def getPropertiesDictFromNode(node: hou.LopNode) -> Dict:
    """
    creates a dictionary containing node input and output parms for conversion to UsdShade shader
    
    :params:
    node : the node to create dictionary from

    :returns: 
    dictionary with keys {shader name, shader inputs, shader outputs}
    """

    parmTemplateList: List[hou.ParmTemplate] = []
    for parameter in node.parms():
        if parameter.name() == "signature": continue # signatue is a UsdShade incompatible houdini native parameter found on materialx nodes
        parmTemplateList.append(parameter.parmTemplate())

    parmTemplateList = list(set(parmTemplateList)) # removes duplicates from parmtuple parameters

    nodeProperties: Dict = {
        "name": "ND_standard_surface_surfaceshader", # absolute name for the time being
        "inputs" : {},
        "outputs": {} }
    
    for parm in parmTemplateList:
        parmType:str = str(parm.type()).split(".")[-1]

        if parmType == "FolderSet": continue
        if parmType == "Toggle":
            parmType = "Int"

        parmName:str    = parm.name()
        parmLabel:str   = parm.label()
        parmLength: int = parm.numComponents()

        # need to distinduish Color3f and Vector3f data types
        if parmLength > 1:
            suffix: str = f"{parmLength}{parmType.split('.')[-1][0].lower()}"
            default = node.parmTuple(parmName).eval()
            parmType = f"Color{suffix}" if node.parm(f"{parmName}r") else f"Vector{suffix}"

        else:
            default = node.evalParm(parmName)

        nodeProperties["inputs"][parmName] = [default, parmType]

    for output in node.outputNames():
        nodeProperties["outputs"][output] = "Token" # all materialx nodes come with output type as Token

    return nodeProperties

def exportPropertiesToJson(propertiesDict: Dict) -> None:
    """
    converts the input dictionary of materialx properties to a json file to be used in MtlXAPI

    :params:
    propertiesDict : the input dictionary of properties using correct JSON formatting
    """
    import json

    jsonDict: Dict = json.dumps(propertiesDict, indent=4)
    with open("mtlx_standardsurface.json", "w") as file:
        json.dump(jsonDict, file)
    


