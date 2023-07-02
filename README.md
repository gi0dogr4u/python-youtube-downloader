# python-youtube-downloader

## Purpose
This is a simple code using pytube 15.0.0 to download a playlist in video or audio format with high resolution and quality
Basicly, a folder with playlist name is created and the videos will be downloaded, one by one.

## Code working
![image](https://github.com/gi0dogr4u/python-youtube-downloader/assets/86978023/e16b6255-0c80-466b-b61e-87c046e15690)
![image](https://github.com/gi0dogr4u/python-youtube-downloader/assets/86978023/71dfecbe-ac46-4ee2-8087-50f55c9e1c1b)
![image](https://github.com/gi0dogr4u/python-youtube-downloader/assets/86978023/d6809ba7-e9a8-4957-867b-ea3354b816e0)

## Error you may face
In my first try using this code, occureed a error like: ``get_throttling_function_name: could not find match for multiple``. 
Searching in web, I found many resolutions but the only one that worked was in a issue thread: https://github.com/pytube/pytube/issues/1678

I just changed the variable ``function_patterns`` of ``get_throttling_function_name`` method, replacing the original code with:

```
def get_throttling_function_name(js: str) -> str:
    """Extract the name of the function that computes the throttling parameter.

    :param str js:
        The contents of the base.js asset file.
    :rtype: str
    :returns:
        The name of the function used to compute the throttling parameter.
    """
    function_patterns = [
        # https://github.com/ytdl-org/youtube-dl/issues/29326#issuecomment-865985377
        # https://github.com/yt-dlp/yt-dlp/commit/48416bc4a8f1d5ff07d5977659cb8ece7640dcd8
        # var Bpa = [iha];
        # ...
        # a.C && (b = a.get("n")) && (b = Bpa[0](b), a.set("n", b),
        # Bpa.length || iha("")) }};
        # In the above case, `iha` is the relevant function name

        # Corrected code to works in pytube 15.0.0
        r'a\.[a-zA-Z]\s*&&\s*\([a-z]\s*=\s*a\.get\("n"\)\)\s*&&.*?\|\|\s*([a-z]+)',
        r'\([a-z]\s*=\s*([a-zA-Z0-9$]+)(\[\d+\])?\([a-z]\)',
    ]
```

good luck with your videos! 
