from PIL import ImageDraw, Image, ImageFont

COLORS = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'yellow': (255, 255, 0),
    'white': (255, 255, 255),
    'black': (0, 0, 0),
    'grey': (200, 200, 200),
    'water': (51, 51, 204),
    'mountain': (166, 166, 166),
    'forest': (45, 134, 45),
    'grassland': (179, 255, 179),
    'road': (191, 128, 64),
}


def draw(nodes, path, open_nodes, closed_nodes, lines, img_path):
    """
    Visualize board, path, open and closed nodes using python imaging library
    :param nodes: All nodes
    :param path: Nodes in resolves path from start to target
    :param open_nodes: Open nodes left unchecked during path resolve
    :param closed_nodes: Checked nodes during path resolve
    :param lines: lines in board
    :param img_path: Path to save image
    """
    height = len(lines)
    width = len(lines[0])
    img = Image.new('RGBA', (width*50, height*50), (255, 255, 255))
    dr = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('./Fonts/Roboto-Black.ttf', 13)

    for i in range(width):
        for j in range(height):
            node = list(filter(lambda n: n.x == i and n.y == j, nodes))[0]

            if node.description == 'Water': color = COLORS['water']
            elif node.description == 'Mountain': color = COLORS['mountain']
            elif node.description == 'Forest': color = COLORS['forest']
            elif node.description == 'Grassland': color = COLORS['grassland']
            elif node.description == 'Road': color = COLORS['road']
            elif node.obstacle: color = COLORS['black']
            else: color = COLORS['grey']

            dr.rectangle([(50*i, 50*j), (50+50*i, 50+50*j)], fill=color, outline="black")

            if node.start:
                dr.text((50*i+6, 50*j+4), "START", font=fnt, fill=COLORS['black'])
            elif node.target:
                dr.text((50*i+2, 50*j+4), "TARGET", font=fnt, fill=COLORS['black'])

            ellipse = [(50*i+20, 50*j+20), (50+50*i-20, 50+50*j-20)]

            if node in path:
                dr.ellipse(ellipse, fill=COLORS['green'])
            elif node in open_nodes:
                dr.ellipse(ellipse, fill=COLORS['yellow'])
            elif node in closed_nodes:
                dr.ellipse(ellipse, fill=COLORS['red'])

            dr.line([(25+node.x*50, 50+node.y*50-25) for node in path], fill=COLORS['green'], width=3)
            
    img.save(img_path, 'PNG')
