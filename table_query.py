import json
import pandas as pd
import tableqa


class TableQA:
    files = "data/tables/"
    schemas = "data/schemas/"

    @classmethod
    def get_response(cls, query, filename=None):
        if filename:
            df = pd.read_csv(f"data/tables/{filename}.csv")
            with open(f"data/schemas/{filename}.json", "r") as f:
                schema = json.load(f)
            agent = tableqa.Agent(df, schema)
        else:
            agent = tableqa.Agent(cls.files, cls.schemas)

        query = query.lower()
        response = agent.query_db(query)

        response = ", \n\n".join(
            [" ".join([str(part) for part in answer]) for answer in response]
        )

        return response
