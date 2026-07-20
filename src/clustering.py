import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def create_spending_clusters(df: pd.DataFrame, number_of_clusters: int = 3) -> pd.DataFrame:
    """
    Group expenses into spending clusters using KMeans.
    """
    df = df.copy()

    features = df[["amount", "category", "payment_method", "day_of_week"]]

    encoded_features = pd.get_dummies(
        features,
        columns=["category", "payment_method", "day_of_week"],
        drop_first=False
    )

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(encoded_features)

    model = KMeans(
        n_clusters=number_of_clusters,
        random_state=42,
        n_init="auto"
    )

    df["cluster"] = model.fit_predict(scaled_features)

    return df