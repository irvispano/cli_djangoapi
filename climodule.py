from string import whitespace
import click
import requests
import datetime
import json


@click.command()
@click.option("--json_in", type=click.File("r"))
@click.option("--target_currency", type=click.STRING)
def inout(json_in, target_currency):
    
    click.echo("json_in: %s" % json_in)

    while True:
        line = json_in.readline()
        if not line:
            break
        line_json = json.loads(line)
        amount = line_json["value"]
        
        from_currency = line_json["currency"]
        to_currency = target_currency
        url = f"http://127.0.0.1:8002/api/v1/convert/?to_currency={to_currency}&from_currency={from_currency}&amount={amount}"

        if from_currency == to_currency:
            exchange = {"value": amount, "currency": to_currency}
            click.echo(json.dumps(exchange))
            continue
        response = requests.get(url)
        response_json = response.json()

        if response_json["success"] == True:
            exchange = {"value": response_json["result"], "currency": to_currency}
            click.echo(json.dumps(exchange))


if __name__ == "__main__":
    inout()
