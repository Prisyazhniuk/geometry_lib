from pyspark.sql import DataFrame
from pyspark.sql.functions import col

def prod_cat_pairs_with_orphans(
    df_prod: DataFrame,
    df_cat: DataFrame,
    df_link: DataFrame
) -> DataFrame:

    prod_with_cat = (
        df_link
        .join(df_cat, on="category_id", how="inner")
        .select("product_id", "category_name")
    )

    result = (
        df_prod
        .join(prod_with_cat, on="product_id", how="left")
        .select(
            col("product_name"),
            col("category_name")
        )
    )

    return result
