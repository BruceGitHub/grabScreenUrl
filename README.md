# grabScreenUrl
grab image screen from list url 

# Usage 
- list.txt
    - http://localhost
    - https://google.it

```{r, engine='bash', count_lines}
./grabscreenurl.py -i list.txt -g cutycap "--javascript=off --insecure --url=<url> --out=<outfiname>"
```
url and outfiname will replace at runtime

Full example with webkit2png
```{r, engine='bash', count_lines}
./grabscreenurl.py -i sample_dirsearch.log -c dirsearch -g "webkit2png -o <outfilename> --timeout=2000 <url>"
```

Full example with cutycapt
```{r, engine='bash', count_lines}
/grabscreenurl.py -i sample_dirsearch.log -c dirsearch -g "cutycapt --javascript=off --insecure --url=<url> --out=<outfiname>"
```

# convert param 
convert origin file to flat list url

list converter 
- dirsearch -c dirsearch link: https://github.com/maurosoria/dirsearch rev Current Release: v0.3.7 (2016.08.22)

# todo
implement converter from dirbuster


