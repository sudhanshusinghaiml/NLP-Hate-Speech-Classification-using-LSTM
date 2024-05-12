from dataclasses import dataclass

# Data Ingestion Artifacts
@dataclass
class DataIngestionArtifacts:
    imbalance_data_path: str
    raw_data_path: str


@dataclass
class DataValidationArtifacts:
    imbalance_dataset_columns: set
    raw_dataset_columns: set


@dataclass
class DataTransformationArtifacts:
    transformed_data_path: str


@dataclass
class ModelTrainingArtifacts:
    trained_model_path:str
    x_test_path: list
    y_test_path: list


@dataclass
class ModelEvaluationArtifacts:
    is_model_accepted: bool



@dataclass
class ModelPusherArtifacts:
    bucket_name: str