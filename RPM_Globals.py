import bpy


class RPM_Globals(bpy.types.PropertyGroup):
    avatar_id: bpy.props.StringProperty(
        name="Avatar ID",
        description="The ID of the avatar you want to use",
        default="63ac69548d4fc7b44d50de62")

    quality: bpy.props.EnumProperty(
        name="Quality",
        description="""\
The quality of the avatar you want to use: \n\n \
not_set: The avatar will be downloaded without any optimization.  \n\n \
low:     meshLod=2, textureSizeLimit=256, textureAtlas=256, morphTargets=none \n\n \
medium:  meshLod=1, textureSizeLimit=512, textureAtlas=512, morphTargets=none) \n\n \
high:    meshLod=0, textureSizeLimit=1024, textureAtlas=1024, morphTargets=none)\n\n \
""",
        items=[
            ("not_set", "-", "Not set"),
            ("low", "Low", "Low quality"),
            ("medium", "Medium", "Medium quality"),
            ("high", "High", "High quality")
        ],
        default="not_set"
    )
