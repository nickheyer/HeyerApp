FROM certbot/certbot:latest

ENTRYPOINT [ "/bin/sh", "-c", 'trap exit TERM; while :; do certbot renew; sleep 12h & wait $${!}; done;' ]