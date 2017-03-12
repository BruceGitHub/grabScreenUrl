# grabScreenUrl
grab image screen from list url 

# Usage 
- list.txt
    - http://localhost
    - https://google.it

./grabscreeenurl.py -i list.txt -g cutycap --javascript=off --insecure --url=<url> --out=<outfiname>
url and outfiname will replace at runtime

Full example with webkit2png
/grabscreeenurl.py -i list.txt -c sample_dirsearch.log -g "webkit2png -o <outfiname> --timeout=2000 <url>"

Full example with cutycapt
/grabscreeenurl.py -i list.txt -c sample_dirsearch.log -g "cutycap --javascript=off --insecure --url=<url> --out=<outfiname>"

# convert param 
convert origin file to flat list url
actual converter is from tool dirsearch -c dirsearch

# todo
implement converter from dirbuster


