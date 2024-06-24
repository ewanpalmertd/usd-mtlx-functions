import json

class MtlxDatabase:

    def GetInfoFromHoudini() -> None:
        """ uses houdini VOPs to create and get all usd properties from 
        materialx nodes
        
        :return: json dictionary containing node information
        """
        import hou
        
        stage: hou.Node = hou.node("/stage")
        materialLibrary: hou.LopNode = stage.createNode("materiallibrary", node_name="materialx_lib")
        subnet: hou.VopNode = materialLibrary.createNode("subnet", node_name="Material")
        subnet.setMaterialFlag(True)
        
        # creating one of each materialx node
        for type, node in hou.vopNodeTypeCategory().nodeTypes().items():
            if not type.startswith("mtlx"): continue
            
            mtlxNode = subnet.createNode(type)
            
        subnet.layoutChildren()
  
MtlxDatabase.GetInfoFromHoudini() # for testing in houdini
        
if __name__ == "__name__":
    MtlxDatabase.GetInfoFromHoudini()
        
        