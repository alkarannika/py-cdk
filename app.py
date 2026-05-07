#!/usr/bin/env python3
import os

import aws_cdk as cdk

from python_app.python_app_stack import PythonAppStack
from python_app.cdk_cp_pipelines import Pipeline


app = cdk.App()
Pipeline(
    app, 
    "CDKpipelineStack",
    env=cdk.Environment(
        account="339713130314",  # Your AWS account from the connection ARN
        region="us-west-2"
    )
)


app.synth()
