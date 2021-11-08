echo 'building...'
mkdir -p debug

for i in failed-decryption slow-website problem-dns-update 50ms-request docker-connection
do
    ./bin/tweego $i.twee common.twee -o $i.html
    python3 dotify.py $i.twee | dot -Tsvg > debug/$i.svg
done

dot -Tsvg code/failed-decryption/story.dot > code/failed-decryption/story.svg
