from os import path
from aws_cdk import (
    Stack,
    aws_servicecatalog as sc,
    aws_iam as iam,
)
from constructs import Construct


class VpcProduct:
    def __init__(self, scope: Construct, team: str, portfolio: sc.Portfolio) -> None:
        product = sc.CloudFormationProduct(
            scope,
            "VPC_Product",
            product_name="VPC",
            owner=f"{team}",
            product_versions=[
                sc.CloudFormationProductVersion(
                    product_version_name="v1.0.0",
                    cloud_formation_template=sc.CloudFormationTemplate.from_asset(
                        path.join(path.dirname(__file__), "templates", "vpc.v1.0.0.yaml")
                    ),
                ),
            ],
            description=f"Provisions VPC under {team} guidance",
            support_email="platform-team@example.com",
        )
        
        portfolio.add_product(product)
        
        role = iam.Role.from_role_name(
            scope,
            "VpcLaunchRole",
            role_name=f"vpc-product-launch-role-{scope.region}",
            mutable=False
        )
        portfolio.set_local_launch_role(product, role)


class S3BucketProduct:
    def __init__(self, scope: Construct, team: str, portfolio: sc.Portfolio) -> None:
        product = sc.CloudFormationProduct(
            scope,
            "S3_Bucket_Product",
            product_name="S3 Bucket",
            owner=f"{team}",
            product_versions=[
                sc.CloudFormationProductVersion(
                    product_version_name="v1.0.0",
                    cloud_formation_template=sc.CloudFormationTemplate.from_asset(
                        path.join(path.dirname(__file__), "templates", "s3-bucket.v1.0.0.yaml")
                    ),
                ),
            ],
            description=f"Provisions S3 Bucket under {team} guidance",
            support_email="platform-team@example.com",
        )
        
        portfolio.add_product(product)
        
        role = iam.Role.from_role_name(
            scope,
            "S3BucketLaunchRole",
            role_name=f"s3-bucket-product-launch-role-{scope.region}",
            mutable=False
        )
        portfolio.set_local_launch_role(product, role)


class Ec2InstanceProduct:
    def __init__(self, scope: Construct, team: str, portfolio: sc.Portfolio) -> None:
        product = sc.CloudFormationProduct(
            scope,
            "EC2_Instance_Product",
            product_name="EC2 Instance",
            owner=f"{team}",
            product_versions=[
                sc.CloudFormationProductVersion(
                    product_version_name="v1.0.0",
                    cloud_formation_template=sc.CloudFormationTemplate.from_asset(
                        path.join(path.dirname(__file__), "templates", "ec2-instance.v1.0.0.yaml")
                    ),
                )
            ],
            description=f"Provisions EC2 Instance under {team} guidance",
            support_email="platform-team@example.com",
        )
        
        portfolio.add_product(product)
        
        role = iam.Role.from_role_name(
            scope,
            "Ec2InstanceLaunchRole",
            role_name=f"ec2-instance-product-launch-role-{scope.region}",
            mutable=False
        )
        portfolio.set_local_launch_role(product, role)


class LambdaFunctionProduct:
    def __init__(self, scope: Construct, team: str, portfolio: sc.Portfolio) -> None:
        product = sc.CloudFormationProduct(
            scope,
            "Lambda_Function_Product",
            product_name="Lambda Function",
            owner=f"{team}",
            product_versions=[
                sc.CloudFormationProductVersion(
                    product_version_name="v1.0.0",
                    cloud_formation_template=sc.CloudFormationTemplate.from_asset(
                        path.join(path.dirname(__file__), "templates", "lambda-function.v1.0.0.yaml")
                    ),
                )
            ],
            description=f"Provisions Lambda Function under {team} guidance",
            support_email="platform-team@example.com",
        )
        
        portfolio.add_product(product)
        
        role = iam.Role.from_role_name(
            scope,
            "LambdaFunctionLaunchRole",
            role_name=f"lambda-function-product-launch-role-{scope.region}",
            mutable=False
        )
        portfolio.set_local_launch_role(product, role)


class EssentialPortfolio(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the portfolio
        portfolio = sc.Portfolio(
            self,
            "EssentialPortfolio",
            display_name="Essential Services Portfolio",
            provider_name="Your Organization",
            description="Essential services and resources for all accounts"
        )

        # Add products to the portfolio
        VpcProduct(self, "Platform Team", portfolio)
        Ec2InstanceProduct(self, "Platform Team", portfolio)


class SandboxPortfolio(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the portfolio
        portfolio = sc.Portfolio(
            self,
            "SandboxPortfolio",
            display_name="Sandbox Portfolio",
            provider_name="Your Organization",
            description="Sandbox environment resources for experimentation"
        )

        # Add products to the portfolio
        S3BucketProduct(self, "Platform Team", portfolio)
        LambdaFunctionProduct(self, "Platform Team", portfolio)



