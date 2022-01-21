set -eux
echo 'building...'

git clone /app /site
cd /site

mkdir public

cp index.html public
for i in slow-website problem-dns-update 50ms-request docker-connection connection-timeout
do
    ./bin/tweego common.twee $i.twee -o public/$i.html
done
