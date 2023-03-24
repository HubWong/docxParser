# -*- coding: utf-8 -*-
import docxParser

if __name__=='__main__':
    path ='D:\\cv.docx'
    d = docxParser.DocxParser().get_content(path)
    print(d)
    pass