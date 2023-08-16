#!/usr/bin/env python3
import os

import aws_cdk as cdk

from demo_stack.demo_stack import AppDemoStack


app = cdk.App()
AppDemoStack(app, "AppDemoStack1")

app.synth()
