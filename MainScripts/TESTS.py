from pdfrw import PdfReader, PdfWriter

trailer = PdfReader("C:\\Users\\Asif\\Desktop\\1\\1.pdf")
my=trailer.Info.Title
my=my.replace("(", " ")
my=my.replace(")", " ")


trailer.Info.Title = "{sdasd}"+my
PdfWriter("C:\\Users\\Asif\\Desktop\\2\\edited.pdf", trailer=trailer).write()