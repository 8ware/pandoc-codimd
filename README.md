
Pandoc Filters for CodiMD
=========================

1. Install requirements
   ```
   $ pip3 install -r requirements.txt
   $ git submodule update --init
   ```
2. Convert Markdown file
   ```
   $ (cat <header>.yaml; ./preprocess.sh <file>.md) \
       | pandoc -F codimd.py -o <file>.pdf
   ```

