from figures.polygon import Polygon
from figures.circle import Circle
from figures.point import Point


def svg_path_to_polygon(svg_path):
    points_str = svg_path[svg_path.index('d="') + 3:svg_path.rindex('Z"')]
    bg_color_str = svg_path[(s := svg_path.index('fill="') + 6):svg_path.index('"', s)]
    stroke_color_str = svg_path[
                       (s := svg_path.index('stroke="') + 8):svg_path.index('"', s)] if 'stroke' in svg_path else None

    parsed = list()
    command = None
    args = ''
    for sym in points_str:
        if sym and sym not in ' .0123456789':
            if command and args:
                parsed.append((command, args))
                args = ''
            command = sym
        else:
            args += sym
    if command and args:
        parsed.append((command, args))

    points = list()
    for i in range(len(parsed)):
        command, args = parsed[i]
        command = command.strip()
        args = args.strip()
        if command == 'H':
            if i:
                args = round(float(args)), points[i - 1].y
            else:
                args = round(float(args)), 0
        elif command == 'V':
            if i:
                args = points[i - 1].x, round(float(args))
            else:
                args = 0, round(float(args))
        if command in 'ML':
            args = tuple(round(float(x)) for x in args.split())
        points.append(Point(*args))

    if bg_color_str == 'black':
        bg_color_str = '#000000'
    elif bg_color_str == 'white':
        bg_color_str = '#ffffff'

    if stroke_color_str:
        if stroke_color_str == 'black':
            stroke_color_str = '#000000'
        elif stroke_color_str == 'white':
            stroke_color_str = '#ffffff'

    if stroke_color_str:
        polygon = Polygon(points, bg_color_str, stroke_color_str)
    else:
        polygon = Polygon(points, bg_color_str)
    return polygon


def svg_circle_to_circle(svg_circle):
    bg_color_str = svg_circle[(s := svg_circle.index('fill="') + 6):svg_circle.index('"', s)]
    stroke_color_str = svg_circle[
                       (s := svg_circle.index('stroke="') + 8):svg_circle.index('"',
                                                                                s)] if 'stroke' in svg_circle else None
    cx_str = svg_circle[(s := svg_circle.index('cx="') + 4):svg_circle.index('"', s)]
    cy_str = svg_circle[(s := svg_circle.index('cy="') + 4):svg_circle.index('"', s)]
    r_str = svg_circle[(s := svg_circle.index('r="') + 3):svg_circle.index('"', s)]

    cx = round(float(cx_str))
    cy = round(float(cy_str))
    r = round(float(r_str))

    return Circle(Point(cx, cy), r, bg_color_str)


if __name__ == '__main__':
    while path := input():
        print(svg_path_to_polygon(path))
    for line in open('circles.txt', 'r', encoding='utf-8'):
        print(svg_circle_to_circle(line.strip()), ',', sep='')
