from aws_cdk import (
    Stack,
    aws_servicecatalog as servicecatalog,
)
from constructs import Construct
import os


class EssentialPortfolio(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the portfolio
        portfolio = servicecatalog.Portfolio(
            self,
            "EssentialPortfolio",
            display_name="Essential Services Portfolio",
            provider_name="Your Organization",
            description="Essential services and resources for all accounts"
        )

        # Add a product with a CloudFormation template asset
        # Use display_name to ensure deterministic asset names and prevent self-mutation loops
        product = servicecatalog.CloudFormationProduct(
            self,
            "VPC_Product_Template",
            product_name="VPC Product",
            owner="Platform Team",
            product_versions=[
                servicecatalog.CloudFormationProductVersion(
                    product_version_name="v1",
                    cloud_formation_template=servicecatalog.CloudFormationTemplate.from_asset(
                        path=os.path.join(os.path.dirname(__file__), "templates", "vpc-template.yaml"),
                        display_name="VPCProductAssetV1"  # Static name prevents self-mutation loop
                    ),
                )
            ],
        )

        portfolio.add_product(product)


class SandboxPortfolio(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the portfolio
        portfolio = servicecatalog.Portfolio(
            self,
            "SandboxPortfolio",
            display_name="Sandbox Portfolio",
            provider_name="Your Organization",
            description="Sandbox environment resources for experimentation"
        )

        # Add a product with a CloudFormation template asset
        # Use display_name to ensure deterministic asset names and prevent self-mutation loops
        product = servicecatalog.CloudFormationProduct(
            self,
            "S3_Bucket_Product",
            product_name="S3 Bucket Product",
            owner="Platform Team",
            product_versions=[
                servicecatalog.CloudFormationProductVersion(
                    product_version_name="v1",
                    cloud_formation_template=servicecatalog.CloudFormationTemplate.from_asset(
                        path=os.path.join(os.path.dirname(__file__), "templates", "s3-template.yaml"),
                        display_name="S3BucketProductAssetV1"  # Static name prevents self-mutation loop
                    ),
                )
            ],
        )

        portfolio.add_product(product)



