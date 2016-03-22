from PIL import Image, ImageColor, ImageFont, ImageDraw
from os import path

composite = Image.new('RGBA', (1280, 720), color=ImageColor.getcolor('white', 'RGBA'))

nl_image = Image.open('C:/Temp/Femmopt/NelderMead_035.bmp')
dl_image = Image.open('C:/Temp/Femmopt/DirectL_020.bmp')

nl_search = Image.open('C:/Temp/Femmopt/NelderMead_searchpath_033.png')
dl_search = Image.open('C:/Temp/Femmopt/DirectL_searchpath_071.png')

objective = Image.open('C:/Temp/Femmopt/Objective_098.png')

nl_image = nl_image.crop((0, 0, 310, 616))
dl_image = dl_image.crop((0, 0, 310, 616))

composite.paste(nl_image, (20, 80))
composite.paste(dl_image, (360, 80))
composite.paste(nl_search, (700, 420))
composite.paste(dl_search, (990, 420))
composite.paste(objective, (700, 80))

font = ImageFont.truetype(path.join("c:/windows/font", "consola.ttf"), 20)
draw = ImageDraw.Draw(composite)
draw.text((20, 20), 'LOCAL SEARCH', font=font, fill='black')
draw.text((20, 45), 'Nelder-Mead', font=font, fill='black')
draw.text((360, 20), 'GLOBAL SEARCH', font=font, fill='black')
draw.text((360, 45), 'Direct-L', font=font, fill='black')
draw.text((700, 60), 'OBJECTIVE FUNCTION VALUE', font=font, fill='black')
draw.text((700, 400), 'SEARCH PATH', font=font, fill='black')
draw.text((890, 400), 'local', font=font, fill='black')
draw.text((1170, 400), 'global', font=font, fill='black')

font = ImageFont.truetype(path.join("c:/windows/font", "consola.ttf"), 16)

draw.text((230, 620), 'current', font=font, fill='black')
draw.text((230, 638), 'yc = 1.000', font=font, fill='black')
draw.text((230, 656), 'r  = 1.000', font=font, fill='black')
draw.text((230, 674), 'E  = 0.234', font=font, fill='black')

draw.text((570, 620), 'BEST', font=font, fill='black')
draw.text((570, 638), 'yc = 1.000', font=font, fill='black')
draw.text((570, 656), 'r  = 1.000', font=font, fill='black')
draw.text((570, 674), 'E  = 0.234', font=font, fill='black')

composite.save('C:/Temp/Femmopt/Composite.png')
