```console
doppler run --command="uvicorn main:app --host 0.0.0.0 --port 8000 --ssl-keyfile=./certs/key.pem --ssl-certfile=./certs/cert.pem" >uvicorn.log 2>&1 &
```
