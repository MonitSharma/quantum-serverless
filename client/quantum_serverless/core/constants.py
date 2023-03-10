"""Constants."""


META_TOPIC: str = "execution-meta"

QS_EXECUTION_WORKLOAD_ID: str = "QS_EXECUTION_WORKLOAD_ID"
QS_EXECUTION_UID: str = "QS_EXECUTION_UID"

QS_EVENTS_REDIS_HOST: str = "QS_EVENTS_REDIS_HOST"
QS_EVENTS_REDIS_PORT: str = "QS_EVENTS_REDIS_PORT"
QS_EVENTS_REDIS_PASSWORD: str = "QS_EVENTS_REDIS_PASSWORD"


# telemetry
OT_PROGRAM_NAME = "OT_PROGRAM_NAME"
OT_PROGRAM_NAME_DEFAULT = "unnamed_execution"
OT_JAEGER_HOST = "OT_JAEGER_HOST"
OT_JAEGER_HOST_KEY = "OT_JAEGER_HOST_KEY"
OT_JAEGER_PORT_KEY = "OT_JAEGER_PORT_KEY"
OT_TRACEPARENT_ID_KEY = "OT_TRACEPARENT_ID_KEY"
OT_SPAN_DEFAULT_NAME = "entrypoint"
OT_ATTRIBUTE_PREFIX = "qs"
OT_LABEL_CALL_LOCATION = "qs.location"

# container image
RAY_IMAGE = "qiskit/quantum-serverless-ray-node:latest-py39"