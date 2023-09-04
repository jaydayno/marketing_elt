FROM apache/airflow:latest-python3.8
ADD requirements.txt . 
RUN pip install "apache-airflow==${AIRFLOW_VERSION}" \
    --no-cache-dir airflow-provider-fivetran-async==1.1.2 -r requirements.txt