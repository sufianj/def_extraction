import os
import re
import csv
import sys

def extract_definitions(tex_file, csv_file):
    with open(tex_file, 'r', errors='replace') as f:
        tex_content = f.read()
    doc = tex_content.split("begin{document}")
    if (len(doc) >= 2) :
        doc = doc[1]
        definitions = re.findall(r'\\begin{definition}\[(.*?)](.*?)\\end{definition}', doc, re.DOTALL)
        
        theorem_sentences = re.findall(r'\\begin{theorem}(.*?)\\end{theorem}', doc, re.DOTALL)
        thm_it_sentences = [sent for sent in theorem_sentences if '\\textit{' in sent]
        thm_it_terms = [re.findall(r'\\textit{(.*?)}', sent) for sent in thm_it_sentences]
        thm_emph_sentences = [sent for sent in theorem_sentences if '\\emph{' in sent]
        thm_emph_terms = [re.findall(r'\\emph{(.*?)}', sent) for sent in thm_emph_sentences]
        
        def_sentences = re.findall(r'\\begin{definition}(.*?)\\end{definition}', doc, re.DOTALL)
        def_it_sentences = [sent for sent in def_sentences if '\\textit{' in sent]
        def_it_terms = [re.findall(r'\\textit{(.*?)}', sent) for sent in def_it_sentences]
        def_emph_sentences = [sent for sent in def_sentences if '\\emph{' in sent]
        def_emph_terms = [re.findall(r'\\emph{(.*?)}', sent) for sent in def_emph_sentences]
        with open(csv_file, 'a') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            for definition in definitions:
                writer.writerow([definition[0].strip(), definition[1].strip(), tex_file, "definition[]"])
            for sent, term_list in zip(thm_it_sentences, thm_it_terms):
                writer.writerow([';'.join(term_list), sent, tex_file, "theorem + \\textit{}"])
            for sent, term_list in zip(thm_emph_sentences, thm_emph_terms):
                writer.writerow([';'.join(term_list), sent, tex_file, "theorem + \\emph{}"])
            for sent, term_list in zip(def_it_sentences, def_it_terms):
                writer.writerow([';'.join(term_list), sent, tex_file, "definition + \\textit{}"])
            for sent, term_list in zip(def_emph_sentences, def_emph_terms):
                writer.writerow([';'.join(term_list), sent, tex_file, "definition + \\emph{}"])
                
if __name__ == '__main__':
    # Check that two arguments were provided
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} TEX_DIR CSV_FILE')
        sys.exit(1)

    # Set the directory containing the .tex files
    tex_dir = sys.argv[1]

    # Set the path to the output .csv file
    csv_file = sys.argv[2]

    # Extract the definitions
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(["term", "def", "file_name", "extraction_rule"])
    for subdir, dirs, filenames in os.walk(tex_dir):
        for filename in filenames:
            filepath = tex_dir + filename
            print(filepath)
            try:
                extract_definitions(filepath, csv_file)
            except (UnicodeDecodeError) as error:
                print(filepath + f'UnicodeDecodeError: {error}')
                continue
            except (FileNotFoundError) as error:
                print(filepath + " NOT FOUND!!")
                continue
    extract_definitions(filepath, csv_file)