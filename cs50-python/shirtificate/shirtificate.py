from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("helvetica", size=36)
        # Moving cursor to the right:
        self.cell(80)
        # Printing title:
        self.cell(30, 30, "CS50 Shirtificate",  border=0, align="C")
        # Performing a line break:
        self.ln(20)
        page_width = self.w
        image_width = 190
        # Calculate the x position for centering
        x_pos = (page_width - image_width) / 2
        self.image("shirtificate.png",x_pos, 50, image_width)

    def write_on_shirt(self, name):
        self.set_text_color(255, 255, 255)
        self.set_font("helvetica", size=24)
        self.cell(80)
        self.cell(30, 170, f"{name} took CS50", align="C")


pdf = PDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
name = input('Name: ').strip()
pdf.write_on_shirt(name)
pdf.output("shirtificate.pdf")
