import img2pdf
import sys
import os

filepath = sys.argv[1]
pdfname = sys.argv[2]
if os.path.isdir(filepath):
    with open(f"{pdfname}.pdf", "wb") as f:
        imgs = []
        for fname in os.listdir(filepath):
            if not fname.endswith((".png", ".jpeg", ".jpg", ".gif")):
                continue
            path = os.path.join(filepath, fname)
            if os.path.isdir(path):
                continue
            imgs.append(path)
        f.write(img2pdf.convert(imgs))
elif os.path.isfile(filepath):
    if filepath.endswith(".PNG"):
        with open(f"{pdfname}.pdf", "wb") as f:
            f.write(img2pdf.convert(filepath))
else:
    print("Please input file or dir")