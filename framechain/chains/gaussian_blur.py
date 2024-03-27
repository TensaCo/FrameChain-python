from framechain.chains.decorator import chain
from framechain.schema import RunInput, RunOutput
from framechain.utils.channel_format import ChannelFormat, convert_channel_format
from framechain.utils.types import Image
from PIL import ImageOps, ImageEnhance, ImageFilter

@chain()
def gaussian_blur(image: Image, radius: float) -> Image:
    return image.filter(ImageFilter.GaussianBlur(radius))
