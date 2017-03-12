# grabScreenUrl
grab image screen from list url 

# Usage 
- list.txt
    - http://localhost
    - https://google.it

```{r, engine='bash', count_lines}
./grabscreeenurl.py -i list.txt -g cutycap "--javascript=off --insecure --url=<url> --out=<outfiname>"
```
url and outfiname will replace at runtime

Full example with webkit2png
```{r, engine='bash', count_lines}
./grabscreeenurl.py -i sample_dirsearch.log -c dirsearch -g "webkit2png -o <outfilename> --timeout=2000 <url>"
```

Full example with cutycapt
```{r, engine='bash', count_lines}
/grabscreeenurl.py -i sample_dirsearch.log -c dirsearch -g "cutycap --javascript=off --insecure --url=<url> --out=<outfiname>"
```

# convert param 
convert origin file to flat list url
actual converter is from tool dirsearch -c dirsearch

# todo
implement converter from dirbuster


