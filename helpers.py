import io
from PIL import Image as pil_image


def image_load_img_manual(
  image_bytes,
  target_size=None,
):
  """Load image from bytes.

  Args:
    image_bytes: Bytes of image.
    target_size: Target size.

  Source:
    tf.keras.utils.load_img
    https://github.com/keras-team/keras/blob/v2.14.0/keras/utils/image_utils.py
  """
  img = pil_image.open(io.BytesIO(image_bytes))

  try:
    pil_image_resampling = pil_image.Resampling
  except AttributeError:
    pil_image_resampling = pil_image

  if target_size is not None:
    width_height_tuple = (target_size[1], target_size[0])
    if img.size != width_height_tuple:

      # assuming `interpolation` is 'nearest'
      resample = pil_image_resampling.NEAREST

      # `if keep_aspect_ratio:` deleted
      # assuming `keep_aspect_ratio` is False
      img = img.resize(width_height_tuple, resample)

  return img
