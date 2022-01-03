echo 'building...'
mkdir -p debug

for i in slow-website problem-dns-update 50ms-request docker-connection connection-timeout
do
    ./bin/tweego common.twee $i.twee -o $i.html
done
