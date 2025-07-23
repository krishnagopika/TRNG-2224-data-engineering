# DevOps for Azure Data Factory (ADF)

## Continuous Integration (CI)
### Purpose
Continuous Integration ensures that changes made to Azure Data Factory (ADF) components such as pipelines, datasets, and linked services are version-controlled and tested automatically. ADF integrates directly with Git repositories (Azure Repos Git or GitHub), enabling developers to work on feature branches and commit changes without directly impacting production.

### How CI Works in ADF
- Developers connect ADF Studio to a Git repository and work in **Author mode**.
- All changes are made and saved in the Git repository (not directly to Live mode).
- When ready, developers create pull requests and merge changes to the collaboration branch (usually `main` or `master`).
- Publishing from ADF Studio generates ARM templates and commits them to the **publish branch** (typically `adf_publish`).
- A build pipeline can be configured to pick up artifacts from the publish branch for deployment.

## Continuous Deployment (CD)
### Purpose
Continuous Deployment automates the release of ADF artifacts (pipelines, datasets, etc.) from one environment (e.g., Dev) to another (Test/Prod), reducing manual errors and ensuring consistency across environments.

## ADF - Git Configuration
### Steps to Configure Git in ADF Studio
1. Go to ADF Studio → Manage → Git Configuration.
2. Choose your Git repository provider (Azure DevOps Git or GitHub).
3. Select Repository, Collaboration Branch (e.g., `main`), Publish Branch (e.g., `adf_publish`), and Root Folder.
4. Save the configuration.

### Benefits
- Enables version control for all ADF artifacts.
- Supports branching strategy (feature, develop, release).
- Facilitates collaboration among multiple developers.
- Separates development work (collaboration branch) from deployment artifacts (publish branch).

## ARM Templates
Azure Resource Manager (ARM) templates are JSON files that define Azure infrastructure and services declaratively. For ADF, ARM templates represent:
- Pipelines
- Datasets
- Linked services
- Triggers
- Integration Runtimes

### Why ARM Templates Are Used in ADF
- ARM templates are auto-generated when the **Publish** button is clicked in ADF Studio.
- They are automatically committed to the **publish branch** in the Git repository.
- They allow infrastructure as code (IaC) to deploy consistent ADF resources across environments.
- They support parameterization, allowing you to modify settings like connection strings, file paths, and environment-specific configurations for each environment (Dev, Test, Prod).

### Generated Files
When the Publish button is clicked in ADF Studio, the following files are generated in the publish branch:
- `ARMTemplateForFactory.json` - Main ARM template
- `ARMTemplateParametersForFactory.json` - Default parameters file
- `linkedTemplates/` folder - Contains linked templates for complex factories

These templates are stored in the publish branch and used as artifacts in deployment pipelines.

## Build Pipeline (CI)
### Purpose
The build pipeline validates and packages the ADF artifacts for deployment.

### Key Components
- **Source**: Connects to the **publish branch** of the Git repository
- **Artifacts**: Publishes the ARM templates and parameter files as build artifacts
- **Validation**: Can include ARM template validation steps

## Azure DevOps Release Pipelines (CD)
### Purpose
The release pipeline handles deployment of the published ADF ARM templates to different environments using Azure Resource Manager deployment tasks.

### Key Components
#### 1. Artifact
- The artifact is the build output from the build pipeline or directly from the **publish branch**.
- Contains the ARM templates (`ARMTemplateForFactory.json`, `ARMTemplateParametersForFactory.json`) and linked templates.
- This artifact is linked in the release pipeline as the source of deployment files.

#### 2. Pre and Post Deployment Scripts
- **Pre-deployment**: Scripts to stop all triggers before deployment to prevent conflicts
- **Post-deployment**: Scripts to restart triggers after successful deployment

#### 3. Stages
Typically defined for:
- Dev
- Test  
- Prod

Each stage can have its own parameter files and variable groups for environment-specific configurations like connection strings, file paths, and resource names.

#### 4. Deployment Tasks
- **Azure Resource Manager Template Deployment** task to deploy the ADF ARM templates
- Uses service connections for authentication to target Azure subscriptions