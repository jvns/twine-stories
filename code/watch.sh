while true ;do \
    sleep 2s ; \
    find . | entr bash sync.sh
done
