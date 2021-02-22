# Author: lindafang
# Date: 2020-10-05 15:00
# File: test_attach_html_png.py
import allure


def test_multiple_attachments():
    '''
    attachment_type=
    TEXT = ("text/plain", "txt")
    CSV = ("text/csv", "csv")
    TSV = ("text/tab-separated-values", "tsv")
    URI_LIST = ("text/uri-list", "uri")

    HTML = ("text/html", "html")
    XML = ("application/xml", "xml")
    JSON = ("application/json", "json")
    YAML = ("application/yaml", "yaml")
    PCAP = ("application/vnd.tcpdump.pcap", "pcap")

    PNG = ("image/png", "png")
    JPG = ("image/jpg", "jpg")
    SVG = ("image/svg-xml", "svg")
    GIF = ("image/gif", "gif")
    BMP = ("image/bmp", "bmp")
    TIFF = ("image/tiff", "tiff")

    MP4 = ("video/mp4", "mp4")
    OGG = ("video/ogg", "ogg")
    WEBM = ("video/webm", "webm")

    PDF = ("application/pdf", "pdf")

    '''
    allure.attach.file('1.jpg', attachment_type=allure.attachment_type.JPG)
    allure.attach.file('2.yaml', attachment_type=allure.attachment_type.YAML)
    allure.attach('<head></head><body> 这是个网页说明：下面可有多个 </body>', '附加一个网页具体说明', allure.attachment_type.HTML)
