from pathlib import Path

import pytest

from segmentmytiff.main import read_input_and_labels_and_save_predictions, FeatureType, get_features_path


def test_integration():
    input_path = Path("test_data") / "test_image.tif"
    labels_path = Path("test_data") / "test_image_labels.tif"
    predictions_path = Path("test_data") / "test_image_predictions.tif"

    read_input_and_labels_and_save_predictions(input_path, labels_path, predictions_path)

    assert predictions_path.exists()

@pytest.mark.parametrize("input_path, feature_type, expected_path", [
    ("input.tiff", FeatureType.FLAIR, "input_FLAIR.tiff"),
    ("../path/to/input.tiff", FeatureType.FLAIR, "../path/to/input_FLAIR.tiff"),
    ("../path/to/input.tiff", FeatureType.IDENTITY, "../path/to/input.tiff"),
])
def test_get_features_path(input_path, feature_type, expected_path):
    features_path = get_features_path(Path(input_path), feature_type)
    assert features_path == Path(expected_path)