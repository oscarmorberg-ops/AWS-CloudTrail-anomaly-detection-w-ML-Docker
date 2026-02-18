FROM public.ecr.aws/lambda/python:3.12

COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt -t ${LAMBDA_TASK_ROOT}

COPY src/realtime/lambda_handler.py ${LAMBDA_TASK_ROOT}/
COPY src/ml/advanced_features.py ${LAMBDA_TASK_ROOT}/

# FIX: Din funktion heter lambda_handler, inte handler
CMD ["lambda_handler.lambda_handler"]
