
# Create a currency conversion api and cli
## API Reference

#### Get request 3 params 
to_currency | from_currency | amount

```http
  GET api/v1/convert/?to_currency=EUR&from_currency=USD&amount=9.95
```

```javascript
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "success": true,
    "query": {
        "from": "USD",
        "to": "EUR",
        "amount": 9.95
    },
    "info": {
        "timestamp": 1674586683,
        "rate": 0.91912
    },
    "date": "2023-01-24",
    "result": 9.145244
}
```

## Deployment

To deploy this project run

```bash
  docker-compose up 
  you can test api on url:
    http://127.0.0.1:8002/api/v1/convert/?to_currency=EUR&from_currency=USD&amount=9.95
  You can test cli by cmd:
  python climodule.py --json_in=filejson.json --target_currency=EUR