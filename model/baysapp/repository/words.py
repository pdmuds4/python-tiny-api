from clients import SqliteClient

from ..._error import RepositoryError
from ..valueObject import Word, Score, NewsCategories


class WordsRepository:
    client: SqliteClient

    def __init__(self, client: SqliteClient):
        self.client = client
        self.cursor = client.cursor()

    def get_news_category_score(self, word: Word, news_category: NewsCategories) -> Score | None:
        try:
            self.cursor.execute(
                f"""
                    SELECT
                        CAST((
                            SELECT {news_category.value} 
                            FROM {self.client.table_name} 
                            WHERE word='{word.value}'
                        ) AS REAL) /
                        CAST((
                            SELECT SUM({news_category.value}) 
                            FROM {self.client.table_name}
                        ) AS REAL)
                    FROM {self.client.table_name};
                """
            )
        except Exception as e:
            raise RepositoryError(
                message = f"SQLiteのクエリ実行中にエラーが発生しました。: {str(e)}",
                detail=str(e),
                status_code=500
            )

        result = self.cursor.fetchone()

        if result[0]:
            return Score(value=result[0])
        else:
            return self.get_laplace_smoothing_score(news_category)


    def get_laplace_smoothing_score(self, news_category: NewsCategories) -> Score | None:
        try:
            self.cursor.execute(
                f"""
                    SELECT
                        1 / CAST(
                            SUM({news_category.value}) + (
                                SELECT COUNT(*) 
                                FROM {self.client.table_name} 
                                WHERE {news_category.value} != 0
                            ) AS REAL
                        )
                    FROM {self.client.table_name};
                """
            )
        except Exception as e:
            raise RepositoryError(
                message = "SQLiteのクエリ実行中にエラーが発生しました。",
                detail=str(e),
                status_code=500
            )

        result = self.cursor.fetchone()
        return Score(value=result[0])