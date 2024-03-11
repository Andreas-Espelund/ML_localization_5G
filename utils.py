# geo_utils.py
import numpy as np
import pandas as pd


def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """
    Calculate the great circle distance in meters between two points
    on the earth (specified in decimal degrees).

    :param lat1: latitude of the first point
    :param lon1: longitude of the first point
    :param lat2: latitude of the second point
    :param lon2: longitude of the second
    :return: great circle distance in meters between two points
    """

    # Convert decimal degrees to radians
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])

    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371000  # Radius of Earth in meters
    return c * r


def mean_position_error(y_true: pd.DataFrame, y_pred: pd.DataFrame) -> float:
    """
    Calculate the mean position error in meters between two sets of positions
    :param y_true: ground truth dataframe
    :param y_pred: predicted dataframe
    :return: mean squared error between two sets of positions
    """

    y_true = np.array(y_true, dtype=float)
    y_pred = np.array(y_pred, dtype=float)

    errors = np.array([haversine(true[0], true[1], pred[0], pred[1]) for true, pred in zip(y_true, y_pred)])
    return errors.mean()


def load_dataframe(path: str) -> pd.DataFrame:
    """
    Load the .csv file and return a dataframe with optimized typws
    :param path: path to the .csv file
    :return: a dataframe with optimized
    """
    df = pd.read_csv(path)

    return df.astype({
        "latitude": "float64",
        "longitude": "float64",
        "PCI_cov": "int16",
        "SSBIdx_cov": "int8",
        "SSB_RSSI": "float32",
        "SSS_SINR": "float32",
        "SSS_RSRP": "float32",
        "SSS_RSRQ": "float32",
        "PPS": "float64",
        "ToA_cov": "float64",
        "operator_ID_cov": "int8",
        "campaign_ID_cov": "int8",
        "PCI_cir": "int16",
        "SSBIdx_cir": "int8",
        "ToA_cir": "float32",
        "operator_ID_cir": "int8",
        "campaign_ID_cir": "int8",
    })
