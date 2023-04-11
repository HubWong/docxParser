# -*- coding: utf-8 -*-
import docxParser

if __name__=='__main__':
    path ='J:\\Project Python\\docxParser\\assets\\test.docx'
    print('*'*140)
    d = docxParser.DocxParser().get_content(path)
    print(d)
    pass