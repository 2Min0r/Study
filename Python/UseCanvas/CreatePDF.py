# coding: utf-8

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import ttfonts
import reportlab.lib.units as unit
import reportlab.lib.pagesizes as pagesizes

# 폰트 등록
pdfmetrics.registerFont(UnicodeCIDFont("HYSMyeongJo-Medium"))
pdfmetrics.registerFont(ttfonts.TTFont("nanumsquare","C:\\windows\\fonts\\NANUMSQUAREL.ttf"))

# PDF를 만든다
pdf = canvas.Canvas("example.pdf", pagesize=pagesizes.A4)

title = "★출시세일★"
for letter in title:    
    # 폰트의 크기는 용지 너비와 같은 210mm
    pdf.setFont("nanumsquare", 210 * unit.mm)
    # 높이
    h = (297 - 210) / 2 * unit.mm
    
    pdf.drawString(0 * unit.mm, h, letter)
    pdf.showPage()

# 저장    
pdf.save()
