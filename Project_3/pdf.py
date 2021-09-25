# import sys
# import os
# import PyPDF2
#
# original_folder = sys.argv[1]
# new_folder = str(sys.argv[2])
# files_list = os.listdir(original_folder)
#
# if os.path.isdir(new_folder):
#     print(f'Folder exists, putting in folder: {new_folder}')
# else:
#     os.mkdir(new_folder)
#     print(f'Next folder created : {new_folder}')
#
#
# for item in files_list:
#     if '.pdf' in item:
#
#
#
#         os.chdir(original_folder)
#
#         converted = Image.open(item)
#         new_item = item.replace(".jpg", '')
#         os.chdir(new_folder)
#         converted.save(new_item + '.png', 'png')
#         gray = converted.convert('L')
#         file_name = new_item + '_gray_' + '.png'
#         gray.save(file_name, 'png')
#         print(f'File create with name {file_name}')
# print('Work is done')























import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.merge(0, )
    merger.write('super.pdf')

import PyPDF2
from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader, PdfFileWriter

output = PdfFileWriter()

ipdf = PdfFileReader(open('pdf1.pdf', 'rb'))
wpdf = PdfFileReader(open('pdf2.pdf', 'rb'))
for i in xrange(wpdf.getNumPages()):
    watermark = wpdf.getPage(i)
    for i in xrange(ipdf.getNumPages()):
        page = ipdf.getPage(i)

for i in watermark:
    page.mergePage(watermark)
    output.addPage(page)

with open('newfile.pdf', 'wb') as f:
   output.write(f)



pdf_combiner(inputs)
