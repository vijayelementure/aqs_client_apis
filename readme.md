# AQS mobile APIs

Deploying on AWS Lambda:

1. Create a event handler for the code using Mangum (pip install -U mangum --no-cache)
2. Make sure the CORS headers are in the code
3. Create a package directory and install the pacakages from the below code

    ```shell
    pip install -r requirements.txt --target ./package --platform manylinux_2_17_x86_64 --only-binary=:all:
    ```

4. Create a zip archive for the code including the dependencies in the package directory

    ```shell
    cd package
    zip -r ../deployment_package.zip .

    cd ..
    zip -g deployment_package.zip -r app
    ```

5. Upload the deployment package to s3
6. Deploy the deployment package on AWS Lambda on x86_64 platform
