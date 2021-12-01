from PIL import Image, ImageEnhance


def add_watermark(image_file, logo_file, opacity=1):
    img = Image.open(image_file).convert('RGB')

    logo = Image.open(logo_file)

    base_w = (img.size[0] / 9) / float(logo.size[0])
    base_h = (img.size[0] / 12) / float(logo.size[1])

    logo_w = int(float(logo.size[0]) * float(base_h))
    logo_h = int(float(logo.size[1]) * float(base_w))

    logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)

    # position the watermark
    offset_x = (img.size[0] - logo.size[0]) - 10
    offset_y = (img.size[1] - logo.size[1]) - 10

    watermark = Image.new('RGBA', img.size, (255, 255, 255, 1))
    watermark.paste(logo, (offset_x, offset_y), mask=logo.split()[3])

    alpha = watermark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)

    watermark.putalpha(alpha)
    Image.composite(watermark, img, watermark).save(image_file, 'JPEG')
