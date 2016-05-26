from _collections import defaultdict


def detect_simple_boxes(text):
    boxes = []
    for top, line in enumerate(text):
        try:
            # Find the left-right range (top of box)
            left = 0
            while left >= 0:
                try:
                    left = line.index('+', left)
                except ValueError:
                    break
                right = left + 1
                while line[right] == '-':
                    right += 1
                if line[right] == '+':
                    # verify sides of box, find bottom
                    bottom = top + 1
                    while text[bottom][left] == '|' and text[bottom][right] == '|':
                        bottom += 1
                    # verify bottom of box
                    expected_bottom = ('-' * (right - left - 1)).join('++')
                    if text[bottom][left:right + 1] == expected_bottom:
                        # +1 is added for use with range()
                        boxes.append((top, bottom + 1, left, right + 1))
                left = right + 1
        except IndexError:
            continue
    return boxes


def get_box_contents(text, box):
    contents = [line[box[2] + 1:box[3] - 1].strip()
                for line in text[box[0] + 1:box[1] - 1]]
    # Remove empty lines
    return ' '.join([line for line in contents if line])


def parse_text_simple(text):
    boxes = detect_simple_boxes(text)
    box_contents = ''
    for box in boxes:
        box_contents += '(' + get_box_contents(text, box) + ') '
    noboxes = text
    for box in boxes:
        for row in range(box[0], box[1]):
            noboxes[row] = noboxes[row][:box[2]] + noboxes[row][box[3]:]
    parsed = ''
    for row, line in enumerate(noboxes):
        if parsed.endswith('-'):
            parsed = parsed[:-1]
        # elif condition prevents any paragraph from starting with a space
        elif not line:
            parsed += '\n'
        elif parsed and not parsed.endswith('\n'):
            parsed += ' '
        parsed += line.strip()
    return box_contents + parsed


def detect_boxes_superduper(text):
    # We COULD assume that + and | toggle the "in a box" state, but let's try
    # for a method that doesn't assume the text won't contain those
    # characters. We WILL assume that the trail following the border of the
    # box is surrounded by whitespace, and that all trails do loop.
    box_ranges = defaultdict(list)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for row, line in enumerate(text):
        for col, char in enumerate(line):
            if char == '+' and col not in box_ranges[row]:
                # New box!
                x, y = row, col
                box = []
                while (x, y) not in box:
                    box.append((x, y))
                    for d in directions:
                        dx, dy = d
                        try:
                            if text[x + dx][y + dy] in '+-|' \
                                    and (x + dx, y + dy) not in box \
                                    and x + dx >= 0 and y + dy >= 0:
                                x += dx
                                y += dy
                                break
                        except:
                            pass
                # Add new box
                new_box_dict = {}
                for new_row in set([x for x, _ in box]):
                    affected_columns = sorted(
                        [y for x, y in box if x == new_row])
                    new_box_dict[new_row] = affected_columns
                    # Ecch, maybe another time.


def parse_text(text):
    parsed = ''  # Parsed text
    boxes = []  # Contents of each box
    current_boxes = ['', '']  # The "current" boxes. [left box, right box]
    current_box = None  # Whether we're looking at a left- or right-aligned box
    for line in text:
        # Start out having encountered no boxes on this line
        boxes_encountered = [False, False]
        in_box = 0  # 0/1/2 == no/inside/on border
        # Handle hyphenation and spacing. Trim extra trailing spaces, remove
        # hyphens, and add the space between words if there was no hyphen.
        if parsed.endswith('-'):
            parsed = parsed[:-1]
        # Don't add a space after a paragraph break!
        elif parsed and not parsed.endswith('\n'):
            parsed += ' '
        # Look at one line at a time; useful for detecting empty lines.
        parsed_line = ''
        for col, char in enumerate(line):
            # Look for boxes! On each line + and | indicate the edge of boxes
            if char in '+|':
                # | always toggles whether we're in a box
                if char == '|':
                    in_box = int(not in_box)
                # + always toggles whether we're on an edge. May not toggle
                # whether we're in a box, such as the 6th line of example 3.
                elif char == '+':
                    in_box = 2 * int(in_box != 2)
                if in_box:
                    # If current_box is unset, we just entered a box. (If it
                    # WAS set, we were inside a box and hit a +)
                    if current_box is None:
                        if col == 0:
                            current_box = 0
                        else:
                            current_box = 1
                        boxes_encountered[current_box] = True
                else:
                    current_box = None
                continue
            if in_box:
                if in_box == 2:
                    continue
                if char == ' ' and current_boxes[current_box].endswith(' '):
                    continue
                current_boxes[current_box] += char
            else:
                if not (parsed_line.endswith(' ') and char == ' '):
                    parsed_line += char
        # Remove extra whitespace from the start/end of the line before adding
        # it to the parsed text.
        parsed_line = parsed_line.strip()
        if not parsed_line:
            parsed_line = '\n'
        parsed += parsed_line
        for box in range(2):
            # End boxes. Example: If we did not encounter a left-aligned box on
            # this row, but we do have data for that box, then we have reached
            # the end of it and need to add it to the list of boxes.
            if current_boxes[box] and not boxes_encountered[box]:
                boxes.append(current_boxes[box])
                current_boxes[box] = ''
    return ' '.join(['(' + box + ')' for box in boxes]) + '\n' + parsed

text = open('input/C225EI.txt').read().splitlines()
print(parse_text(text))
