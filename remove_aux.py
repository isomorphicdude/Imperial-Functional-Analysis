import os
import glob

to_remove = ['aux', 'gz', 'fls', 'log', 'out', 
             'toc', 'blg', 'fdb_latexmk', 
            'bcf', 'xml', 'dvi', 'pdf']

if __name__ == "__main__":
    if 'tex' in to_remove:
        raise Exception("\nDo not remove .tex\n")
    else:    
        for item in to_remove:            
            aux_list = glob.glob(f"**/*.{item}", recursive = True)
            for dir in aux_list:    
                try:
                    os.remove(dir)
                    print(f"Removed {dir}")
                except:
                    print(f"Error removing {dir}")
        print('\nDone.')