from aws_cdk import (
    Environment,
    Stack,
    Stage,
    aws_codebuild as codebuild,
    pipelines,
)

from constructs import Construct

from python_app.portfolios import (
    EssentialPortfolio,
    SandboxPortfolio
)


class EssentialPortfolioStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        EssentialPortfolio(self, "EssentialPortfolio")


class SandboxPortfolioStage(Stage):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        SandboxPortfolio(self, "SandboxPortfolio")


class Pipeline(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        source = pipelines.CodePipelineSource.connection(
            'alkarannika/py-cdk',
            'main',
            connection_arn='arn:aws:codestar-connections:us-west-2:339713130314:connection/829d9a98-1d7f-40be-b853-0194db048f21',
            trigger_on_push=True
        )

        pipeline = pipelines.CodePipeline(
            self,
            "Pipeline",
            pipeline_name="cdk-service-catalog-pipeline",
            self_mutation=True,  # Re-enabled now that we have static asset names
            cli_version="2.1121.0",  # Match the CDK CLI version
            code_build_defaults=pipelines.CodeBuildOptions(
                build_environment=codebuild.BuildEnvironment(
                    build_image=codebuild.LinuxBuildImage.from_code_build_image_id(
                        "aws/codebuild/standard:8.0"
                    ),
                ),
            ),
            synth=pipelines.ShellStep(
                "Synth",
                input=source,
                commands=[
                    "pip install -r requirements.txt",
                    "npx cdk synth",
                ],
                primary_output_directory="cdk.out",
            ),
        )
        wave = pipeline.add_wave("Portfolios")
        wave.add_stage(
            EssentialPortfolioStage(self,"EssentialPortfolio",
                env=Environment(
                   account=self.account,
                   region="us-west-2"
                )
            )
        )

        wave.add_stage(
            SandboxPortfolioStage(self,"SandboxPortfolio",
                env=Environment(
                   account=self.account,
                   region="us-west-2"
                )
            )
        )
        
        # Build the pipeline to finalize the structure
        pipeline.build_pipeline()