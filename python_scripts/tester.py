import BLAST_new_alignment_parser as parser
import os


folder_path = "/Users/ginoprasad/Downloads/text_files/"
files = list(os.listdir(folder_path))


content = []
for file in files:
	with open(folder_path + file) as infile:
		content.append(infile.readlines())


parser.parse_batch(files, content, "BATCH.xlsx")
parser.parse(files[0], content[0])




