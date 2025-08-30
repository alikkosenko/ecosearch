import xml.etree.ElementTree as ET
from typing import Any

def get_img_dict():
    drawing_file = "drawing1.xml"

    # Пространства имён
    ns = {
        "xdr": "http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing",
        "a": "http://schemas.openxmlformats.org/drawingml/2006/main"
    }

    # Список для результата
    result = dict()

    tree = ET.parse(drawing_file)
    root = tree.getroot()

    # Ищем все oneCellAnchor и twoCellAnchor
    for anchor_tag in root.findall("xdr:oneCellAnchor", ns) + root.findall("xdr:twoCellAnchor", ns):
        # получаем строку верхнего левого угла
        from_tag = anchor_tag.find("xdr:from", ns)
        if from_tag is None:
            continue
        row = int(from_tag.find("xdr:row", ns).text) + 1  # Excel строки с 1

        # имя картинки
        cNvPr = anchor_tag.find(".//xdr:cNvPr", ns)
        if cNvPr is None:
            continue
        img_name = cNvPr.attrib.get("name")

        # сохраняем в список
        result[row] = img_name

    return result

if __name__ == "__main__":
    for key, data in get_img_dict().items():
        print(key, data)
