from framechain.chains.decorator import chain
from framechain.schema import RunInput, RunOutput
from framechain.utils.channel_format import ChannelFormat, convert_channel_format
from framechain.utils.types import Image
from PIL import ImageOps, ImageEnhance, ImageFilter


@chain()
def adjust_sharpness(image: Image, factor: float) -> Image:
    enhancer = ImageEnhance.Sharpness(image)
    return enhancer.enhance(factor)