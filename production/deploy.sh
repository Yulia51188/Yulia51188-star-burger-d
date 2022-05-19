#!/bin/bash -e
#Build
cd /opt/star-burger-d/
git pull
cd production
docker compose build
docker cp burger_django:/backend/staticfiles/. ../static/
docker cp burger_parcel:/frontend/bundles/. ../static/
#Release
docker exec -it burger_django python manage.py migrate --noinput
docker compose up -d
systemctl reload nginx
#Logging to Rollbar
REVISION=$(git rev-parse --short HEAD)
ROLLBAR_TOKEN=$(cat .env | grep ROLLBAR_TOKEN | cut -d "=" -f 2)
curl -H "Accept: application/json" -H "X-Rollbar-Access-Token: $ROLLBAR_TOKEN" -H "Content-Type: application/json" -X POST 'https://api.rollbar.com/api/1/deploy' -d '{"environment": "production", "revision": "'"$REVISION"'", "status": "succeeded"}'
echo "Deploy $REVISION is finished successfully"
