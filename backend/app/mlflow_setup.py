import mlflow

mlflow.set_experiment("Credit Risk Prediction")

with mlflow.start_run():

    mlflow.log_param("model", "RandomForest")

    mlflow.log_metric("accuracy", 0.92)

    print("MLflow tracking completed")