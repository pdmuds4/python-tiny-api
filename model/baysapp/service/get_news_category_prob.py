from clients import SqliteClient
from ..._abstruct.service import ServiceModel
from ...baysapp.valueObject import Word, Score
from ..._error.service import ServiceError

class GetNewsCategoryProbService(ServiceModel):
    client: SqliteClient
    request: Word

    def __init__(self, client: SqliteClient, request: Word):
        self.client = client
        self.cursor = client.cursor()
        self.request = request


    def execute(self) -> list[Score] | None:
        table_name = self.client.table_name
        word = self.request.value

        try:
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
        except Exception as e:
            raise ServiceError(
                message = "SQLiteのクエリ実行中にエラーが発生しました。",
                detail=str(e),
                status_code=500
            )

        result = self.cursor.fetchone()

        if result[0] is None:
            return None
        else:
            return [Score(value=prob) for prob in result]