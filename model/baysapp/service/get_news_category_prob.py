from clients import SqliteClient
from ..._abstruct.service import ServiceModel
from ...baysapp.valueObject import Word, Score


class GetNewsCategoryProbService(ServiceModel):
    client: SqliteClient
    request: Word

    def __init__(self, client: SqliteClient, word: Word):
        super().__init__(client=client, request=word)
        self.cursor = self.client.cursor()


    def execute(self) -> list[Score] | None:
        table_name = self.client.table_name
        word = self.request.value

        self.cursor.execute(
            f"""
                SELECT
                    CAST((SELECT weather FROM {table_name} WHERE word='{word}') AS REAL) /
                    CAST(SUM(weather) AS REAL),
                    CAST((SELECT life FROM {table_name} WHERE word='{word}') AS REAL) /
                    CAST(SUM(life) AS REAL),
                    CAST((SELECT sports FROM {table_name} WHERE word='{word}') AS REAL) /
                    CAST(SUM(sports) AS REAL),
                    CAST((SELECT culture FROM {table_name} WHERE word='{word}') AS REAL) /
                    CAST(SUM(culture) AS REAL),
                    CAST((SELECT economy FROM {table_name} WHERE word='{word}') AS REAL) /
                    CAST(SUM(economy) AS REAL)
                FROM {table_name};
            """
        )

        result = self.cursor.fetchone()

        if result[0] is None:
            return None
        else:
            return [Score(value=prob) for prob in result]