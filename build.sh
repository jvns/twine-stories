echo 'building...'
./bin/tweego slow-website.twee common.twee -o slow-website.html
./bin/tweego connection-timeout.twee common.twee -o connection-timeout.html
./bin/tweego problem-dns-update.twee common.twee -o problem-dns-update.html
./bin/tweego 50ms-request.twee common.twee -o 50ms-request.html
