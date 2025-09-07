import xml.etree.ElementTree as ET
from typing import Any
from config import DRAWINGS, NAMESPACES

def get_img_dict():

    # Список для результата
    result = dict()

    tree = ET.parse(DRAWINGS)
    root = tree.getroot()

    # Ищем все oneCellAnchor и twoCellAnchor
    for anchor_tag in root.findall("xdr:oneCellAnchor", NAMESPACES) + root.findall("xdr:twoCellAnchor", NAMESPACES):
        # получаем строку верхнего левого угла
        from_tag = anchor_tag.find("xdr:from", NAMESPACES)
        if from_tag is None:
            continue
        row = int(from_tag.find("xdr:row", NAMESPACES).text) + 1  # Excel строки с 1

        # имя картинки
        cNvPr = anchor_tag.find(".//xdr:cNvPr", NAMESPACES)
        if cNvPr is None:
            continue
        img_name = cNvPr.attrib.get("name")

        # сохраняем в список
        result[row] = img_name

    return result

if __name__ == "__main__":
    for key, data in get_img_dict().items():
        print(key, data)
