REMOTE=$1
# REMOTE_LOCATION=$2

# # Remove leading and tailing slashs, if either exist, from the user-provided 
# # REMOTE_LOCATION so that we can ensure rsync works as expected
# REMOTE_LOCATION=$(echo $REMOTE_LOCATION | sed 's#/$##' | sed 's#^/##')

echo "Copying docker-compose.yml"
# rsync -chv --progress docker-compose.yml $REMOTE:/$REMOTE_LOCATION/
rsync -chv --progress docker-compose.yml $REMOTE

echo "Copying Nginx config"
rsync -achv --progress ./nginx-conf $REMOTE

echo "Copying .env.prod"
rsync -chv --progress .env.prod $REMOTE

echo "Done!"