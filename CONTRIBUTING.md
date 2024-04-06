# Contributing

Contributions are welcome, and greatly appreciated! Every little bit helps, and credit will always be given.

Read on if you want to learn about how our team contributes to our project's development (Internal Contributions) and how you can get involved (External Contributions).

## Internal Contributions

Our team follows the [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow). This includes creating new branches to work on changes. When the changes are ready a pull request is made, accompanied by linked issues to facilitate discussion and review. After approval, the changes are merged to incorporate the new feature or fix to our project. Branches no longer in use are deleted to maintain a tidy repository.

## External Contributions

Here are the different types of contributions you can make!

### &blacktriangleright; Report Bugs

If you are reporting a bug, please open an [issue](https://github.com/UBC-MDS/DSCI-532_2024_9_solar-savers/issues) and include:

* A clear, yet concise, description of the bug, indicating details that would be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### &blacktriangleright; Fix Bugs

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help wanted" is open to whoever wants to implement it.

### &blacktriangleright; Implement Features

Look through the GitHub issues for features. Anything tagged with "enhancement" and "help wanted" is open to whoever wants to implement it.

###  &blacktriangleright; Submit Feedback

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope narrow, so its easier to implement.
* Remember that this is a volunteer-driven project, and that contributions  are welcome :)

## Get Started!

Here's how to set up for local development.

1. Clone the repository locally. In your terminal run:

    ```console
    $ git clone https://github.com/UBC-MDS/DSCI-532_2024_9_solar-savers.git
    ```

2. Create and activate the `conda` environment. In the root of the repository run:
    ```console
    $ conda env create --file environment.yml
    ```

    ```console
    $ conda activate solar-saver 
    ```

3. Create a branch for local development and make your changes:

    ```console
    $ git checkout -b name-of-your-fix-or-feature
    ```

4. To run the dashboard, navigate to `src` then run `app.py`: 

    ```console
    $ cd src
    ```
    ```console
    $ python app.py
    ```

4. When you're done making changes, check that your changes conform to any code formatting requirements.

5. Commit and push your changes, then open a pull request with a detailed description outlining your contribution. 

## Code of Conduct

Please note that the Solar Savers project is released with a [Code of Conduct](CODE_OF_CONDUCT.md). By contributing to the development of this project you agree to abide by its terms.

## Attribution

This document was adpated from the `eda_mds` package, developed in DSCI 524 held in 2024, found [here](https://github.com/UBC-MDS/eda_mds/blob/main/CONTRIBUTING.md). 
