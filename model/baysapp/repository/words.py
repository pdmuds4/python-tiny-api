from clients import SqliteClient

from ..._abstruct.repository import RepositoryModel
from ..._error.repository import RepositoryError

from ...baysapp.valueObject import Word, Score


class WordsRepository(RepositoryModel):
    client: SqliteClient

    def __init__(self, client: SqliteClient):
        self.client = client
        self.cursor = client.cursor()

    def get_news_category_score(self, request: Word) -> list[Score] | None:
        table_name = self.client.table_name
        word = request.value

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
            raise RepositoryError(
                message = "SQLiteのクエリ実行中にエラーが発生しました。",
                detail=str(e),
                status_code=500
            )

        result = self.cursor.fetchone()

        if result[0] is None:
            return None
        else:
            return [Score(value=prob) for prob in result]
        
    
    def get_laplace_smoothing_score(self) -> list[Score] | None:
        table_name = self.client.table_name

        try:
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
        except Exception as e:
            raise RepositoryError(
                message = "SQLiteのクエリ実行中にエラーが発生しました。",
                detail=str(e),
                status_code=500
            )

        result = self.cursor.fetchone()

        if result[0] is None:
            return None
        else:
            return [Score(value=prob) for prob in result]