from PIL import Image, ImageDraw

colors = {
    0: '#FF0000',   # RED
    1: '#0000FF',   # BLUE
    2: '#FFFF00',   # YELLOW
    3: '#008000',   # GREEN
    4: '#FF8C00',   # ORANGE
    5: '#FFFFFF'    # WHITE
}

def show_cube(cube):
    ''' This function shows the actual state of all the Cube faces '''
    n = len(cube.BACK)
    square_size = 25
    padding = 5
    face_size = n*square_size
    width, height = (face_size*4 + padding*5, face_size*3 + padding*4)

    cube_img = Image.new('RGBA', (width, height), (255,255,255,0))
    d = ImageDraw.Draw(cube_img)

    draw_face(d, cube.LEFT, square_size, padding, padding*2 + face_size)
    draw_face(d, cube.DOWN, square_size, padding*2 + face_size, padding*2 + face_size)
    draw_face(d, cube.RIGHT, square_size, padding*3 + face_size*2, padding*2 + face_size)
    draw_face(d, cube.UP, square_size, padding*4 + face_size*3, padding*2 + face_size)
    draw_face(d, cube.BACK, square_size, padding*2 + face_size, padding)
    draw_face(d, cube.FRONT, square_size, padding*2 + face_size, padding*3 + face_size*2)
    cube_img.show()

def draw_face(drawer, face, square_size, x, y):
    '''
    Function that draws the cube square by square
        - drawer: ImageDraw object, linked with the Image that you want to edit
        - face: face of the Cube object (Cube.BACK, Cube.FRONT, Cube.LEFT...)
        - square_size: the size in px of each piece of the cube
        - x: initial x position for drawing
        - y: initial y position for drawing
    '''
    y1 = y ; y2 = y1 + square_size
    for row in face:
        x1 = x ; x2 = x1+ square_size
        for n in row:
            drawer.rectangle((x1, y1, x2, y2), fill=colors[n], outline='#000000')
            x1 += square_size ; x2 += square_size
        y1 += square_size ; y2 += square_size

def copy_column(face, position, column):
    '''
    Function that overrides a face column with a given column and position
        - face: face of the Cube object (Cube.BACK, Cube.FRONT, Cube.LEFT...)
        - position: position of the column you want to override (0...N-1)
        - column: vector that contains the values you want to override the face with
    '''
    for i in range(0, len(face)):
        face[i][position] = column[i]
    return face

def copy_row(face, position, row):
    '''
    Function that overrides a face row with a given row and position
        - face: face of the Cube object (Cube.BACK, Cube.FRONT, Cube.LEFT...)
        - position: position of the row you want to override (0...N-1)
        - row: vector that contains the values you want to override the face with
    '''
    for i in range(0, len(face)):
        face[position][i] = row[i]
    return face