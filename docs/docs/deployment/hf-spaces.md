# Hugging Face Spaces

!!! info "NOTE:"
    If you want to use `dstack` alone, it's enough to start the Hub server locally using
    the [`dstack start`](../reference/cli/start.md)
    command. It will allow you to run dev environments, pipelines, and apps both locally
    and in the cloud.
    
    However, if you want to work as a team and manage cloud credentials in a more secure way, you may consider
    deploying the Hub server as a Hugging Face Space.

## Create a space

!!! info "NOTE:"
    Before creating a Hugging Face Space, make sure you're logged in to Hugging Face.

The easiest way to create a Space to run `dstack` is duplicating the
[`dstackai/dstack-template`](https://huggingface.co/spaces/dstackai/dstack-template) Space template
by clicking the button below.

<a href="https://huggingface.co/spaces/dstackai/dstack-template?duplicate=true" 
    class="md-button md-button--primary" target="_blank">Create a Space</a>

## Configure the settings

Once the space is created, click on `Settings` and proceed to configure the visibility and secrets of the space.

### Visibility

Ensure that the visibility of the space is set to `Public`. This is a requirement for the `dstack` CLI to access
the Hub server APIs. Rest assured, the Hub server has its own authentication system and will only allow registered users
to access it.

### Secrets

#### Token

If you want to configure the value of the default token for the admin user, add the `DSTACK_HUB_ADMIN_TOKEN` secret with
the required value.

If you don't do that, dstack will generate it randomly and print it to the `Logs`.

#### Persisting state

If you want the space to maintain the state across restarts, you need to add the secrets that instruct `dstack`
to persist the state in a cloud object storage of your choice.

- `LITESTREAM_REPLICA_URL` - The url of the cloud object storage.
  Examples: `s3://<bucket-name>/<path>`, `gcs://<bucket-name>/<path>`, `abs://<storage-account>@<container-name>/<path>`, etc.

??? info "AWS S3"
    To persist state into an AWS S3 bucket, provide the following environment variables:

    - `AWS_ACCESS_KEY_ID` - The AWS access key ID
    - `AWS_SECRET_ACCESS_KEY` -  The AWS secret access key

??? info "GCP Storage"
    To persist state into an AWS S3 bucket, provide one of the following environment variables:

    - `GOOGLE_APPLICATION_CREDENTIALS` - The path to the GCP service account key JSON file
    - `GOOGLE_APPLICATION_CREDENTIALS_JSON` - The GCP service account key JSON

??? info "Azure Blob Storage"
    To persist state into an Azure blog storage, provide the following environment variable.

    - `LITESTREAM_AZURE_ACCOUNT_KEY` - The Azure storage account key

Once the settings are configured, you can restart the space and log in as an administrator. From there, you can create
users, projects, and configure the `dstack` CLI. This allows you to collaborate as a team, running development
environments, pipelines, and apps securely and conveniently in the cloud without the need to host the Hub server
yourself.