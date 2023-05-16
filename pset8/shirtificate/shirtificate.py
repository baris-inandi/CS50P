from fpdf import FPDF


def main():
    name = input("Name: ")

    # init pdf
    pdf = FPDF(format="a4", orientation="portrait")
    pdf.set_auto_page_break(False)
    pdf.add_page()

    # add header
    pdf.set_font("Helvetica", size=48)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 40, "CS50 Shirtificate", align="C")

    # add the shirt
    pdf.set_x(0)
    pdf.set_y(0)
    pdf.image("shirtificate.png", x=0, y=72)

    # add the name
    pdf.set_font("Helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 300, f"{name} took CS50", align="C")
    
    # write the file into "shirtificate.pdf"
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
