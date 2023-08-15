#!/usr/bin/env python3
import os

import aws_cdk as cdk

from demo_stack.demo_stack import DemoAppStack


app = cdk.App()
DemoAppStack(app, "DemoStack",
    
    )

app.synth()
