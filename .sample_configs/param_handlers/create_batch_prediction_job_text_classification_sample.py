# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

def make_parent(parent: str) -> str:
    parent = parent

    return parent

def make_batch_prediction_job(
    display_name: str,
    model: str,
    gcs_source_uri: str,
    gcs_destination_output_uri_prefix: str,
) -> google.cloud.aiplatform_v1beta1.types.batch_prediction_job.BatchPredictionJob:
    model_parameters_dict = {}
    model_parameters = to_protobuf_value(model_parameters_dict)

    batch_prediction_job = {
        "display_name": display_name,
        # Format: 'projects/{project}/locations/{location}/models/{model_id}'
        "model": model,
        "model_parameters": model_parameters,
        "input_config": {
            "instances_format": "jsonl",
            "gcs_source": {"uris": [gcs_source_uri]},
        },
        "output_config": {
            "predictions_format": "jsonl",
            "gcs_destination": {"output_uri_prefix": gcs_destination_output_uri_prefix},
        },
    }

    return batch_prediction_job

