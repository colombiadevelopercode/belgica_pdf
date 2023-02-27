from fpdf import FPDF

from styles import *

class PDF(FPDF):

    def header(self):
        
        self.image('logo.jpg',
                x = 20, y = 10, w = 20, h = 30)

        self.set_font('Arial', '', 15)     

        self.cell(w = 0, h = 20, txt = '', border = 0, ln=1,
                 align = 'C', fill = 0)


        self.ln(12)

    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-20)

        # Arial italic 8
        self.set_font('Arial', 'I', 12)

        # Page number
        # self.cell(w = 0, h = 10, txt =  'Pagina ' + str(self.page_no()) + '/{nb}',
        #          border = 0,
        #         align = 'C', fill = 0)   
        self.cell(w = 0, h = 10, txt =   str(self.page_no()) ,
                 border = 0,
                align = 'C', fill = 0)   


