import pyPdf
from pdf import PdfFileReader, PdfFileWriter
from matplotlib import pyplot as plt
from numpy.core.setup_common import file

def getPDFContent(path):
    content = ""
    # Load PDF into pyPDF
    pdf = pyPdf.PdfFileReader(file(path, "rb"))
    # Iterate pages
    for i in range(0, pdf.getNumPages()):
        # Extract text from page and add to content
        content += pdf.getPage(i).extractText() + "\n"
    # Collapse whitespace
    content = " ".join(content.replace(u"\xa0", " ").strip().split())
    return content

#  PHASE 1 - Read file data
# page_data = pd.read_csv('Q4_page_data.csv', dtype=str, delimiter=',')
#https://learning.edureka.co/classroom/assignment/777/7016/123422?tab=CourseContent
#file_read = open('inputs/Q4_page_data.csv', 'r')
#file_read = open('https://s3.amazonaws.com/module-non-videos/c8jj1fnsta.pdf')
# file_read = webbrowser.open('https://s3.amazonaws.com/module-non-videos/c8jj1fnsta.pdf')
# print(file_read)

pdf = pyPdf.PdfFileReader(file('https://s3.amazonaws.com/module-non-videos/c8jj1fnsta.pdf', "rb"))
#print(getPDFContent('https://s3.amazonaws.com/module-non-videos/c8jj1fnsta.pdf').encode("ascii", "ignore"))




# count = 0
# llist = []
# for line in file_read:
#     if not line:
#         break
#     if len(line.split(',')) == 8:
#         llist.append(line.strip().split(','))
#         count += 1
#     else:
#         continue
# file_read.close()
# print('\nlines read: \n', llist)
#df = pd.DataFrame(llist, columns=['account_number', 'name', 'item_code', 'category', 'quantity', 'unit price', 'net_price', 'date']])
# print('\nlines read: \n', df)
# #   write file
# output_file = open('Q4_page_data_output.csv','w')
# output_file.writelines((data))
# output_file.close()
#
# #   capture headers of table
# hurricanes_data.head()
# df = pd.DataFrame(hurricanes_data)
# print(df)
# #
# year_data = df['Year']
# month_data = df['Month']
# moscow_data = df['Moscow']
# melbourne_data = df['Melbourne']
# sanfrancisco_data = df['San Francisco']
#

# plt.hist(x_data, y_data)
# plt.show()
