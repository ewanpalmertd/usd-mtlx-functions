from pxr import Usd, Sdf, UsdShade

"""
quick test to make sure that writing mtlx properties to an empty shader prim
translates to a materialx node inside of Houdini
"""

layer = Sdf.Layer.CreateNew("mtlx_test.usda")

root_path  = Sdf.Path("/materials")
mat_path   = root_path.AppendChild("mtl_materialx_test")
const_path = mat_path.AppendChild("constant_test")

root_spec  = Sdf.CreatePrimInLayer(layer, root_path)
mat_spec   = Sdf.CreatePrimInLayer(layer, mat_path)
const_spec = Sdf.CreatePrimInLayer(layer, const_path)

root_spec.specifier  = Sdf.SpecifierDef
mat_spec.specifier   = Sdf.SpecifierDef
const_spec.specifier = Sdf.SpecifierDef

root_spec.typeName  = "Scope"
mat_spec.typeName   = "Material"
const_spec.typeName = "Shader"


layer.Save()