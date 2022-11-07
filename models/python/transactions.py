import dateutil


def try_dateutil_parse(x):
    try:
        return dateutil.parser.parse(x)
    except:
        return


def model(dbt, session):
    df = dbt.ref("tpch.snowflake_contract_rates")

    df['parsed_transaction_time'] = df['effective_date'].apply(try_dateutil_parse)

    return df
