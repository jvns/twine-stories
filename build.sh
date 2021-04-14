wget https://github.com/tmedwards/tweego/releases/download/v2.1.1/tweego-2.1.1-linux-x64.zip
unzip tweego-2.1.1-linux-x64.zip
mv tweego /usr/local/bin
chmod a+x /usr/local/bin/tweego
mv storyformats /usr/local/bin
tweego slow-website.twee -o index.html
