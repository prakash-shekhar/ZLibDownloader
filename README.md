# ZLibDownloader
**A parser and downloader for Z-Library**

## Example Program:
```python
import zlibdownoader
# minimal search
lst = zlibdownoader.bookSearch('python')
# all options
lst = zlibdownoader.bookSearch('python', exact = True, extension = 'pdf', limit = 1)
# cookies - HIGHLY RECOMMENDED
cookies={'remix_userkey': 'userkey', 'remix_userid': 'userid'}
# download book
downloadBook(lst[0][2], cookies)
```

## How to get cookies
1. Login to Zlibrary
2. Open a javascript console and type ```document.cookies```
3. It should return a string that looks like ```"remix_userkey=userkey; remix_userid=userid"```
4. Turn this into a python dictionary that looks like ```cookies={'remix_userkey': 'userkey', 'remix_userid': 'userid'}```