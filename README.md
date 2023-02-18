# steambrowse
Download and view Steam Workshop items with a click!

Setup:
1. Download `steamcmd`, run it, let it update
2. Log in using `steamcmd`, then quit
3. `pip install twisted` or use `requirements.txt`
4. Put `steambrowse.py` in steamcmd's directory and run it
5. Install the `steambrowse.user.js` user script
6. Click on thumbnails to download items, or click on their title to open the item's webpage

Configuration:
- `steambrowse.py` can be run with two parameters: Steam Username and Port to serve on
- If `steambrowse.py` is run without parameters, the default values will be used, which can be set by editing `steambrowse.py`
- To user script has to know the python server's URL, which can be set by editing `steambrowse.user.js`