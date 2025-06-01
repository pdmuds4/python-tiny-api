from clients import SqliteClient
from ..._abstruct.service import ServiceModel
from ...baysapp.valueObject import Score


class GetLaplaceSmoothingProbService(ServiceModel):
    client: SqliteClient

    def __init__(self, client: SqliteClient):
        super().__init__(client=client, request=None)
        self.cursor = self.client.cursor()


    def execute(self) -> list[Score] | None:
        table_name = self.client.table_name

        self.cursor.execute(
            f"""
                SELECT
                    1 / CAST(
                        SUM(weather) + 
                        (SELECT COUNT(*) FROM {table_name} WHERE weather != 0) AS REAL
                    ),
                    1 / CAST(
                        SUM(life) + 
                        (SELECT COUNT(*) FROM {table_name} WHERE life != 0) AS REAL
                    ),
                    1 / CAST(
                        SUM(sports) + 
                        (SELECT COUNT(*) FROM {table_name} WHERE sports != 0) AS REAL
                    ),
                    1 / CAST(
                        SUM(culture) + 
                        (SELECT COUNT(*) FROM {table_name} WHERE culture != 0) AS REAL
                    ),
                    1 / CAST(
                        SUM(economy) + 
                        (SELECT COUNT(*) FROM {table_name} WHERE economy != 0) AS REAL
                    )
                FROM {table_name};
            """
        )

        result = self.cursor.fetchone()

        if result[0] is None:
            return None
        else:
            return [Score(value=prob) for prob in result]