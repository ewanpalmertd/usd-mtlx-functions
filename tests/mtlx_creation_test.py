from pxr import Usd, Sdf, UsdShade

def MtlxNodeTest(filename:str = None) -> None:
    """ using UsdShade API to create a dummy materialx prim to be loaded into 
    houdini

    :params:
    filename(str) : the name of the output usda file
    """
    stage    = Usd.Stage.CreateNew(filename)
    material = UsdShade.Material.Define(stage, "/materials/MTL_test")

    surface = UsdShade.Shader.Define(stage, "/materials/MTL_test/surface")
    surface.CreateIdAttr("ND_surface")

    diffuseBsdf = UsdShade.Shader.Define(stage, "/materials/MTL_test/diffuse_bsdf")
    diffuseBsdf.CreateIdAttr("ND_oren_nayar_diffuse_bsdf")
    diffuseBsdf.CreateInput("color", Sdf.ValueTypeNames.Color3f).Set((0.18, 0.18, 0.18))
    diffuseBsdf.CreateInput("normal", Sdf.ValueTypeNames.Vector3f).Set((0, 0, 0))
    diffuseBsdf.CreateInput("roughness", Sdf.ValueTypeNames.Float).Set(0)
    diffuseBsdf.CreateInput("weight", Sdf.ValueTypeNames.Float).Set(0.8)
    diffuseBsdf.CreateOutput("out", Sdf.ValueTypeNames.Token)

    surface.CreateInput("bsdf", Sdf.ValueTypeNames.String).ConnectToSource(diffuseBsdf.ConnectableAPI(), "out")
    material.CreateSurfaceOutput().ConnectToSource(surface.ConnectableAPI(), "out")

    stage.Save()


if __name__ == "__main__":
    MtlxNodeTest("mtlx_test.usda")